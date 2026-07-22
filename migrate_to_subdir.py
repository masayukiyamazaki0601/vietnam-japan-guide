#!/usr/bin/env python3
"""
vietnam-japan-guide: .vi.html 方式 → サブディレクトリ方式 への移行スクリプト

変更前: articles/visa/xxx.html (JP), articles/visa/xxx.vi.html (VI)
変更後: ja/articles/visa/xxx.html, vi/articles/visa/xxx.html
"""

import os
import re
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
ARTICLES_DIR = BASE_DIR / "articles"
PAGES_DIR = BASE_DIR / "pages"

def migrate_articles():
    """articles/ 配下を ja/vi に振り分け、内部リンクを書き換え"""
    for cat_dir in sorted(ARTICLES_DIR.iterdir()):
        if not cat_dir.is_dir():
            continue
        category = cat_dir.name
        print(f"\n=== Category: {category} ===")

        for f in sorted(cat_dir.iterdir()):
            if not f.is_file() or not f.name.endswith(".html"):
                continue

            # .vi.html → vi/ (リネームして .html に)
            if f.name.endswith(".vi.html"):
                new_name = f.name[:-8] + ".html"
                dest = BASE_DIR / "vi" / "articles" / category / new_name
                lang = "vi"
            else:
                dest = BASE_DIR / "ja" / "articles" / category / f.name
                lang = "ja"

            dest.parent.mkdir(parents=True, exist_ok=True)
            content = f.read_text(encoding="utf-8")

            # 内部リンク書き換え: href="articles/..." → そのまま維持 (ja/vi からの相対パス)
            # pages/ へのリンクは後で処理

            # hreflang の href を新しいパスに書き換え
            if lang == "ja":
                # ja版: .vi.html → vi/ に、自分自身 → ja/ に
                content = re.sub(
                    r'(<link\s+rel="alternate"\s+hreflang="vi"\s+href=")https://vietnam-japan-guide\.com/articles/([^"]+)\.vi\.html(")',
                    r'\1https://vietnam-japan-guide.com/vi/articles/\2.html\3',
                    content
                )
                content = re.sub(
                    r'(<link\s+rel="alternate"\s+hreflang="ja"\s+href=")https://vietnam-japan-guide\.com/articles/([^"]+)\.html(")',
                    r'\1https://vietnam-japan-guide.com/ja/articles/\2.html\3',
                    content
                )
                # canonical
                content = re.sub(
                    r'(<link\s+rel="canonical"\s+href=")https://vietnam-japan-guide\.com/articles/',
                    r'\1https://vietnam-japan-guide.com/ja/articles/',
                    content
                )
                # breadcrumb/pages/ リンク
                content = re.sub(
                    r'(href="/)pages/',
                    r'\1ja/pages/',
                    content
                )
            else:  # vi
                content = re.sub(
                    r'(<link\s+rel="alternate"\s+hreflang="vi"\s+href=")https://vietnam-japan-guide\.com/articles/([^"]+)\.vi\.html(")',
                    r'\1https://vietnam-japan-guide.com/vi/articles/\2.html\3',
                    content
                )
                content = re.sub(
                    r'(<link\s+rel="alternate"\s+hreflang="ja"\s+href=")https://vietnam-japan-guide\.com/articles/([^"]+)\.html(")',
                    r'\1https://vietnam-japan-guide.com/ja/articles/\2.html\3',
                    content
                )
                content = re.sub(
                    r'(<link\s+rel="canonical"\s+href=")https://vietnam-japan-guide\.com/articles/',
                    r'\1https://vietnam-japan-guide.com/vi/articles/',
                    content
                )
                content = re.sub(
                    r'(href="/)pages/',
                    r'\1vi/pages/',
                    content
                )

            dest.write_text(content, encoding="utf-8")
            print(f"  {lang.upper()}: {f.name} -> {dest.relative_to(BASE_DIR)}")


def migrate_pages():
    """pages/ を ja/pages/ vi/pages/ に複製・編集"""
    for f in sorted(PAGES_DIR.iterdir()):
        if not f.is_file() or not f.name.endswith(".html"):
            continue

        content = f.read_text(encoding="utf-8")

        # ja/ へコピー（pages内リンクを調整）
        ja_content = content
        ja_content = re.sub(
            r'(href="\.\./articles/)',
            r'\1',  # そのまま維持
            ja_content
        )
        # canonical 書き換え
        ja_content = re.sub(
            r'(<link\s+rel="canonical"\s+href=")https://vietnam-japan-guide\.com/pages/',
            r'\1https://vietnam-japan-guide.com/ja/pages/',
            ja_content
        )
        ja_dest = BASE_DIR / "ja" / "pages" / f.name
        ja_dest.parent.mkdir(parents=True, exist_ok=True)
        ja_dest.write_text(ja_content, encoding="utf-8")
        print(f"  JP page: {f.name} -> ja/pages/{f.name}")

        # vi/ へ（VI版pagesは新規作成：タイトル・文言をVIに）
        vi_content = content
        vi_content = re.sub(
            r'(<link\s+rel="canonical"\s+href=")https://vietnam-japan-guide\.com/pages/',
            r'\1https://vietnam-japan-guide.com/vi/pages/',
            vi_content
        )
        # pages内のhreflangなど調整
        vi_content = re.sub(
            r'(href="\.\./articles/)',
            r'\1',
            vi_content
        )
        vi_dest = BASE_DIR / "vi" / "pages" / f.name
        vi_dest.parent.mkdir(parents=True, exist_ok=True)
        vi_dest.write_text(vi_content, encoding="utf-8")
        print(f"  VI page: {f.name} -> vi/pages/{f.name}")


