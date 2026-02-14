"""
Comprehensive unit tests for jm_tools.wordpress_wxr.WordpressWxrExporter.

Uses small inline WXR XML fixtures — no external files needed.
"""

import hashlib
import os
import tempfile
import textwrap
import unittest
from pathlib import Path

from jm_tools.wordpress_wxr import WordpressWxrExporter, ExportError
from jm_tools.wordpress_wxr.exporter import ExportReport


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

WP_NS = "http://wordpress.org/export/1.2/"
CONTENT_NS = "http://purl.org/rss/1.0/modules/content/"
DC_NS = "http://purl.org/dc/elements/1.1/"
EXCERPT_NS = "http://wordpress.org/export/1.2/excerpt/"

WXR_HEADER = textwrap.dedent(f"""\
    <?xml version="1.0" encoding="UTF-8"?>
    <rss version="2.0"
         xmlns:content="{CONTENT_NS}"
         xmlns:wp="{WP_NS}"
         xmlns:dc="{DC_NS}"
         xmlns:excerpt="{EXCERPT_NS}">
    <channel>
""")

WXR_FOOTER = textwrap.dedent("""\
    </channel>
    </rss>
""")


def _make_item(
    title="Test Post",
    post_id="100",
    post_date_gmt="",
    pub_date="",
    post_date="",
    post_name="test-post",
    post_type="post",
    status="publish",
    link="https://example.com/test-post",
    content="<p>Hello world</p>",
    tags=None,
    categories=None,
):
    """Build a single <item> element with the given fields."""
    tags = tags or []
    categories = categories or []

    tag_xml = "\n".join(
        f'        <category domain="post_tag" nicename="{t}"><![CDATA[{t}]]></category>'
        for t in tags
    )
    cat_xml = "\n".join(
        f'        <category domain="category" nicename="{c}"><![CDATA[{c}]]></category>'
        for c in categories
    )

    date_gmt_el = (
        f"<wp:post_date_gmt>{post_date_gmt}</wp:post_date_gmt>"
        if post_date_gmt
        else "<wp:post_date_gmt></wp:post_date_gmt>"
    )
    pub_date_el = f"<pubDate>{pub_date}</pubDate>" if pub_date else "<pubDate></pubDate>"
    post_date_el = (
        f"<wp:post_date>{post_date}</wp:post_date>"
        if post_date
        else "<wp:post_date></wp:post_date>"
    )

    return textwrap.dedent(f"""\
        <item>
            <title>{title}</title>
            <link>{link}</link>
            {pub_date_el}
            <dc:creator>admin</dc:creator>
            <content:encoded><![CDATA[{content}]]></content:encoded>
            <wp:post_id>{post_id}</wp:post_id>
            <wp:post_name>{post_name}</wp:post_name>
            <wp:post_type>{post_type}</wp:post_type>
            <wp:status>{status}</wp:status>
            {date_gmt_el}
            {post_date_el}
            {tag_xml}
            {cat_xml}
        </item>
    """)


def _build_wxr(*items):
    """Wrap one or more <item> blocks in a complete WXR document."""
    return WXR_HEADER + "\n".join(items) + WXR_FOOTER


def _write_wxr(tmp_dir, xml_text):
    """Write *xml_text* to a temp WXR file and return its Path."""
    wxr_path = Path(tmp_dir) / "export.xml"
    wxr_path.write_text(xml_text, encoding="utf-8")
    return wxr_path


def _run_export(tmp_dir, xml_text, **kwargs):
    """Convenience: write WXR, run exporter, return (report, out_dir Path)."""
    wxr_path = _write_wxr(tmp_dir, xml_text)
    out_dir = Path(tmp_dir) / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir, **kwargs)
    report = exporter.run()
    return report, out_dir


def _md_files(out_dir):
    """Return sorted list of .md filenames in *out_dir*."""
    return sorted(f.name for f in Path(out_dir).glob("*.md"))


