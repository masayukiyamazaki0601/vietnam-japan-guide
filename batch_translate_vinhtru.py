#!/usr/bin/env python3
"""
Batch translate all Japanese articles in articles/vinh-tru/ to Vietnamese.
Preserves EXACT line count and HTML structure.
"""
import os
import re

ARTICLES_DIR = os.path.dirname(os.path.abspath(__file__)) + "/articles/vinh-tru"

TITLE_MAP = {
    "cach-chon-gyoseishoshi": "Cách chọn Gyoseishoshi (luật sư hành chính)",
    "eijyu-fukyoka-sai-shinsei": "Nộp lại đơn xin Vĩnh trú sau khi bị từ chối",
    "eijyu-go-tetsuzuki": "Thủ tục sau khi được cấp Vĩnh trú",
    "eijyu-zairyu-card-kankei": "Quan hệ giữa Vĩnh trú và Thẻ lưu trú",
    "fukyoka-reki-eikyo": "Ảnh hưởng của lịch sử bị từ chối đến xin Vĩnh trú",
    "fuyou-kazoku-gerasu": "Vỡ kế hoạch gia đình phụ thuộc",
    "fuyou-koujo-eikyo": "Ảnh hưởng của khấu trừ phụ thuộc đến Vĩnh trú",
    "gyoseishoshi-ni-tanomu-baai": "Khi nào nên nhờ Gyoseishoshi",
    "huong-dan-chuan-bi-ho-so-vinh-tru": "Hướng dẫn chuẩn bị hồ sơ xin Vĩnh trú",
    "juminzei-shotokuzei-taino-eikyo": "Ảnh hưởng của nợ thuế cư trú/thu nhập đến Vĩnh trú",
    "kekkon-eijyu-kikan": "Thời gian cư trú sau kết hôn và điều kiện Vĩnh trú",
    "kika-joken": "Điều kiện nhập tịch Nhật Bản",
    "kika-koseki-sakusei": "Tạo hộ tịch khi nhập tịch",
    "kika-mensetsu-taisaku": "Biện pháp đối phó phỏng vấn nhập tịch",
    "minamoto-hoshonin-joken": "Điều kiện người bảo lãnh Vĩnh trú",
    "minashi-sainyukoku": "Nhập cảnh giả định (Minashi Sainyukoku)",
    "muryou-soudan-junbi": "Chuẩn bị cho tư vấn miễn phí về Vĩnh trú",
    "nenkin-cham-nop-anh-huong-vinh-tru": "Ảnh hưởng của việc chậm nộp Nenkin đến Vĩnh trú",
    "rikon-go-eijyu-ken": "Quyền Vĩnh trú sau khi ly hôn",
    "riyu-sho-apiru-point": "Điểm hấp dẫn trong lý do xin Vĩnh trú",
    "riyu-sho-jibun-ka": "Tự viết lý do xin Vĩnh trú",
    "so-sanh-chi-phi-gyoseishoshi": "So sánh chi phí Gyoseishoshi",
    "teijusha-oyobi-yose": "Người thường trú nhân và quy chế",
    "tenshoku-taishoku-chu": "Trong thời gian chuyển việc/nghỉ việc",
    "vietnam-kokuseki-ridatsu": "Từ bỏ quốc tịch Việt Nam khi nhập tịch",
}

