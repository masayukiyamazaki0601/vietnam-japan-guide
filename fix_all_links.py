#!/usr/bin/env python3
"""全カテゴリページの記事リンクを相対パスに修正"""
import os, glob, re

BASE = os.path.dirname(os.path.abspath(__file__))

# カテゴリページと相対パスの関係（pages/xxx.htmlから見た相対パス）
CATEGORIES = {
    "visa": ("pages/visa.html", "../articles/visa/"),
    "vinh-tru": ("pages/vinh-tru.html", "../articles/vinh-tru/"),
    "sinh-hoat": ("pages/sinh-hoat.html", "../articles/sinh-hoat/"),
    "cong-viec": ("pages/cong-viec.html", "../articles/cong-viec/"),
    "jobs": ("pages/jobs.html", "../articles/jobs/"),
    "telecom": ("pages/telecom.html", "../articles/telecom/"),
    "estate": ("pages/estate.html", "../articles/estate/"),
}

for cat, (page_file, rel_prefix) in CATEGORIES.items():
    filepath = os.path.join(BASE, page_file)
    if not os.path.exists(filepath):
        print(f"SKIP: {filepath} not found")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 絶対パス `/articles/visa/xxx.html` → 相対パス `../articles/visa/xxx.html`
    updated = re.sub(
        r'href="/articles/' + cat + r'/([^"]+)"',
        r'href="' + rel_prefix + r'\1"',
        content
    )
    
    if updated != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated)
        # Count changes
        changes = len(re.findall(r'href="/articles/' + cat + r'/', content)) - len(re.findall(r'href="/articles/' + cat + r'/', updated))
        print(f"FIXED: {page_file} ({cat} links)")
    else:
        print(f"OK: {page_file}")

# Also fix index.html
idx_path = os.path.join(BASE, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    content = f.read()

# index.htmlはルートにあるので /articles/xxx はそのまま絶対パスでOK
# ただし /pages/xxx も絶対パスでOK（ルートからの相対）
print(f"OK: index.html (root, absolute paths are correct)")

print("Done! All links fixed.")