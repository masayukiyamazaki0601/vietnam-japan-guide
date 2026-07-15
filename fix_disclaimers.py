#!/usr/bin/env python3
"""
全記事に免責事項を追加するスクリプト（改良版）
1. 記事冒頭（h1直後）に⚠️注意書きボックスを追加
2. フッターに免責文を追加
"""
import os
import re

ARTICLES_DIR = os.path.join(os.path.dirname(__file__), "articles")
PAGES_DIR = os.path.join(os.path.dirname(__file__), "pages")

DISCLAIMER_TOP = '''    <div class="info-box info-box--warning">
      <div class="info-box__title">⚠️ おことわり</div>
      <p>この記事は、出入国在留管理庁などの公的機関が公開している公式情報をもとに解説しています。当サイトは法律専門家ではなく、正確な判断が必要な場合は必ず出入国在留管理庁または行政書士・弁護士などの専門家にご確認ください。</p>
    </div>'''

DISCLAIMER_FOOTER_LINE = '<p>※ 当サイトは法律専門家ではありません。記載内容は参考情報であり、正確な判断については出入国在留管理庁または行政書士にご確認ください。</p>'


def fix_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    modified = False
    
    # 1. フッターに免責を追加（既存の免責がある場合はスキップ）
    if '当サイトは法律専門家ではありません' not in content:
        # フッターの閉じタグ前に免責を挿入
        # <div class="footer__bottom"><p>© ...</p></div></footer> または
        # <div class="footer__bottom"><p>© ...</p></div>
        #   </footer>
        pattern_footer = r'(<div class="footer__bottom">\s*<p>[^<]*?</p>\s*</div>\s*</footer>)'
        replacement_footer = f'<div class="footer__bottom">{DISCLAIMER_FOOTER_LINE}<p>\\1</p></div></footer>'
        
        # Replace the content INSIDE footer__bottom
        # Pattern: find footer__bottom, capture the existing <p>, replace with disclaimer + original
        pattern_footer2 = r'(<div class="footer__bottom">)(\s*<p>)([^<]*?)(</p>\s*</div>\s*</footer>)'
        if re.search(pattern_footer2, content, re.DOTALL):
            content = re.sub(
                pattern_footer2,
                rf'\1{DISCLAIMER_FOOTER_LINE}\2\3\4',
                content
            )
            modified = True
    
    # 2. 記事冒頭に注意書きを追加（h1直後。既存のwarning系info-boxがあればスキップ）
    if 'おことわり' not in content and 'info-box--warning' not in content:
        # h1の後に挿入（最初の改行の後）
        pattern_h1 = r'(</h1>\s*\n)'
        if re.search(pattern_h1, content):
            content = re.sub(pattern_h1, r'\1' + DISCLAIMER_TOP + '\n', content, count=1)
            modified = True
    
    if modified and content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    count = 0
    total = 0
    # 記事ディレクトリを走査
    for root, dirs, files in os.walk(ARTICLES_DIR):
        for f in files:
            if f.endswith('.html') and f != 'index.html':
                filepath = os.path.join(root, f)
                total += 1
                if fix_article(filepath):
                    print(f"  ✅ {os.path.relpath(filepath, os.path.dirname(__file__))}")
                    count += 1
    
    # pages/ も同様に処理
    for f in os.listdir(PAGES_DIR):
        if f.endswith('.html'):
            filepath = os.path.join(PAGES_DIR, f)
            total += 1
            if fix_article(filepath):
                print(f"  ✅ pages/{f}")
                count += 1
    
    print(f"\n📊 全{total}ファイル中、{count}ファイルを修正しました。")
    print(f"📊 {total - count}ファイルは既に適用済みまたはスキップされました。")


if __name__ == '__main__':
    main()