def _read_md(out_dir, filename):
    """Read a markdown file and return its text."""
    return (Path(out_dir) / filename).read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# 1. Filename collision handling
# ---------------------------------------------------------------------------


class TestFilenameCollision(unittest.TestCase):
    """Two posts with the same date+slug must produce distinct filenames."""

    def test_collision_appends_post_id(self):
        item_a = _make_item(
            title="Dup",
            post_id="10",
            post_date_gmt="2024-01-15 10:00:00",
            post_name="hello",
        )
        item_b = _make_item(
            title="Dup",
            post_id="20",
            post_date_gmt="2024-01-15 10:00:00",
            post_name="hello",
        )
        xml = _build_wxr(item_a, item_b)

        with tempfile.TemporaryDirectory() as tmp:
            report, out_dir = _run_export(tmp, xml)

            files = _md_files(out_dir)
            self.assertEqual(len(files), 2)
            self.assertEqual(report.exported, 2)

            # One file should be the plain name; the other has the post_id suffix.
            self.assertIn("2024-01-15-hello.md", files)
            collision_file = [f for f in files if f != "2024-01-15-hello.md"][0]
            # Must contain one of the post IDs
            self.assertTrue(
                collision_file.endswith("-10.md") or collision_file.endswith("-20.md"),
                f"Expected post-id suffix, got {collision_file}",
            )

    def test_no_collision_no_suffix(self):
        """When slugs differ, no post-id suffix is appended."""
        item_a = _make_item(
            post_id="10",
            post_date_gmt="2024-01-15 10:00:00",
            post_name="alpha",
        )
        item_b = _make_item(
            post_id="20",
            post_date_gmt="2024-01-15 10:00:00",
            post_name="beta",
        )
        xml = _build_wxr(item_a, item_b)

        with tempfile.TemporaryDirectory() as tmp:
            report, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(files, ["2024-01-15-alpha.md", "2024-01-15-beta.md"])


# ---------------------------------------------------------------------------
# 2. Date resolution
# ---------------------------------------------------------------------------