def create_vi_index():
    """ベトナム語版トップページ index.html を作成（日本語版をコピーして vi/ に）"""
    src = BASE_DIR / "index.html"
    if not src.exists():
        return
    content = src.read_text(encoding="utf-8")

    # canonical
    content = re.sub(
        r'(<link\s+rel="canonical"\s+href=")https://vietnam-japan-guide\.com/(")',
        r'\1https://vietnam-japan-guide.com/vi/\2',
        content
    )
    # pages/ リンクを vi/pages/ に
    content = re.sub(
        r'(href=")pages/',
        r'\1vi/pages/',
        content
    )
    # articles/ リンクを vi/articles/ に
    content = re.sub(
        r'(href=")articles/',
        r'\1vi/articles/',
        content
    )
    # lang
    content = re.sub(r'<html\s+lang="ja"', '<html lang="vi"', content)
    # title
    content = re.sub(
        r'<title>在日ベトナム人生活ガイド - Vietnam Japan Guide \| ビザ・永住権・生活情報</title>',
        '<title>Hướng dẫn cuộc sống tại Nhật cho người Việt - Vietnam Japan Guide | Visa, Vĩnh trú, Thông tin cuộc sống</title>',
        content
    )

    dest = BASE_DIR / "vi" / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")
    print(f"  VI index: index.html -> vi/index.html")


def create_ja_index():
    """日本語版トップページを ja/ にコピー"""
    src = BASE_DIR / "index.html"
    if not src.exists():
        return
    content = src.read_text(encoding="utf-8")
    # canonical
    content = re.sub(
        r'(<link\s+rel="canonical"\s+href=")https://vietnam-japan-guide\.com/(")',
        r'\1https://vietnam-japan-guide.com/ja/\2',
        content
    )
    # pages/ リンクを ja/pages/ に
    content = re.sub(
        r'(href=")pages/',
        r'\1ja/pages/',
        content
    )
    # articles/ リンクを ja/articles/ に
    content = re.sub(
        r'(href=")articles/',
        r'\1ja/articles/',
        content
    )

    dest = BASE_DIR / "ja" / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")
    print(f"  JA index: index.html -> ja/index.html")


def copy_static_assets():
    """CSS/JS/画像などの静的ファイルを ja/ vi/ にコピー"""
    for asset_dir in ["css", "js", "assets"]:
        src = BASE_DIR / asset_dir
        if not src.exists():
            continue
        for lang in ["ja", "vi"]:
            dest = BASE_DIR / lang / asset_dir
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
            print(f"  Copied {asset_dir}/ -> {lang}/{asset_dir}/")


def update_sitemap():
    """sitemap.xml を更新（サブディレクトリ対応）"""
    # 新しいsitemapではja/とvi/の両方を含める
    sitemap_path = BASE_DIR / "sitemap.xml"
    if not sitemap_path.exists():
        return

    content = sitemap_path.read_text(encoding="utf-8")

    # 既存の記事URLをja/に書き換え
    content = re.sub(
        r'https://vietnam-japan-guide\.com/articles/',
        r'https://vietnam-japan-guide.com/ja/articles/',
        content
    )
    content = re.sub(
        r'https://vietnam-japan-guide\.com/pages/',
        r'https://vietnam-japan-guide.com/ja/pages/',
        content
    )

    sitemap_path.write_text(content, encoding="utf-8")
    print("  sitemap.xml updated")


def main():
    print("=" * 60)
    print("Migrating vietnam-japan-guide to subdirectory structure")
    print("=" * 60)

    # 1. 記事ファイルの振り分け
    migrate_articles()

    # 2. ページファイルの複製
    migrate_pages()

    # 3. トップページの複製
    create_ja_index()
    create_vi_index()

    # 4. 静的ファイルのコピー
    copy_static_assets()

    # 5. sitemap更新
    update_sitemap()

    print("\n" + "=" * 60)
    print("Migration complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Check the ja/ and vi/ directories")
    print("  2. Update _redirects or Netlify config for language detection")
    print("  3. Deploy to Netlify or GitHub Pages")


if __name__ == "__main__":
    main()