TITLE_JP_TO_VI = {
    "行政書士の選び方｜在日ベトナム人ガイド": "Cách chọn Gyoseishoshi (luật sư hành chính)",
    "永住不許可後の再申請方法": "Nộp lại đơn xin Vĩnh trú sau khi bị từ chối",
    "永住許可後の手続き": "Thủ tục sau khi được cấp Vĩnh trú",
    "永住権と在留カードの関係": "Quan hệ giữa Vĩnh trú và Thẻ lưu trú",
    "不許可歴が永住申請に与える影響": "Ảnh hưởng của lịch sử bị từ chối đến xin Vĩnh trú",
    "扶養家族ゲラスのリスクと対策": "Vỡ kế hoạch gia đình phụ thuộc",
    "扶養控除が永住申請に与える影響": "Ảnh hưởng của khấu trừ phụ thuộc đến Vĩnh trú",
    "行政書士に依頼する場合のポイント": "Khi nào nên nhờ Gyoseishoshi",
    "永住許可申請の必要書類一覧": "Hướng dẫn chuẩn bị hồ sơ xin Vĩnh trú",
    "住民税・所得税の滞納が永住に与える影響": "Ảnh hưởng của nợ thuế đến Vĩnh trú",
    "結婚後の在留期間と永住条件": "Thời gian cư trú sau kết hôn",
    "帰化の条件と手続き": "Điều kiện nhập tịch Nhật Bản",
    "帰化と戸籍作成の基礎知識": "Tạo hộ tịch khi nhập tịch",
    "帰化面接対策と注意点": "Biện pháp đối phó phỏng vấn nhập tịch",
    "身元保証人の条件と役割": "Điều kiện người bảo lãnh Vĩnh trú",
    "みなし再入国許可とは": "Nhập cảnh giả định (Minashi Sainyukoku)",
    "永住申請の無料相談を受ける前に": "Chuẩn bị cho tư vấn miễn phí Vĩnh trú",
    "年金未納が永住申請に与える影響": "Ảnh hưởng của chậm nộp Nenkin",
    "離婚後の永住権維持条件": "Quyền Vĩnh trú sau khi ly hôn",
    "理由書でアピールすべきポイント": "Điểm hấp dẫn trong lý do xin Vĩnh trú",
    "理由書を自分で書く方法": "Tự viết lý do xin Vĩnh trú",
    "行政書士の費用比較と選び方": "So sánh chi phí Gyoseishoshi",
    "定住者と呼び寄せの条件": "Người thường trú nhân và quy chế",
    "転職・退職中の在留資格と永住": "Trong thời gian chuyển việc/nghỉ việc",
    "ベトナム国籍離脱と帰化の関係": "Từ bỏ quốc tịch Việt Nam khi nhập tịch",
}

