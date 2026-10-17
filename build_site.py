#!/usr/bin/env python3
"""Build the static web app (for GitHub Pages or any static host).

Combines the validated question bank, the self-marking exam template and the
app page into a single self-contained `index.html` in the output folder.

    python build_site.py              # writes site/index.html
    python build_site.py -o docs      # e.g. to publish from a /docs folder
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from question_bank import KSBS, load_bank

HERE = Path(__file__).resolve().parent
APP_TEMPLATE = HERE / "web" / "app_template.html"
EXAM_TEMPLATE = HERE / "exam_template.html"


def _js(value) -> str:
    """JSON for embedding inside a <script> tag."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def build(out_dir: Path) -> Path:
    bank = load_bank()  # validates every question
    html = APP_TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "/*__BANK__*/[]": _js(bank),
        "/*__AREAS__*/{}": _js(KSBS),
        "/*__TEMPLATE__*/\"\"": _js(EXAM_TEMPLATE.read_text(encoding="utf-8")),
        "/*__BUILT__*/\"\"": _js(datetime.now(timezone.utc).strftime("%d %b %Y")),
    }
    for token, value in replacements.items():
        if token not in html:
            raise SystemExit(f"Placeholder {token} missing from {APP_TEMPLATE}")
        html = html.replace(token, value)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")  # serve files as-is on GitHub Pages
    (out_dir / "bank.json").write_text(json.dumps(bank, indent=1, ensure_ascii=False), encoding="utf-8")
    return out_dir / "index.html"


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-o", "--out-dir", type=Path, default=HERE / "site", help="output folder (default ./site)")
    args = p.parse_args(argv)
    path = build(args.out_dir)
    print(f"Built {path} ({path.stat().st_size // 1024} KB, {len(load_bank())} questions)")


if __name__ == "__main__":
    main()
