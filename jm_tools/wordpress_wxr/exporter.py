"""
WordPress WXR XML to Markdown exporter.

Converts a WordPress WXR (WordPress eXtended RSS) export file into
individual Markdown files with YAML front matter.
"""

import hashlib
import logging
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Optional, Set

import markdownify
import yaml

logger = logging.getLogger(__name__)

# XML namespace URIs used in WXR files
WP_NS = "http://wordpress.org/export/1.2/"
CONTENT_NS = "http://purl.org/rss/1.0/modules/content/"
DC_NS = "http://purl.org/dc/elements/1.1/"
EXCERPT_NS = "http://wordpress.org/export/1.2/excerpt/"

# Default output directory
DEFAULT_OUT_DIR = Path("data/writing/wordpress")

# Front matter key order
FRONT_MATTER_KEY_ORDER = [
    "title",
    "date",
    "url",
    "source",
    "wp",
    "tags",
    "categories",
]


@dataclass
class ExportReport:
    """Report returned by WordpressWxrExporter.run()."""

    exported: int
    skipped: int
    errors: list


def _slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    Lowercase, replace non-alphanumeric with hyphens, collapse multiple
    hyphens, strip leading/trailing hyphens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = text.strip("-")
    return text


def _get_text(element, tag, default=""):
    """Get text content of a child element, or default if missing/empty."""
    child = element.find(tag)
    if child is not None and child.text:
        return child.text.strip()
    return default


def _parse_wp_datetime(date_str: str) -> Optional[datetime]:
    """Parse a WordPress-format datetime string (YYYY-MM-DD HH:MM:SS)."""
    if not date_str or not date_str.strip():
        return None
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d %H:%M:%S")
    except (ValueError, TypeError):
        return None


def _parse_rfc2822_datetime(date_str: str) -> Optional[datetime]:
    """Parse an RFC 2822 date string (pubDate format)."""
    if not date_str or not date_str.strip():
        return None
    try:
        return parsedate_to_datetime(date_str.strip())
    except (ValueError, TypeError):
        return None


def _resolve_date(item) -> Optional[datetime]:
    """Resolve the best available date from a WXR item element.

    Fallback order: post_date_gmt -> pubDate -> post_date.
    Invalid/unparseable dates are skipped with a warning.
    """
    # Try post_date_gmt first
    gmt_str = _get_text(item, f"{{{WP_NS}}}post_date_gmt")
    if gmt_str:
        dt = _parse_wp_datetime(gmt_str)
        if dt:
            return dt
        logger.warning("Unparseable post_date_gmt: %s, falling back", gmt_str)

    # Try pubDate
    pub_str = _get_text(item, "pubDate")
    if pub_str:
        dt = _parse_rfc2822_datetime(pub_str)
        if dt:
            return dt
        logger.warning("Unparseable pubDate: %s, falling back", pub_str)

    # Try post_date
    post_str = _get_text(item, f"{{{WP_NS}}}post_date")
    if post_str:
        dt = _parse_wp_datetime(post_str)
        if dt:
            return dt
        logger.warning("Unparseable post_date: %s", post_str)

    return None


def _resolve_slug(item) -> str:
    """Resolve slug from wp:post_name or slugified title."""
    post_name = _get_text(item, f"{{{WP_NS}}}post_name")
    if post_name:
        return post_name

    title = _get_text(item, "title", "untitled")
    return _slugify(title)


def _html_to_markdown(html_content: str) -> str:
    """Convert HTML content to Markdown using markdownify.

    Strips inline style and class attributes.
    """
    if not html_content:
        return ""

    # Strip style and class attributes before conversion
    html_content = re.sub(r'\s+style="[^"]*"', "", html_content)
    html_content = re.sub(r"\s+style='[^']*'", "", html_content)
    html_content = re.sub(r'\s+class="[^"]*"', "", html_content)
    html_content = re.sub(r"\s+class='[^']*'", "", html_content)

    md = markdownify.markdownify(html_content, heading_style="ATX", strip=["style"])
    return md.strip()


def _build_front_matter(
    title: str,
    date: Optional[datetime],
    url: str,
    post_id: str,
    post_type: str,
    status: str,
    slug: str,
    tags: list,
    categories: list,
) -> str:
    """Build YAML front matter string with stable key order."""
    # Build ordered dict-like structure manually to maintain key order
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S") if date else ""

    # Use an OrderedDict-style approach via list of tuples to ensure stable order
    lines = []
    lines.append("---")
    lines.append("# source: wordpress export")
    lines.append(f"title: {yaml.dump(title, default_flow_style=True, allow_unicode=True).strip()}")
    lines.append(f"date: {yaml.dump(date_str, default_flow_style=True, allow_unicode=True).strip()}")
    lines.append(f"url: {yaml.dump(url, default_flow_style=True, allow_unicode=True).strip()}")
    lines.append('source: "wordpress"')
    lines.append("wp:")
    lines.append(f"  id: {yaml.dump(post_id, default_flow_style=True, allow_unicode=True).strip()}")
    lines.append(f"  post_type: {yaml.dump(post_type, default_flow_style=True, allow_unicode=True).strip()}")
    lines.append(f"  status: {yaml.dump(status, default_flow_style=True, allow_unicode=True).strip()}")
    lines.append(f"  slug: {yaml.dump(slug, default_flow_style=True, allow_unicode=True).strip()}")
    lines.append(f"tags: {yaml.dump(tags, default_flow_style=True, allow_unicode=True).strip()}")
    lines.append(f"categories: {yaml.dump(categories, default_flow_style=True, allow_unicode=True).strip()}")
    lines.append("---")

    return "\n".join(lines) + "\n"


