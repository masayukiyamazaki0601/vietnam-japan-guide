#!/usr/bin/env python3
"""
Batch translate remaining Japanese articles in articles/cong-viec/ to Vietnamese.
Line-by-line replacement preserving exact HTML structure.
"""
import os
import re

ARTICLES_DIR = os.path.dirname(os.path.abspath(__file__)) + "/articles/cong-viec"

# Full title translations for all articles
TITLE_MAP = {
    "扶養控除で節税する方法": "Cách giảm thuế với khấu trừ người phụ thuộc",
    "外国人が日本で資産運用する際のリスク": "Rủi ro khi người nước ngoài quản lý tài sản tại Nhật",
    "銀行送金の比較：銀行・インターネット送金サービス": "So sánh chuyển tiền ngân hàng: Ngân hàng & dịch vụ chuyển tiền online",
    "外国人の住宅ローンの組み方": "Cách vay mua nhà cho người nước ngoài tại Nhật",
    "確定申告が必要なケースとは": "Các trường hợp cần khai thuế thu nhập (Kakutei Shinkoku)",
    "給与明細書の見方と控除の基本": "Cách đọc phiếu lương và cơ bản về các khoản khấu trừ",
    "ふるさと納税で節税する方法": "Cách giảm thuế với Furusato Nozei (quyên góp địa phương)",
    "海外送金の基礎知識": "Kiến thức cơ bản về chuyển tiền quốc tế",
    "年金の基礎知識：日本の年金制度": "Kiến thức cơ bản về Nenkin: Hệ thống lương hưu Nhật Bản",
    "投資の基礎知識": "Kiến thức cơ bản về đầu tư",
    "税金の基礎知識と計算方法": "Kiến thức cơ bản về thuế và cách tính",
    "年金脱退一時金が今後の在留に与える影響": "Ảnh hưởng của Nenkin Dattai Ichijikin đến lưu trú",
    "労働契約書のポイントと確認方法": "Điểm quan trọng trong hợp đồng lao động và cách xác nhận",
    "資本金・準備金の基礎知識": "Kiến thức cơ bản về vốn điều lệ và dự trữ",
    "相続税の基礎知識": "Kiến thức cơ bản về thuế thừa kế",
    "退職後の住民税と手続き": "Thuế cư trú và thủ tục sau khi nghỉ việc",
    "通信・ネット銀行の選び方": "Cách chọn ngân hàng trực tuyến và viễn thông",
}

DESC_MAP = {
    "扶養控除で節税する方法": "Giải thích cách giảm thuế bằng khấu trừ người phụ thuộc. Điều kiện, số tiền khấu trừ, thủ tục đăng ký tại nơi làm việc.",
    "外国人が日本で資産運用する際のリスク": "Giải thích rủi ro khi người nước ngoài quản lý tài sản tại Nhật. Rủi ro tỷ giá, thuế, pháp lý, lừa đảo.",
    "銀行送金の比較：銀行・インターネット送金サービス": "So sánh chuyển tiền ngân hàng và dịch vụ chuyển tiền online. Phí, tỷ giá, thời gian, an toàn.",
    "外国人の住宅ローンの組み方": "Giải thích cách vay mua nhà cho người nước ngoài. Điều kiện, tư cách lưu trú, lãi suất, giấy tờ.",
    "確定申告が必要なケースとは": "Giải thích các trường hợp cần khai thuế thu nhập. Điều kiện, thời hạn, thủ tục, nộp thuế.",
    "給与明細書の見方と控除の基本": "Giải thích cách đọc phiếu lương và các khoản khấu trừ. Bảo hiểm, thuế, phụ cấp.",
    "ふるさと納税で節税する方法": "Giải thích cách giảm thuế với Furusato Nozei. Cơ chế, giới hạn, thủ tục, lợi ích.",
    "海外送金の基礎知識": "Kiến thức cơ bản về chuyển tiền quốc tế. Phương thức, phí, tỷ giá, quy định pháp lý.",
    "年金の基礎知識：日本の年金制度": "Kiến thức cơ bản về hệ thống lương hưu Nhật Bản. Loại, đóng góp, quyền lợi, thủ tục.",
    "投資の基礎知識": "Kiến thức cơ bản về đầu tư tại Nhật. Cổ phiếu, trái phiếu, quỹ tương hỗ, tài khoản NISA.",
    "税金の基礎知識と計算方法": "Kiến thức cơ bản về thuế Nhật Bản và cách tính. Thuế thu nhập, cư trú, khai thuế.",
    "年金脱退一時金が今後の在留に与える影響": "Giải thích ảnh hưởng của Nenkin Dattai Ichijikin đến lưu trú. Điều kiện, thủ tục, ảnh hưởng visa.",
    "労働契約書のポイントと確認方法": "Giải thích điểm quan trọng trong hợp đồng lao động. Lương, giờ làm, bảo hiểm, nghỉ phép.",
    "資本金・準備金の基礎知識": "Kiến thức cơ bản về vốn điều lệ và dự trữ cho doanh nghiệp tại Nhật.",
    "相続税の基礎知識": "Kiến thức cơ bản về thuế thừa kế Nhật Bản. Đối tượng, thuế suất, khấu trừ, thủ tục.",
    "退職後の住民税と手続き": "Giải thích thuế cư trú và thủ tục sau khi nghỉ việc. Phương thức nộp, thay đổi, lưu ý.",
    "通信・ネット銀行の選び方": "Hướng dẫn chọn ngân hàng trực tuyến và dịch vụ viễn thông. Phí, lãi suất, tiện ích.",
}

