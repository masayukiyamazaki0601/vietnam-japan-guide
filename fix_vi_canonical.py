#!/usr/bin/env python3
"""vi版のcanonical URLから .vi を取り除く修正スクリプト"""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
VI_DIR = BASE_DIR / "vi"

for f in sorted(VI_DIR.rglob("*.html")):
    content = f.read_text(encoding="utf-8")
    original = content

    # canonical: .vi.html を .html に修正
    content = re.sub(
        r'(<link\s+rel="canonical"\s+href="https://vietnam-japan-guide\.com/vi/[^"]+)\.vi\.html(")',
        r'\1.html\2',
        content
    )

    if content != original:
        f.write_text(content, encoding="utf-8")
        print(f"Fixed: {f.relative_to(BASE_DIR)}")