def _extract_tags(item) -> list:
    """Extract post tags from category elements with domain='post_tag'."""
    tags = []
    for cat in item.findall("category"):
        if cat.get("domain") == "post_tag":
            nicename = cat.get("nicename", "")
            if nicename:
                tags.append(nicename)
    return tags


def _extract_categories(item) -> list:
    """Extract categories from category elements with domain='category'."""
    categories = []
    for cat in item.findall("category"):
        if cat.get("domain") == "category":
            nicename = cat.get("nicename", "")
            if nicename:
                categories.append(nicename)
    return categories


class WordpressWxrExporter:
    """Converts WordPress WXR XML exports to Markdown files.

    Parameters
    ----------
    wxr_path : Path
        Path to the WXR XML export file.
    out_dir : Path
        Output directory for Markdown files.
    post_types : set
        Set of wp:post_type values to export.
    statuses : set
        Set of wp:status values to export.
    overwrite : bool
        If True, overwrite existing files even when content is unchanged.
    incremental : bool
        If True, skip writing when file content hash matches.
    max_posts : int or None
        Maximum number of posts to export. None means no limit.
    """

    def __init__(
        self,
        wxr_path,
        out_dir=None,
        post_types=None,
        statuses=None,
        overwrite=False,
        incremental=True,
        max_posts=None,
    ):
        self.wxr_path = Path(wxr_path)
        self.out_dir = Path(out_dir) if out_dir is not None else DEFAULT_OUT_DIR
        self.post_types = post_types if post_types is not None else {"post"}
        self.statuses = statuses if statuses is not None else {"publish"}
        self.overwrite = overwrite
        self.incremental = incremental
        self.max_posts = max_posts

    def run(self) -> ExportReport:
        """Execute the export and return an ExportReport."""
        exported = 0
        skipped = 0
        errors = []
        used_filenames = set()

        # Create output directory
        self.out_dir.mkdir(parents=True, exist_ok=True)

        # Read and sanitize XML content (fix unescaped ampersands)
        try:
            raw_xml = self.wxr_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            raise Exception(f"Cannot read {self.wxr_path}: {e}") from e

        # Fix bare & that aren't part of XML entities
        raw_xml = re.sub(
            r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)",
            "&amp;",
            raw_xml,
        )

        # Parse sanitized XML
        try:
            root = ET.fromstring(raw_xml)
        except ET.ParseError as e:
            raise Exception(f"XML parse error: {e}") from e

        # Find all <item> elements (they may be under <channel>)
        for elem in root.iter("item"):
            # Check max_posts cap
            if self.max_posts is not None and exported >= self.max_posts:
                elem.clear()
                continue

            # Extract post type and status for filtering
            post_type = _get_text(elem, f"{{{WP_NS}}}post_type")
            status = _get_text(elem, f"{{{WP_NS}}}status")

            if post_type not in self.post_types:
                elem.clear()
                continue

            if status not in self.statuses:
                elem.clear()
                continue

            # Extract fields
            title = _get_text(elem, "title", "Untitled")
            post_id = _get_text(elem, f"{{{WP_NS}}}post_id", "0")
            link = _get_text(elem, "link", "")
            date = _resolve_date(elem)
            slug = _resolve_slug(elem)
            tags = _extract_tags(elem)
            categories = _extract_categories(elem)

            # Get content
            content_el = elem.find(f"{{{CONTENT_NS}}}encoded")
            if content_el is None or content_el.text is None:
                logger.warning(
                    "Post '%s' (id=%s) missing content:encoded",
                    title,
                    post_id,
                )
                html_content = ""
            else:
                html_content = content_el.text

            # Convert HTML to Markdown
            md_body = _html_to_markdown(html_content)

            # Build front matter
            front_matter = _build_front_matter(
                title=title,
                date=date,
                url=link,
                post_id=post_id,
                post_type=post_type,
                status=status,
                slug=slug,
                tags=tags,
                categories=categories,
            )

            # Build full file content
            file_content = front_matter + "\n" + md_body + "\n"

            # Determine output filename
            date_prefix = date.strftime("%Y-%m-%d") if date else "0000-00-00"
            base_filename = f"{date_prefix}-{slug}.md"

            if base_filename in used_filenames:
                base_filename = f"{date_prefix}-{slug}-{post_id}.md"

            used_filenames.add(base_filename)
            out_path = self.out_dir / base_filename

            # Incremental check: skip if file exists and content hash matches
            if (
                self.incremental
                and not self.overwrite
                and out_path.exists()
            ):
                existing_hash = hashlib.md5(
                    out_path.read_bytes()
                ).hexdigest()
                new_hash = hashlib.md5(
                    file_content.encode("utf-8")
                ).hexdigest()
                if existing_hash == new_hash:
                    skipped += 1
                    elem.clear()
                    continue

            # Write file
            try:
                out_path.write_text(
                    file_content, encoding="utf-8", newline="\n"
                )
                exported += 1
            except OSError as e:
                raise Exception(
                    f"Cannot write to {out_path}: {e}"
                ) from e

            # Clear element to free memory
            elem.clear()

        return ExportReport(exported=exported, skipped=skipped, errors=errors)