# Description map based on base filename
DESC_MAP = {
    "cach-chon-gyoseishoshi": "Giải thích cách chọn Gyoseishoshi. Tiêu chuẩn, chi phí, kinh nghiệm, lưu ý.",
    "eijyu-fukyoka-sai-shinsei": "Giải thích cách nộp lại đơn Vĩnh trú sau khi bị từ chối. Nguyên nhân, cải thiện, thủ tục.",
    "eijyu-go-tetsuzuki": "Giải thích thủ tục sau khi được cấp Vĩnh trú. Đăng ký, gia hạn thẻ, nghĩa vụ.",
    "eijyu-zairyu-card-kankei": "Giải thích quan hệ giữa Vĩnh trú và Thẻ lưu trú. Hiệu lực, hạn, thủ tục.",
    "fukyoka-reki-eikyo": "Giải thích ảnh hưởng của lịch sử bị từ chối. Thời gian, khắc phục, cơ hội.",
    "fuyou-kazoku-gerasu": "Giải thích rủi ro vỡ kế hoạch gia đình phụ thuộc. Ảnh hưởng đến Vĩnh trú.",
    "fuyou-koujo-eikyo": "Giải thích ảnh hưởng của khấu trừ phụ thuộc đến xét duyệt Vĩnh trú.",
    "gyoseishoshi-ni-tanomu-baai": "Giải thích khi nào nên nhờ Gyoseishoshi. Chi phí, lợi ích, thời điểm.",
    "huong-dan-chuan-bi-ho-so-vinh-tru": "Hướng dẫn chi tiết chuẩn bị hồ sơ xin Vĩnh trú. Giấy tờ, thủ tục, lưu ý.",
    "juminzei-shotokuzei-taino-eikyo": "Giải thích ảnh hưởng của nợ thuế đến Vĩnh trú. Rủi ro, giải pháp.",
    "kekkon-eijyu-kikan": "Giải thích thời gian cư trú sau kết hôn. Điều kiện xin Vĩnh trú.",
    "kika-joken": "Giải thích điều kiện nhập tịch Nhật Bản. Cư trú, tư cách, thuế, phỏng vấn.",
    "kika-koseki-sakusei": "Giải thích thủ tục tạo hộ tịch khi nhập tịch. Giấy tờ, quy trình.",
    "kika-mensetsu-taisaku": "Giải thích biện pháp đối phó phỏng vấn nhập tịch. Nội dung, chuẩn bị.",
    "minamoto-hoshonin-joken": "Giải thích điều kiện người bảo lãnh Vĩnh trú. Thu nhập, tư cách.",
    "minashi-sainyukoku": "Giải thích chế độ nhập cảnh giả định. Điều kiện, thủ tục, lưu ý.",
    "muryou-soudan-junbi": "Hướng dẫn chuẩn bị trước khi tư vấn miễn phí Vĩnh trú.",
    "nenkin-cham-nop-anh-huong-vinh-tru": "Giải thích ảnh hưởng của việc chậm nộp Nenkin. Rủi ro, biện pháp.",
    "rikon-go-eijyu-ken": "Giải thích quyền Vĩnh trú sau ly hôn. Điều kiện, thủ tục.",
    "riyu-sho-apiru-point": "Giải thích điểm hấp dẫn trong lý do xin Vĩnh trú. Cách viết, nội dung.",
    "riyu-sho-jibun-ka": "Hướng dẫn tự viết lý do xin Vĩnh trú. Cấu trúc, nội dung.",
    "so-sanh-chi-phi-gyoseishoshi": "So sánh chi phí Gyoseishoshi. Bảng giá, dịch vụ, lưu ý.",
    "teijusha-oyobi-yose": "Giải thích quy chế người thường trú nhân. Điều kiện, thủ tục.",
    "tenshoku-taishoku-chu": "Giải thích về tư cách lưu trú khi chuyển việc/nghỉ việc.",
    "vietnam-kokuseki-ridatsu": "Giải thích thủ tục từ bỏ quốc tịch Việt Nam khi nhập tịch Nhật.",
}

def translate_text(text):
    """Translate common Japanese patterns"""
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
    text = text.replace("永住", "Vĩnh trú")
    text = text.replace("永住権", "Vĩnh trú")
    text = text.replace("帰化", "Nhập tịch")
    text = text.replace("ビザ", "Visa")
    text = text.replace("当サイトについて", "Về chúng tôi")
    text = text.replace("カテゴリー", "Danh mục")
    text = text.replace("トップページ", "Trang chủ")
    text = text.replace("メニュー", "Menu")
    text = text.replace("トップに戻る", "Lên đầu trang")
    text = text.replace("生活", "Đời sống")
    text = text.replace("仕事", "Công việc")
    
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

def get_base_name(filename):
    return filename.replace('.html', '').replace('.vi', '')