def translate_text(text):
    """Translate common Japanese text to Vietnamese"""
    text = text.replace("おことわり", "Tuyên bố miễn trừ")
    text = text.replace("本記事のポイント", "Những điểm chính")
    text = text.replace("見極めポイント", "Điểm chính")
    text = text.replace("具体的な内容", "Nội dung cụ thể")
    text = text.replace("目次", "Mục lục")
    text = text.replace("よくある質問（FAQ）", "Câu hỏi thường gặp (FAQ)")
    text = text.replace("情報源", "Nguồn thông tin")
    text = text.replace("出典・参考リンク", "Tham khảo")
    text = text.replace("関連記事", "Bài viết liên quan")
    text = text.replace("仕事・金融", "Công việc & Tài chính")
    text = text.replace("生活・行政", "Đời sống & Hành chính")
    text = text.replace("ビザ・更新", "Visa & Gia hạn")
    text = text.replace("永住・帰化", "Vĩnh trú & Nhập tịch")
    text = text.replace("永住権", "Vĩnh trú")
    text = text.replace("当サイトについて", "Về chúng tôi")
    text = text.replace("カテゴリー", "Danh mục")
    text = text.replace("トップページ", "Trang chủ")
    text = text.replace("メニュー", "Menu")
    text = text.replace("トップに戻る", "Lên đầu trang")
    text = text.replace("ビザ", "Visa")
    text = text.replace("生活", "Đời sống")
    text = text.replace("仕事", "Công việc")
    
    # Disclaimer
    text = text.replace(
        "本記事は日本の行政機関等の公式情報や一般的な社会ルールをもとに、制度や手続きを整理して提供するものです。個別の手続きや契約に関する判断については、必ず各管轄窓口やサービス提供会社等にてご確認ください。",
        "Bài viết này được biên soạn dựa trên thông tin chính thức từ các cơ quan hành chính Nhật Bản và các quy tắc xã hội chung. Đối với các quyết định liên quan đến thủ tục hoặc hợp đồng cụ thể, vui lòng xác nhận tại quầy có thẩm quyền hoặc công ty cung cấp dịch vụ."
    )
    text = text.replace(
        "初回無料相談対応の専門家があなたのケースをサポートします。",
        "Chuyên gia tư vấn miễn phí lần đầu sẽ hỗ trợ trường hợp của bạn."
    )
    text = text.replace("お困りですか？", "vấn đề này?")
    
    # Icons to HTML entities
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

def has_vi_article(filename):
    """Check if Vietnamese version already exists"""
    vi_path = os.path.join(ARTICLES_DIR, filename.replace('.html', '.vi.html'))
    return os.path.exists(vi_path)

