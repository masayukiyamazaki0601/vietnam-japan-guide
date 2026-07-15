#!/usr/bin/env python3
"""
SEO一括改善スクリプト（1回だけ実行）
1. リンク切れを修正
2. スケルトン記事に noindex 追加
3. sitemap.xml を全記事網羅で再生成
"""
import os
import re
import glob
from datetime import date

BASE_DIR = os.path.dirname(__file__)
ARTICLES_DIR = os.path.join(BASE_DIR, "articles")
PAGES_DIR = os.path.join(BASE_DIR, "pages")

# ============================================================
# 1. リンク切れ修正マッピング
#    ベトナム語ファイル名 → 実際の日本語ファイル名
# ============================================================
BROKEN_LINK_FIXES = {
    # Vinh Tru
    "/articles/vinh-tru/ly-do-ho-so-vinh-tru-bi-tu-choi.html":
        "/articles/vinh-tru/eijyu-fukyoka-sai-shinsei.html",
    "/articles/vinh-tru/nguoi-bao-lanh-vinh-tru.html":
        "/articles/vinh-tru/minamoto-hoshonin-joken.html",
    "/articles/vinh-tru/thoi-gian-xu-ly-ho-so-vinh-tru.html":
        "/articles/vinh-tru/nenshuu-shinsa-kijun.html",
    "/articles/vinh-tru/thu-nhap-yeu-cau-xin-vinh-tru.html":
        "/articles/vinh-tru/nenshuu-shinsa-kijun.html",
    # Visa
    "/articles/visa/chuyen-doi-cong-ty-visa-ky-su.html":
        "/articles/visa/gijinkoku-koushin.html",
    "/articles/visa/tokutei-ginou-chuyen-ky-su.html":
        "/articles/visa/tokutei-1go-2go-sai.html",
}


def fix_broken_links():
    """全HTMLファイルのリンク切れを修正"""
    count = 0
    html_files = glob.glob(f"{ARTICLES_DIR}/**/*.html", recursive=True) + \
                 glob.glob(f"{PAGES_DIR}/*.html") + \
                 [os.path.join(BASE_DIR, "index.html")]

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        for old_link, new_link in BROKEN_LINK_FIXES.items():
            content = content.replace(old_link, new_link)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            relpath = os.path.relpath(filepath, BASE_DIR)
            print(f"  ✅ {relpath}")
            count += 1

    print(f"📊 リンク切れ修正: {count}ファイル\n")


# ============================================================
# 2. スケルトン記事に noindex 追加
# ============================================================
SKELETON_KEYWORDS = ["skeleton", "執筆中です", "このセクションは執筆中です"]


def add_noindex_to_skeletons():
    """執筆中のスケルトン記事に <meta name="robots" content="noindex"> を追加"""
    count = 0
    html_files = glob.glob(f"{ARTICLES_DIR}/**/*.html", recursive=True)

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # スケルトンかどうか判定
        is_skeleton = any(kw in content for kw in SKELETON_KEYWORDS)
        if not is_skeleton:
            continue

        # 既に noindex があればスキップ
        if 'noindex' in content:
            continue

        # <meta name="robots" content="index, follow"> を noindex に変更
        content = content.replace(
            '<meta name="robots" content="index, follow">',
            '<meta name="robots" content="noindex, follow">'
        )
        # なければ robots の前に追加
        if 'noindex' not in content:
            content = content.replace(
                '<link rel="canonical"',
                '<meta name="robots" content="noindex, follow">\n  <link rel="canonical"'
            )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        relpath = os.path.relpath(filepath, BASE_DIR)
        print(f"  ✅ {relpath}")
        count += 1

    print(f"📊 noindex追加: {count}ファイル\n")


# ============================================================
# 3. sitemap.xml を自動生成
# ============================================================
def generate_sitemap():
    """全記事を網羅した sitemap.xml を生成"""
    today = date.today().isoformat()
    base_url = "https://vietnam-japan-guide.com"

    urls = []

    # トップページ
    urls.append(("", today, "weekly", "1.00"))

    # カテゴリーページ
    category_pages = [
        ("pages/vinh-tru.html", today, "weekly", "0.80"),
        ("pages/visa.html", today, "weekly", "0.80"),
        ("pages/sinh-hoat.html", today, "weekly", "0.80"),
        ("pages/cong-viec.html", today, "weekly", "0.80"),
        ("pages/chuyen-gia.html", today, "weekly", "0.80"),
    ]
    urls.extend(category_pages)

    # 記事一覧（カテゴリ別に分類）
    categories = ["vinh-tru", "visa", "sinh-hoat", "cong-viec", "chuyen-gia"]
    for cat in categories:
        cat_dir = os.path.join(ARTICLES_DIR, cat)
        if not os.path.isdir(cat_dir):
            continue
        for f in sorted(os.listdir(cat_dir)):
            if f.endswith(".html"):
                path = f"articles/{cat}/{f}"
                # スケルトンは優先度低め
                filepath = os.path.join(cat_dir, f)
                with open(filepath, 'r', encoding='utf-8') as fh:
                    content = fh.read()
                if "執筆中" in content or "skeleton" in f:
                    priority = "0.30"
                    changefreq = "monthly"
                else:
                    priority = "0.70"
                    changefreq = "monthly"
                urls.append((path, today, changefreq, priority))

    # XML生成
    xml_parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, lastmod, changefreq, priority in urls:
        loc = f"{base_url}/{path}" if path else base_url
        xml_parts.append("  <url>")
        xml_parts.append(f"    <loc>{loc}</loc>")
        xml_parts.append(f"    <lastmod>{lastmod}</lastmod>")
        xml_parts.append(f"    <changefreq>{changefreq}</changefreq>")
        xml_parts.append(f"    <priority>{priority}</priority>")
        xml_parts.append("  </url>")
    xml_parts.append("</urlset>")

    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_parts) + '\n')

    # 件数表示
    file_count = len(urls)
    article_count = sum(1 for p, _, _, _ in urls if p.startswith("articles/"))
    skeleton_count = sum(1 for p, _, _, pri in urls if pri == "0.30")
    print(f"📊 sitemap.xml 再生成完了: 全{file_count}URL")
    print(f"   - カテゴリーページ: 5")
    print(f"   - 通常記事: {article_count - skeleton_count}")
    print(f"   - スケルトン記事(noindex): {skeleton_count}")


def main():
    print("=" * 50)
    print("🔧 SEO一括改善スクリプト")
    print("=" * 50)

    print("\n--- 1. リンク切れ修正 ---")
    fix_broken_links()

    print("\n--- 2. スケルトン記事に noindex 追加 ---")
    add_noindex_to_skeletons()

    print("\n--- 3. sitemap.xml 再生成 ---")
    generate_sitemap()

    print("\n" + "=" * 50)
    print("🎉 完了！")
    print("=" * 50)


if __name__ == '__main__':
    main()