class TestDateResolution(unittest.TestCase):
    """Verify fallback order: post_date_gmt → pubDate → post_date."""

    def test_prefers_post_date_gmt(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-06-01 12:00:00",
            pub_date="Sat, 01 Jan 2022 00:00:00 +0000",
            post_date="2020-01-01 00:00:00",
            post_name="gmt-wins",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(len(files), 1)
            self.assertTrue(
                files[0].startswith("2024-06-01"),
                f"Expected date from post_date_gmt, got {files[0]}",
            )

    def test_falls_back_to_pubdate(self):
        item = _make_item(
            post_id="2",
            post_date_gmt="",
            pub_date="Sun, 15 Sep 2023 08:30:00 +0000",
            post_date="2020-01-01 00:00:00",
            post_name="pubdate-wins",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(len(files), 1)
            self.assertTrue(
                files[0].startswith("2023-09-15"),
                f"Expected date from pubDate, got {files[0]}",
            )

    def test_falls_back_to_post_date(self):
        item = _make_item(
            post_id="3",
            post_date_gmt="",
            pub_date="",
            post_date="2021-12-25 18:00:00",
            post_name="postdate-wins",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(len(files), 1)
            self.assertTrue(
                files[0].startswith("2021-12-25"),
                f"Expected date from post_date, got {files[0]}",
            )

    def test_unparseable_date_falls_through(self):
        """An invalid post_date_gmt should be skipped in favour of pubDate."""
        item = _make_item(
            post_id="4",
            post_date_gmt="not-a-date",
            pub_date="Mon, 03 Mar 2025 00:00:00 +0000",
            post_date="2019-07-07 00:00:00",
            post_name="bad-gmt",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(len(files), 1)
            self.assertTrue(
                files[0].startswith("2025-03-03"),
                f"Expected fallback to pubDate, got {files[0]}",
            )


# ---------------------------------------------------------------------------
# 3. Slug resolution
# ---------------------------------------------------------------------------


class TestSlugResolution(unittest.TestCase):
    """wp:post_name is preferred; slugified title is the fallback."""

    def test_uses_post_name_when_present(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="custom-slug",
            title="My Fancy Title!",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(files, ["2024-01-01-custom-slug.md"])

    def test_falls_back_to_slugified_title(self):
        item = _make_item(
            post_id="2",
            post_date_gmt="2024-02-02 00:00:00",
            post_name="",
            title="Hello, World! It's Me",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(len(files), 1)
            slug_part = files[0].replace("2024-02-02-", "").replace(".md", "")
            # Should be lowercase, hyphen-separated, non-alphanum stripped
            self.assertRegex(slug_part, r"^[a-z0-9-]+$")
            self.assertIn("hello", slug_part)
            self.assertIn("world", slug_part)

    def test_slugified_title_strips_special_characters(self):
        item = _make_item(
            post_id="3",
            post_date_gmt="2024-03-03 00:00:00",
            post_name="",
            title="C++ & Rust: A Comparison!!! @2024",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(len(files), 1)
            slug_part = files[0].replace("2024-03-03-", "").replace(".md", "")
            self.assertRegex(slug_part, r"^[a-z0-9-]+$")
            self.assertNotIn("!", slug_part)
            self.assertNotIn("@", slug_part)
            self.assertNotIn("&", slug_part)
            self.assertNotIn(":", slug_part)


# ---------------------------------------------------------------------------
# 4. Front-matter emission
# ---------------------------------------------------------------------------


class TestFrontMatter(unittest.TestCase):
    """Output contains expected YAML keys in stable order."""

    def _export_single(self, **item_kwargs):
        """Export a single item and return the markdown text."""
        item = _make_item(**item_kwargs)
        xml = _build_wxr(item)
        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(len(files), 1)
            return _read_md(out_dir, files[0])

    def test_front_matter_delimiters(self):
        text = self._export_single(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="fm-test",
        )
        self.assertTrue(text.startswith("---\n"), "File must start with YAML delimiter")
        # There must be a closing delimiter after the opening one
        parts = text.split("---")
        self.assertGreaterEqual(
            len(parts), 3, "Expected opening and closing --- delimiters"
        )

    def test_front_matter_contains_required_keys(self):
        text = self._export_single(
            post_id="42",
            post_date_gmt="2024-05-10 09:00:00",
            post_name="required-keys",
            title="Required Keys Post",
            link="https://example.com/required-keys",
            post_type="post",
            status="publish",
            tags=["python", "testing"],
            categories=["tech"],
        )
        # Extract front matter between the --- delimiters
        fm = text.split("---")[1]

        self.assertIn("title:", fm)
        self.assertIn("date:", fm)
        self.assertIn("url:", fm)
        self.assertIn("source: wordpress", fm)
        self.assertIn("wp:", fm)
        self.assertIn("id:", fm)
        self.assertIn("post_type:", fm)
        self.assertIn("status:", fm)
        self.assertIn("slug:", fm)
        self.assertIn("tags:", fm)
        self.assertIn("categories:", fm)

    def test_front_matter_title_value(self):
        text = self._export_single(
            post_id="5",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="title-val",
            title="My Awesome Post",
        )
        fm = text.split("---")[1]
        self.assertIn("My Awesome Post", fm)

    def test_front_matter_date_is_iso8601(self):
        text = self._export_single(
            post_id="6",
            post_date_gmt="2024-07-20 14:30:00",
            post_name="iso-date",
        )
        fm = text.split("---")[1]
        # ISO 8601: should contain YYYY-MM-DD and a time component
        self.assertRegex(fm, r"date:.*2024-07-20")

    def test_front_matter_url(self):
        text = self._export_single(
            post_id="7",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="url-test",
            link="https://myblog.com/url-test",
        )
        fm = text.split("---")[1]
        self.assertIn("https://myblog.com/url-test", fm)

    def test_front_matter_source_is_wordpress(self):
        text = self._export_single(
            post_id="8",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="src-test",
        )
        fm = text.split("---")[1]
        self.assertIn("wordpress", fm)

    def test_front_matter_wp_block(self):
        text = self._export_single(
            post_id="99",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="wp-block",
            post_type="post",
            status="publish",
        )
        fm = text.split("---")[1]
        self.assertIn("99", fm)  # id
        self.assertIn("post", fm)  # post_type
        self.assertIn("publish", fm)  # status
        self.assertIn("wp-block", fm)  # slug

    def test_front_matter_tags_and_categories(self):
        text = self._export_single(
            post_id="10",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="tags-cats",
            tags=["alpha", "beta"],
            categories=["news", "updates"],
        )
        fm = text.split("---")[1]
        self.assertIn("alpha", fm)
        self.assertIn("beta", fm)
        self.assertIn("news", fm)
        self.assertIn("updates", fm)

    def test_front_matter_empty_tags_and_categories(self):
        text = self._export_single(
            post_id="11",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="no-tags",
            tags=[],
            categories=[],
        )
        fm = text.split("---")[1]
        self.assertIn("tags:", fm)
        self.assertIn("categories:", fm)

    def test_front_matter_key_order_is_stable(self):
        """Keys should appear in a deterministic order across runs."""
        text1 = self._export_single(
            post_id="12",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="order-a",
            tags=["x"],
            categories=["y"],
        )
        text2 = self._export_single(
            post_id="12",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="order-a",
            tags=["x"],
            categories=["y"],
        )
        fm1 = text1.split("---")[1]
        fm2 = text2.split("---")[1]
        self.assertEqual(fm1, fm2, "Front matter key order must be deterministic")


# ---------------------------------------------------------------------------
# 5. Incremental skip
# ---------------------------------------------------------------------------


class TestIncrementalSkip(unittest.TestCase):
    """Unchanged content produces no write on second run."""

    def test_second_run_skips_unchanged(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="incr-test",
            content="<p>Same content</p>",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = _write_wxr(tmp, xml)
            out_dir = Path(tmp) / "output"
            out_dir.mkdir()

            exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)

            # First run — file should be written
            r1 = exporter.run()
            self.assertEqual(r1.exported, 1)
            self.assertEqual(r1.skipped, 0)

            files = _md_files(out_dir)
            self.assertEqual(len(files), 1)
            mtime1 = os.path.getmtime(out_dir / files[0])

            # Second run — file should be skipped (incremental=True by default)
            r2 = exporter.run()
            self.assertEqual(r2.exported, 0)
            self.assertEqual(r2.skipped, 1)

    def test_incremental_false_always_writes(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="no-incr",
            content="<p>Same content</p>",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = _write_wxr(tmp, xml)
            out_dir = Path(tmp) / "output"
            out_dir.mkdir()

            exporter = WordpressWxrExporter(
                wxr_path=wxr_path, out_dir=out_dir, incremental=False
            )

            r1 = exporter.run()
            self.assertEqual(r1.exported, 1)

            r2 = exporter.run()
            # With incremental=False, it re-exports (not skipped)
            self.assertEqual(r2.exported, 1)
            self.assertEqual(r2.skipped, 0)

    def test_overwrite_true_always_writes(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="overwrite-test",
            content="<p>Same content</p>",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = _write_wxr(tmp, xml)
            out_dir = Path(tmp) / "output"
            out_dir.mkdir()

            exporter = WordpressWxrExporter(
                wxr_path=wxr_path, out_dir=out_dir, overwrite=True
            )

            r1 = exporter.run()
            self.assertEqual(r1.exported, 1)

            r2 = exporter.run()
            self.assertEqual(r2.exported, 1)
            self.assertEqual(r2.skipped, 0)

    def test_changed_content_is_re_exported(self):
        """If the WXR content changes, incremental mode should re-export."""
        item_v1 = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="changing",
            content="<p>Version 1</p>",
        )
        item_v2 = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="changing",
            content="<p>Version 2 — updated</p>",
        )

        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp) / "output"
            out_dir.mkdir()

            # First run with v1
            wxr_v1 = _write_wxr(tmp, _build_wxr(item_v1))
            r1 = WordpressWxrExporter(wxr_path=wxr_v1, out_dir=out_dir).run()
            self.assertEqual(r1.exported, 1)
            content_v1 = _read_md(out_dir, _md_files(out_dir)[0])

            # Second run with v2
            wxr_v2 = _write_wxr(tmp, _build_wxr(item_v2))
            r2 = WordpressWxrExporter(wxr_path=wxr_v2, out_dir=out_dir).run()
            self.assertEqual(r2.exported, 1)
            self.assertEqual(r2.skipped, 0)
            content_v2 = _read_md(out_dir, _md_files(out_dir)[0])

            self.assertNotEqual(content_v1, content_v2)
            self.assertIn("Version 2", content_v2)


# ---------------------------------------------------------------------------
# 6. Post-type and status filtering
# ---------------------------------------------------------------------------


class TestFiltering(unittest.TestCase):
    """Only items matching post_types and statuses are exported."""

    def test_filters_by_post_type(self):
        post = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="a-post",
            post_type="post",
        )
        page = _make_item(
            post_id="2",
            post_date_gmt="2024-01-02 00:00:00",
            post_name="a-page",
            post_type="page",
        )
        nav = _make_item(
            post_id="3",
            post_date_gmt="2024-01-03 00:00:00",
            post_name="a-nav",
            post_type="nav_menu_item",
        )
        xml = _build_wxr(post, page, nav)

        with tempfile.TemporaryDirectory() as tmp:
            report, out_dir = _run_export(tmp, xml, post_types={"post"})
            self.assertEqual(report.exported, 1)
            files = _md_files(out_dir)
            self.assertEqual(files, ["2024-01-01-a-post.md"])

    def test_filters_by_status(self):
        published = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="pub",
            status="publish",
        )
        draft = _make_item(
            post_id="2",
            post_date_gmt="2024-01-02 00:00:00",
            post_name="dra",
            status="draft",
        )
        xml = _build_wxr(published, draft)

        with tempfile.TemporaryDirectory() as tmp:
            report, out_dir = _run_export(tmp, xml, statuses={"publish"})
            self.assertEqual(report.exported, 1)
            files = _md_files(out_dir)
            self.assertEqual(files, ["2024-01-01-pub.md"])

    def test_multiple_post_types(self):
        post = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="a-post",
            post_type="post",
        )
        page = _make_item(
            post_id="2",
            post_date_gmt="2024-01-02 00:00:00",
            post_name="a-page",
            post_type="page",
        )
        xml = _build_wxr(post, page)

        with tempfile.TemporaryDirectory() as tmp:
            report, out_dir = _run_export(tmp, xml, post_types={"post", "page"})
            self.assertEqual(report.exported, 2)

    def test_multiple_statuses(self):
        published = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="pub",
            status="publish",
        )
        draft = _make_item(
            post_id="2",
            post_date_gmt="2024-01-02 00:00:00",
            post_name="dra",
            status="draft",
        )
        xml = _build_wxr(published, draft)

        with tempfile.TemporaryDirectory() as tmp:
            report, out_dir = _run_export(
                tmp, xml, statuses={"publish", "draft"}
            )
            self.assertEqual(report.exported, 2)

    def test_no_matching_posts_exports_nothing(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="irrelevant",
            post_type="attachment",
            status="inherit",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            report, out_dir = _run_export(tmp, xml)
            self.assertEqual(report.exported, 0)
            self.assertEqual(len(_md_files(out_dir)), 0)


# ---------------------------------------------------------------------------
# 7. max_posts cap
# ---------------------------------------------------------------------------


class TestMaxPosts(unittest.TestCase):
    """The max_posts parameter caps the number of exported posts."""

    def test_max_posts_limits_output(self):
        items = [
            _make_item(
                post_id=str(i),
                post_date_gmt=f"2024-01-{i:02d} 00:00:00",
                post_name=f"post-{i}",
            )
            for i in range(1, 6)
        ]
        xml = _build_wxr(*items)

        with tempfile.TemporaryDirectory() as tmp:
            report, out_dir = _run_export(tmp, xml, max_posts=3)
            self.assertEqual(report.exported, 3)
            self.assertEqual(len(_md_files(out_dir)), 3)

    def test_max_posts_none_exports_all(self):
        items = [
            _make_item(
                post_id=str(i),
                post_date_gmt=f"2024-01-{i:02d} 00:00:00",
                post_name=f"post-{i}",
            )
            for i in range(1, 4)
        ]
        xml = _build_wxr(*items)

        with tempfile.TemporaryDirectory() as tmp:
            report, out_dir = _run_export(tmp, xml, max_posts=None)
            self.assertEqual(report.exported, 3)


# ---------------------------------------------------------------------------
# 8. Markdown body conversion
# ---------------------------------------------------------------------------


class TestMarkdownBody(unittest.TestCase):
    """HTML from content:encoded is converted to Markdown correctly."""

    def _get_body(self, html_content):
        """Export a single post with given HTML and return the body (after front matter)."""
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="body-test",
            content=html_content,
        )
        xml = _build_wxr(item)
        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            text = _read_md(out_dir, _md_files(out_dir)[0])
            # Body is everything after the second ---
            parts = text.split("---", 2)
            return parts[2].strip() if len(parts) >= 3 else ""

    def test_paragraph_conversion(self):
        body = self._get_body("<p>Hello world</p>")
        self.assertIn("Hello world", body)

    def test_heading_preservation(self):
        body = self._get_body("<h2>My Heading</h2><p>Text</p>")
        self.assertIn("My Heading", body)
        # Markdown heading syntax: ## or equivalent
        self.assertRegex(body, r"#{1,6}\s*My Heading")

    def test_link_preservation(self):
        body = self._get_body('<p>Visit <a href="https://example.com">here</a></p>')
        self.assertIn("[here]", body)
        self.assertIn("https://example.com", body)

    def test_list_preservation(self):
        body = self._get_body("<ul><li>One</li><li>Two</li></ul>")
        self.assertIn("One", body)
        self.assertIn("Two", body)

    def test_blockquote_preservation(self):
        body = self._get_body("<blockquote><p>Quoted text</p></blockquote>")
        self.assertIn("Quoted text", body)
        # Markdown blockquote syntax
        self.assertIn(">", body)

    def test_code_block_preservation(self):
        body = self._get_body("<pre><code>print('hello')</code></pre>")
        self.assertIn("print('hello')", body)

    def test_inline_style_stripped(self):
        body = self._get_body(
            '<p style="color: red; font-size: 14px;">Styled text</p>'
        )
        self.assertIn("Styled text", body)
        self.assertNotIn("color: red", body)
        self.assertNotIn("style=", body)

    def test_inline_class_stripped(self):
        body = self._get_body('<p class="wp-block-paragraph">Class text</p>')
        self.assertIn("Class text", body)
        self.assertNotIn("class=", body)
        self.assertNotIn("wp-block", body)


# ---------------------------------------------------------------------------
# 9. Output file encoding
# ---------------------------------------------------------------------------


class TestOutputEncoding(unittest.TestCase):
    """Files should be UTF-8 with \\n newlines."""

    def test_utf8_encoding(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="utf8-test",
            title="Ünïcödé Pöst",
            content="<p>Héllo wörld — «quotes»</p>",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            # Read as bytes to check encoding
            raw = (Path(out_dir) / files[0]).read_bytes()
            text = raw.decode("utf-8")
            self.assertIn("Ünïcödé Pöst", text)
            self.assertIn("Héllo wörld", text)

    def test_newlines_are_unix(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="newline-test",
            content="<p>Line one</p><p>Line two</p>",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            raw = (Path(out_dir) / files[0]).read_bytes()
            self.assertNotIn(b"\r\n", raw, "File should use \\n, not \\r\\n")
            self.assertIn(b"\n", raw)


# ---------------------------------------------------------------------------
# 10. Error handling
# ---------------------------------------------------------------------------


class TestErrorHandling(unittest.TestCase):
    """Fatal and warning conditions are handled correctly."""

    def test_invalid_xml_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = Path(tmp) / "bad.xml"
            wxr_path.write_text("<<<NOT XML>>>", encoding="utf-8")
            out_dir = Path(tmp) / "output"
            out_dir.mkdir()

            exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)
            with self.assertRaises(ExportError):
                exporter.run()

    def test_unwritable_out_dir_collects_errors(self):
        """Write errors are collected in report.errors, not raised."""
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="perm-test",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = _write_wxr(tmp, xml)
            out_dir = Path(tmp) / "readonly"
            out_dir.mkdir()

            try:
                exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)
                # Make dir read-only after mkdir so exporter can't write files
                os.chmod(out_dir, 0o444)
                report = exporter.run()
                # Write error should be collected, not raised
                self.assertGreater(len(report.errors), 0)
                self.assertEqual(report.exported, 0)
            finally:
                os.chmod(out_dir, 0o755)  # restore for cleanup

    def test_missing_content_encoded_is_warning_not_fatal(self):
        """A post missing content:encoded should warn but not crash."""
        # Build an item without content:encoded
        item_xml = textwrap.dedent(f"""\
            <item>
                <title>No Content</title>
                <link>https://example.com/no-content</link>
                <pubDate></pubDate>
                <wp:post_id>1</wp:post_id>
                <wp:post_name>no-content</wp:post_name>
                <wp:post_type>post</wp:post_type>
                <wp:status>publish</wp:status>
                <wp:post_date_gmt>2024-01-01 00:00:00</wp:post_date_gmt>
                <wp:post_date></wp:post_date>
            </item>
        """)
        xml = _build_wxr(item_xml)

        with tempfile.TemporaryDirectory() as tmp:
            # Should not raise
            report, out_dir = _run_export(tmp, xml)
            # May have an error in the report or the post may be exported with empty body
            # Either way it should NOT crash


# ---------------------------------------------------------------------------
# 11. ExportReport dataclass
# ---------------------------------------------------------------------------


class TestExportReport(unittest.TestCase):
    """ExportReport has expected fields."""

    def test_report_fields(self):
        report = ExportReport(exported=5, skipped=2, errors=["some error"])
        self.assertEqual(report.exported, 5)
        self.assertEqual(report.skipped, 2)
        self.assertEqual(report.errors, ["some error"])

    def test_report_empty_errors(self):
        report = ExportReport(exported=0, skipped=0, errors=[])
        self.assertEqual(report.errors, [])

    def test_report_from_export(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="report-test",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            report, _ = _run_export(tmp, xml)
            self.assertIsInstance(report, ExportReport)
            self.assertIsInstance(report.exported, int)
            self.assertIsInstance(report.skipped, int)
            self.assertIsInstance(report.errors, list)


# ---------------------------------------------------------------------------
# 12. Constructor defaults
# ---------------------------------------------------------------------------


class TestConstructorDefaults(unittest.TestCase):
    """Verify default parameter values."""

    def test_wxr_path_is_required(self):
        with self.assertRaises(TypeError):
            WordpressWxrExporter()

    def test_out_dir_is_required(self):
        """Library API requires an explicit out_dir."""
        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = Path(tmp) / "dummy.xml"
            wxr_path.write_text("<rss></rss>", encoding="utf-8")
            with self.assertRaises(ValueError):
                WordpressWxrExporter(wxr_path=wxr_path)

    def test_default_post_types(self):
        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = Path(tmp) / "dummy.xml"
            wxr_path.write_text("<rss></rss>", encoding="utf-8")
            out_dir = Path(tmp) / "output"
            exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)
            self.assertEqual(exporter.post_types, {"post"})

    def test_default_statuses(self):
        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = Path(tmp) / "dummy.xml"
            wxr_path.write_text("<rss></rss>", encoding="utf-8")
            out_dir = Path(tmp) / "output"
            exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)
            self.assertEqual(exporter.statuses, {"publish"})

    def test_default_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = Path(tmp) / "dummy.xml"
            wxr_path.write_text("<rss></rss>", encoding="utf-8")
            out_dir = Path(tmp) / "output"
            exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)
            self.assertFalse(exporter.overwrite)

    def test_default_incremental(self):
        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = Path(tmp) / "dummy.xml"
            wxr_path.write_text("<rss></rss>", encoding="utf-8")
            out_dir = Path(tmp) / "output"
            exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)
            self.assertTrue(exporter.incremental)

    def test_default_max_posts(self):
        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = Path(tmp) / "dummy.xml"
            wxr_path.write_text("<rss></rss>", encoding="utf-8")
            out_dir = Path(tmp) / "output"
            exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)
            self.assertIsNone(exporter.max_posts)