def main():
    # Get all JP files that don't have VI version
    files_to_do = []
    for f in sorted(os.listdir(ARTICLES_DIR)):
        if f.endswith('.html') and not f.endswith('.vi.html'):
            if not has_vi_article(f):
                files_to_do.append(f)
    
    total = len(files_to_do)
    print(f"Processing {total} files...\n")
    
    for jp_file in files_to_do:
        jp_path = os.path.join(ARTICLES_DIR, jp_file)
        vi_path = os.path.join(ARTICLES_DIR, jp_file.replace('.html', '.vi.html'))
        
        with open(jp_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        jp_lines = content.count('\n')
        
        # === HEAD CHANGES ===
        # lang
        content = content.replace('lang="ja"', 'lang="vi"')
        
        # title
        m = re.search(r'<title>(.+?)｜(.+?) \| Vietnam Japan Guide</title>', content)
        if m:
            jp_title = m.group(1)
            vi_title = TITLE_MAP.get(jp_title, jp_title)
            content = content.replace(
                f'<title>{m.group(0)[7:-8]}',
                f'<title>{vi_title}｜Hướng dẫn cho người Việt | Vietnam Japan Guide</title>'
            )
            # Fix the title properly
            content = re.sub(
                r'<title>(.+?)｜(.+?) \| Vietnam Japan Guide</title>',
                f'<title>{vi_title}｜Hướng dẫn cho người Việt | Vietnam Japan Guide</title>',
                content
            )
        
        # meta description
        m = re.search(r'content="(.+?)"', content.split('\n')[6])
        title_match = re.search(r'<title>(.+?)｜', content)
        if title_match:
            jp_t = title_match.group(1)
            vi_desc = DESC_MAP.get(jp_t, "")
            if vi_desc:
                old_desc_line = [l for l in content.split('\n') if 'name="description"' in l]
                if old_desc_line:
                    content = content.replace(
                        old_desc_line[0],
                        f'  <meta name="description" content="{vi_desc}">'
                    )
        
        # canonical & hreflang
        vi_filename = jp_file.replace('.html', '.vi.html')
        content = content.replace(
            f'href="https://vietnam-japan-guide.com/articles/cong-viec/{jp_file}"',
            f'href="https://vietnam-japan-guide.com/articles/cong-viec/{vi_filename}"'
        )
        
        # Add hreflang after canonical
        canonical_tag = f'<link rel="canonical" href="https://vietnam-japan-guide.com/articles/cong-viec/{vi_filename}">'
        hreflang_ja = f'  <link rel="alternate" hreflang="ja" href="https://vietnam-japan-guide.com/articles/cong-viec/{jp_file}">'
        hreflang_vi = f'  <link rel="alternate" hreflang="vi" href="https://vietnam-japan-guide.com/articles/cong-viec/{vi_filename}">'
        content = re.sub(
            r'<link rel="canonical"[^>]+>',
            f'{canonical_tag}\n  {hreflang_ja}\n  {hreflang_vi}',
            content
        )
        
        # JSON-LD updates
        content = content.replace('"inLanguage":"ja"', '"inLanguage":"vi"')
        content = content.replace('"dateModified":"2026-07-16"', '"dateModified":"2026-07-19"')
        
        # Remove FAQPage JSON-LD if present (complex translation)
        content = re.sub(r'<script type="application/ld\+json">\s*{"@context":"https://schema.org","@type":"FAQPage".*?</script>\s*', '', content, flags=re.DOTALL)
        
        # === BODY CHANGES ===
        content = translate_text(content)
        
        # Fix info-box titles after icon replacement
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
        
        # CTA heading
        content = re.sub(
            r'<h3 style="color: white; margin-bottom: var\(--space-md\);">&#x1f4de; .+?</h3>',
            '<h3 style="color: white; margin-bottom: var(--space-md);">&#x1f4de; Bạn gặp khó khăn về vấn đề này?</h3>',
            content
        )
        
        # Article h1
        h1_match = re.search(r'<h1>(.+?)</h1>', content)
        if h1_match:
            jp_h1 = h1_match.group(1)
            vi_h1 = TITLE_MAP.get(jp_h1, jp_h1)
            content = content.replace(f'<h1>{jp_h1}</h1>', f'<h1>{vi_h1}</h1>')
        
        # Breadcrumb current
        bread_match = re.search(r'breadcrumb__item--current">(.+?)</li>', content)
        if bread_match:
            jp_bread = bread_match.group(1)
            vi_bread = TITLE_MAP.get(jp_bread, jp_bread)
            content = content.replace(
                f'breadcrumb__item--current">{jp_bread}</li>',
                f'breadcrumb__item--current">{vi_bread}</li>'
            )
        
        # JSON-LD headline
        headline_match = re.search(r'"headline":"(.+?)"', content)
        if headline_match:
            jp_head = headline_match.group(1)
            vi_head = TITLE_MAP.get(jp_head, jp_head)
            if vi_head != jp_head:
                content = content.replace(f'"headline":"{jp_head}"', f'"headline":"{vi_head}"')
        
        # JSON-LD breadcrumb name at position 3
        for m in re.finditer(r'"position":3,"name":"([^"]+)"', content):
            jp_name = m.group(1)
            vi_name = TITLE_MAP.get(jp_name, jp_name)
            if vi_name != jp_name:
                content = content.replace(f'"position":3,"name":"{jp_name}"', f'"position":3,"name":"{vi_name}"')
        
        # JSON-LD breadcrumb full match
        content = content.replace(
            '"name":"トップページ"', '"name":"Trang chủ"'
        )
        content = content.replace(
            '"name":"仕事・金融"', '"name":"Công việc & Tài chính"'
        )
        
        # Write VI file
        with open(vi_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        vi_lines = content.count('\n')
        ratio = min(vi_lines, jp_lines) / max(vi_lines, jp_lines) * 100 if max(vi_lines, jp_lines) > 0 else 0
        status = "✅" if ratio >= 95 else "⚠️"
        print(f"{status} {jp_file} ({jp_lines}行) -> {vi_filename} ({vi_lines}行, {ratio:.1f}%)")

if __name__ == '__main__':
    main()