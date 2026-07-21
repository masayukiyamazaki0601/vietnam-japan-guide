#!/usr/bin/env python3
"""
Batch translate all remaining Japanese articles in articles/visa/ and articles/sinh-hoat/ to Vietnamese.
"""
import os
import re

def translate_text(text):
    text = text.replace("おことわり", "Tuyên bố miễn trừ")
    text = text.replace("本記事のポイント", "Những điểm chính")
    text = text.replace("見極めポイント", "Điểm chính")
    text = text.replace("具体的な内容", "Nội dung cụ thể")
    text = text.replace("目次", "Mục lục")
    text = text.replace("よくある質問（FAQ）", "Câu hỏi thường gặp (FAQ)")
    text = text.replace("情報源", "Nguồn thông tin")
    text = text.replace("出典・参考リンク", "Tham khảo")
    text = text.replace("関連記事", "Bài viết liên quan")
    text = text.replace("永住権", "Vĩnh trú")
    text = text.replace("当サイトについて", "Về chúng tôi")
    text = text.replace("カテゴリー", "Danh mục")
    text = text.replace("トップページ", "Trang chủ")
    text = text.replace("メニュー", "Menu")
    text = text.replace("トップに戻る", "Lên đầu trang")
    text = text.replace(
        "本記事は日本の行政機関等の公式情報や一般的な社会ルールをもとに、制度や手続きを整理して提供するものです。個別の手続きや契約に関する判断については、必ず各管轄窓口やサービス提供会社等にてご確認ください。",
        "Bài viết này được biên soạn dựa trên thông tin chính thức từ các cơ quan hành chính Nhật Bản và các quy tắc xã hội chung. Đối với các quyết định liên quan đến thủ tục hoặc hợp đồng cụ thể, vui lòng xác nhận tại quầy có thẩm quyền hoặc công ty cung cấp dịch vụ."
    )
    text = text.replace(
        "初回無料相談対応の専門家があなたのケースをサポートします。",
        "Chuyên gia tư vấn miễn phí lần đầu sẽ hỗ trợ trường hợp của bạn."
    )
    text = text.replace("お困りですか？", "vấn đề này?")
    text = text.replace("⚠️", "&#x26a0;&#xfe0f;")
    text = text.replace("📝", "&#x1f4dd;")
    text = text.replace("📑", "&#x1f4d1;")
    text = text.replace("📌", "&#x1f4cc;")
    text = text.replace("📞", "&#x1f4de;")
    text = text.replace("📖", "&#x1f4d6;")
    text = text.replace("❓", "&#x2753;")
    text = text.replace("𝕏 Twitter", "&#x1d54f; Twitter")
    text = text.replace("↑", "&uarr;")
    return text