# ---------------------------------------------------------------------------
# 13. Output file path format
# ---------------------------------------------------------------------------


class TestOutputFilePath(unittest.TestCase):
    """Output files follow the YYYY-MM-DD-slug.md pattern."""

    def test_filename_format(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-11-05 00:00:00",
            post_name="my-great-post",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            _, out_dir = _run_export(tmp, xml)
            files = _md_files(out_dir)
            self.assertEqual(files, ["2024-11-05-my-great-post.md"])

    def test_output_dir_is_created(self):
        """If out_dir doesn't exist, it should be created."""
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="dir-test",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = _write_wxr(tmp, xml)
            out_dir = Path(tmp) / "nested" / "deep" / "output"
            exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)
            report = exporter.run()
            self.assertEqual(report.exported, 1)
            self.assertTrue(out_dir.exists())


# ---------------------------------------------------------------------------
# 14. No side effects outside out_dir
# ---------------------------------------------------------------------------


class TestNoSideEffects(unittest.TestCase):
    """The exporter must not create files outside out_dir."""

    def test_only_writes_to_out_dir(self):
        item = _make_item(
            post_id="1",
            post_date_gmt="2024-01-01 00:00:00",
            post_name="side-effect",
        )
        xml = _build_wxr(item)

        with tempfile.TemporaryDirectory() as tmp:
            wxr_path = _write_wxr(tmp, xml)
            out_dir = Path(tmp) / "output"
            out_dir.mkdir()

            # Snapshot of tmp dir before (excluding the wxr file and output dir)
            before = set(Path(tmp).rglob("*"))

            exporter = WordpressWxrExporter(wxr_path=wxr_path, out_dir=out_dir)
            exporter.run()

            after = set(Path(tmp).rglob("*"))
            new_files = after - before

            # All new files should be under out_dir
            for f in new_files:
                self.assertTrue(
                    str(f).startswith(str(out_dir)),
                    f"File {f} created outside out_dir",
                )


# ---------------------------------------------------------------------------
# 15. Import / public API
# ---------------------------------------------------------------------------


class TestPublicAPI(unittest.TestCase):
    """WordpressWxrExporter is importable from jm_tools.wordpress_wxr."""

    def test_importable_from_package(self):
        from jm_tools.wordpress_wxr import WordpressWxrExporter as Cls

        self.assertTrue(callable(Cls))

    def test_export_report_importable(self):
        from jm_tools.wordpress_wxr.exporter import ExportReport as Cls

        self.assertTrue(callable(Cls))


if __name__ == "__main__":
    unittest.main()