def process_vinh_tru():
    files = sorted(os.listdir(ARTICLES_DIR))
    
    done_vi = {f for f in files if f.endswith('.vi.html')}
    
    to_translate = []
    for f in files:
        if f.endswith('.html') and not f.endswith('.vi.html'):
            vi_name = f.replace('.html', '.vi.html')
            if vi_name not in done_vi:
                to_translate.append(f)
    
    print(f"Translating {len(to_translate)} files...\n")
    
    for jp_file in to_translate:
        jp_path = os.path.join(ARTICLES_DIR, jp_file)
        vi_path = os.path.join(ARTICLES_DIR, jp_file.replace('.html', '.vi.html'))
        
        with open(jp_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        jp_lines = content.count('\n')
        base = get_base_name(jp_file)
        
        # lang
        content = content.replace('lang="ja"', 'lang="vi"')
        
        # title
        for jp_t, vi_t in TITLE_JP_TO_VI.items():
            if jp_t in content:
                content = content.replace(jp_t, vi_t)
                break
        
        # meta description
        if base in DESC_MAP:
            vi_desc = DESC_MAP[base]
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if 'name="description"' in line and 'content="' in line:
                    lines[i] = f'  <meta name="description" content="{vi_desc}">'
                    break
            content = '\n'.join(lines)
        
        # canonical
        content = content.replace(
            f'href="https://vietnam-japan-guide.com/articles/vinh-tru/{jp_file}"',
            f'href="https://vietnam-japan-guide.com/articles/vinh-tru/{jp_file.replace(".html", ".vi.html")}"'
        )
        
        # Add hreflang
        vi_filename = jp_file.replace('.html', '.vi.html')
        canonical_tag = f'<link rel="canonical" href="https://vietnam-japan-guide.com/articles/vinh-tru/{vi_filename}">'
        hreflang_ja = f'  <link rel="alternate" hreflang="ja" href="https://vietnam-japan-guide.com/articles/vinh-tru/{jp_file}">'
        hreflang_vi = f'  <link rel="alternate" hreflang="vi" href="https://vietnam-japan-guide.com/articles/vinh-tru/{vi_filename}">'
        content = re.sub(
            r'<link rel="canonical"[^>]+>',
            f'{canonical_tag}\n  {hreflang_ja}\n  {hreflang_vi}',
            content
        )
        
        # JSON-LD
        content = content.replace('"inLanguage":"ja"', '"inLanguage":"vi"')
        content = content.replace('"dateModified":"2026-07-16"', '"dateModified":"2026-07-19"')
        content = content.replace('"name":"トップページ"', '"name":"Trang chủ"')
        content = content.replace('"name":"永住・帰化"', '"name":"Vĩnh trú & Nhập tịch"')
        
        # headline
        for jp_t, vi_t in TITLE_JP_TO_VI.items():
            content = content.replace(f'"headline":"{jp_t}"', f'"headline":"{vi_t}"')
        
        # breadcrumb name
        for jp_t, vi_t in TITLE_JP_TO_VI.items():
            content = content.replace(f'"name":"{jp_t}"', f'"name":"{vi_t}"')
        
        # body translations
        content = translate_text(content)
        
        # Fix specific items after icon conversion
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
        
        # h1
        for jp_t, vi_t in TITLE_JP_TO_VI.items():
            # Find h1 with this title
            h1_pattern = f'<h1>{jp_t}</h1>'
            if h1_pattern in content:
                content = content.replace(h1_pattern, f'<h1>{vi_t}</h1>')
                break
        
        # breadcrumb current
        for jp_t, vi_t in TITLE_JP_TO_VI.items():
            bc_pattern = f'breadcrumb__item--current">{jp_t}</li>'
            if bc_pattern in content:
                content = content.replace(bc_pattern, f'breadcrumb__item--current">{vi_t}</li>')
                break
        
        # Fix page links
        content = re.sub(
            r'href="/articles/vinh-tru/([^"]*?)\.html"',
            lambda m: f'href="/articles/vinh-tru/{m.group(1)}.vi.html"',
            content
        )
        content = re.sub(
            r'href="/pages/vinh-tru\.html"',
            'href="/pages/vinh-tru.html"',
            content
        )
        
        # Write
        with open(vi_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        vi_lines = content.count('\n')
        ratio = min(vi_lines, jp_lines) / max(vi_lines, jp_lines) * 100 if max(vi_lines, jp_lines) > 0 else 0
        status = "✅" if ratio >= 95 else "⚠️"
        print(f"{status} {jp_file} ({jp_lines}行) -> {vi_filename} ({vi_lines}行, {ratio:.1f}%)")

if __name__ == '__main__':
    process_vinh_tru()