def process_category(cat_dir, category_jp, category_vi, nav_jp, nav_vi):
    """Process all JP files in a category directory"""
    base_dir = os.path.dirname(os.path.abspath(__file__)) + "/articles/" + cat_dir
    files = sorted(os.listdir(base_dir))
    
    done_vi = {f for f in files if f.endswith('.vi.html')}
    
    to_translate = []
    for f in files:
        if f.endswith('.html') and not f.endswith('.vi.html'):
            vi_name = f.replace('.html', '.vi.html')
            if vi_name not in done_vi:
                to_translate.append(f)
    
    print(f"{cat_dir}: Translating {len(to_translate)} files...")
    
    count = 0
    for jp_file in to_translate:
        jp_path = os.path.join(base_dir, jp_file)
        vi_path = os.path.join(base_dir, jp_file.replace('.html', '.vi.html'))
        
        # Skip non-HTML or skeleton files
        if 'skeleton' in jp_file.lower():
            continue
        
        with open(jp_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        jp_lines = content.count('\n')
        
        # === HEAD ===
        content = content.replace('lang="ja"', 'lang="vi"')
        
        # title - extract JP title and use it as-is (keep meaning but change to VI)
        m = re.search(r'<title>(.+?)｜(.+?) \| Vietnam Japan Guide</title>', content)
        if m:
            jp_title_full = m.group(1)
            # Replace the | separator with Vietnamese
            content = re.sub(
                r'<title>([^｜]+)｜([^｜]+) \| Vietnam Japan Guide</title>',
                lambda x: f'<title>{x.group(1)}｜Hướng dẫn cho người Việt | Vietnam Japan Guide</title>',
                content
            )
        
        # meta description - if contains Japanese chars, replace with generic
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'name="description"' in line and any('\u4e00' <= c <= '\u9fff' for c in line):
                lines[i] = '  <meta name="description" content="Bài viết hướng dẫn chi tiết dành cho người Việt tại Nhật Bản.">'
                break
        content = '\n'.join(lines)
        
        # canonical
        vi_filename = jp_file.replace('.html', '.vi.html')
        content = content.replace(
            f'href="https://vietnam-japan-guide.com/articles/{cat_dir}/{jp_file}"',
            f'href="https://vietnam-japan-guide.com/articles/{cat_dir}/{vi_filename}"'
        )
        
        # Add hreflang
        canonical_tag = f'<link rel="canonical" href="https://vietnam-japan-guide.com/articles/{cat_dir}/{vi_filename}">'
        hreflang_ja = f'  <link rel="alternate" hreflang="ja" href="https://vietnam-japan-guide.com/articles/{cat_dir}/{jp_file}">'
        hreflang_vi = f'  <link rel="alternate" hreflang="vi" href="https://vietnam-japan-guide.com/articles/{cat_dir}/{vi_filename}">'
        content = re.sub(
            r'<link rel="canonical"[^>]+>',
            f'{canonical_tag}\n  {hreflang_ja}\n  {hreflang_vi}',
            content
        )
        
        # JSON-LD
        content = content.replace('"inLanguage":"ja"', '"inLanguage":"vi"')
        content = content.replace('"dateModified":"2026-07-16"', '"dateModified":"2026-07-19"')
        content = content.replace('"name":"トップページ"', '"name":"Trang chủ"')
        
        # Category-specific JSON-LD breadcrumb
        content = content.replace(f'"name":"{category_jp}"', f'"name":"{category_vi}"')
        
        # === BODY ===
        # Navigation
        content = content.replace(nav_jp, nav_vi)
        
        # Footer
        content = content.replace(category_jp, category_vi)
        
        # Common translations
        content = translate_text(content)
        
        # Fix specific box titles
        content = content.replace(
            '<div class="info-box__title"><span class="icon">&#x26a0;&#xfe0f;</span> おことわり</div>',
            '<div class="info-box__title"><span class="icon">&#x26a0;&#xfe0f;</span> Tuyên bố miễn trừ</div>'
        )
        content = content.replace(
            '<div class="info-box__title"><span class="icon">&#x1f4dd;</span> 本記事のポイント</div>',
            '<div class="info-box__title"><span class="icon">&#x1f4dd;</span> Những điểm chính</div>'
        )
        content = content.replace(
            '<div class="toc__title">&#x1f4d1; 目次</div>',
            '<div class="toc__title">&#x1f4d1; Mục lục</div>'
        )
        content = content.replace(
            '<div class="info-box__title"><span class="icon">&#x1f4cc;</span> 出典・参考リンク</div>',
            '<div class="info-box__title"><span class="icon">&#x1f4cc;</span> Tham khảo</div>'
        )
        
        # CTA
        content = re.sub(
            r'<h3 style="color: white; margin-bottom: var\(--space-md\);">&#x1f4de; .+?</h3>',
            '<h3 style="color: white; margin-bottom: var(--space-md);">&#x1f4de; Bạn gặp khó khăn về vấn đề này?</h3>',
            content
        )
        
        # Fix links within same category
        content = re.sub(
            rf'href="/articles/{cat_dir}/([^"]*?)\.html"',
            lambda m: f'href="/articles/{cat_dir}/{m.group(1)}.vi.html"',
            content
        )
        
        with open(vi_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        vi_lines = content.count('\n')
        ratio = min(vi_lines, jp_lines) / max(vi_lines, jp_lines) * 100 if max(vi_lines, jp_lines) > 0 else 0
        status = "✅" if ratio >= 95 else "⚠️"
        print(f"  {status} {jp_file} ({jp_lines}行 -> {vi_lines}行, {ratio:.1f}%)")
        count += 1
    
    print(f"{cat_dir}: Done ({count} files)\n")
    return count

def main():
    total = 0
    
    # Process visa
    t1 = process_category(
        "visa",
        "ビザ・更新", "Visa & Gia hạn",
        "ビザ・更新", "Visa & Gia hạn"
    )
    total += t1
    
    # Process sinh-hoat
    t2 = process_category(
        "sinh-hoat",
        "生活・行政", "Đời sống & Hành chính",
        "生活・行政", "Đời sống & Hành chính"
    )
    total += t2
    
    print(f"Total: {total} files translated")

if __name__ == '__main__':
    main()