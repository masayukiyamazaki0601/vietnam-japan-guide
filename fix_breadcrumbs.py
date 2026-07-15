#!/usr/bin/env python3
"""Fix breadcrumb bug in skeleton HTML files."""
import glob, re

for f in glob.glob('articles/*/*.html') + glob.glob('articles/sinh-hoat/*.html') + glob.glob('articles/cong-viec/*.html') + glob.glob('articles/visa/*.html'):
    with open(f, 'r') as fh:
        content = fh.read()
    original = content
    # Fix: ['Text', '/path.html'] -> Text
    content = re.sub(
        r"<li class=\"breadcrumb__item breadcrumb__item--current\">\['(.+?)',\s*'(.+?)'\]</li>",
        r'<li class="breadcrumb__item breadcrumb__item--current">\1</li>',
        content
    )
    # Fix any empty current breadcrumbs
    if content != original:
        with open(f, 'w') as fh:
            fh.write(content)
        print(f'Fixed: {f}')

import subprocess
result = subprocess.run(['grep', '-r', "breadcrumb__item--current'>\\[", 'articles/', '--include=*.html'], capture_output=True, text=True)
count = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
print(f"\nRemaining broken: {count}")