"""CLI entry point for WordPress WXR to Markdown exporter.

Usage:
    python -m jm_tools.wordpress_wxr --wxr path/to/export.xml
"""

import argparse
from pathlib import Path

from .exporter import WordpressWxrExporter, _CLI_DEFAULT_OUT_DIR


def main():
    parser = argparse.ArgumentParser(
        description="Convert WordPress WXR XML export to Markdown files."
    )
    parser.add_argument(
        "--wxr",
        type=Path,
        required=True,
        help="Path to WXR XML export file",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory (default: data/writing/wordpress)",
    )
    parser.add_argument(
        "--include",
        type=str,
        default=None,
        help="Comma-separated post types to include (default: post)",
    )
    parser.add_argument(
        "--status",
        type=str,
        default=None,
        help="Comma-separated statuses to include (default: publish)",
    )
    parser.add_argument(
        "--no-incremental",
        action="store_true",
        help="Disable incremental mode (always write)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files",
    )
    parser.add_argument(
        "--max-posts",
        type=int,
        default=None,
        help="Maximum number of posts to export",
    )

    args = parser.parse_args()

    post_types = set(args.include.split(",")) if args.include else None
    statuses = set(args.status.split(",")) if args.status else None

    # CLI provides a default out_dir; the library API requires it explicitly
    out_dir = args.out_dir if args.out_dir is not None else _CLI_DEFAULT_OUT_DIR

    kwargs = {
        "wxr_path": args.wxr,
        "out_dir": out_dir,
    }
    if post_types is not None:
        kwargs["post_types"] = post_types
    if statuses is not None:
        kwargs["statuses"] = statuses
    if args.no_incremental:
        kwargs["incremental"] = False
    if args.overwrite:
        kwargs["overwrite"] = True
    if args.max_posts is not None:
        kwargs["max_posts"] = args.max_posts

    exporter = WordpressWxrExporter(**kwargs)
    report = exporter.run()

    print(f"Export complete: {report.exported} exported, {report.skipped} skipped, {len(report.errors)} errors")
    if report.errors:
        for err in report.errors:
            print(f"  ERROR: {err}")


if __name__ == "__main__":
    main()
