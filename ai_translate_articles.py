#!/usr/bin/env python3
"""
AI Translate all JP articles to Vietnamese using the prompt from VIETNAMESE_QA_PROMPT.md.
Preserves HTML structure - only translates body text content.
"""
import os, re, sys, json, time
sys.setrecursionlimit(10000)

BASE = os.path.dirname(os.path.abspath(__file__))

def cnt_jp(t):
    return len(re.findall(r'[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9fff]', t))

def extract_body_text(jp_html):
    """Extract text content from body, preserving HTML tags"""
    body_match = re.search(r'<body>(.*?)</body>', jp_html, re.DOTALL)
    if not body_match:
        return "", jp_html
    return body_match.group(1), jp_html

def build_translation_prompt(jp_body_text, filename):
    """Build the translation prompt using VIETNAMESE_QA_PROMPT.md template"""
    prompt_template = """Bạn là một nhà văn chuyên nghiệp người Việt Nam.
Hãy tuân thủ nghiêm ngặt các quy tắc sau để viết bài cho người Việt sống tại Nhật Bản bằng tiếng Việt.

【QUY TẮC TUYỆT ĐỐI】
1. KHÔNG dịch từng từ tiếng Nhật - hãy viết lại nội dung bằng tiếng Việt tự nhiên
2. KHÔNG giữ nguyên cấu trúc câu tiếng Nhật
3. Phải có dấu thanh điệu chính xác (á à ả ã ạ)
4. Sử dụng các thuật ngữ thống nhất sau (KHÔNG được sai lệch):
   - Vĩnh trú (vĩnh trú)
   - Visa Gijinkoku (visa kỹ thuật - nhân văn - quốc tế)
   - Cục Quản lý Xuất nhập cảnh (cục xuất nhập cảnh)
   - Gyoseishoshi (luật sư hành chính)
   - Thẻ lưu trú (thẻ cư trú)
   - Gia hạn (gia hạn)
   - Chuyển đổi (chuyển đổi)
   - Nộp đơn (nộp đơn)
5. Bạn đọc là người Việt sống tại Nhật Bản
6. Giải thích thuật ngữ chuyên môn trước khi sử dụng
7. GIỮ NGUYÊN số dòng - không thêm bớt dòng

【Nội dung tiếng Nhật gốc】
(Dán nội dung tiếng Nhật vào đây)

Hãy viết bài bằng tiếng Việt theo các quy tắc trên."""
    return prompt_template.replace("(Dán nội dung tiếng Nhật vào đây)", jp_body_text)

def translate_via_ai(jp_body_text, filename):
    """Translate body text via AI"""
    # Build the prompt
    prompt = build_translation_prompt(jp_body_text, filename)
    
    # Write prompt to file for AI processing
    prompt_file = os.path.join(BASE, f"_translate_prompt_{os.getpid()}.txt")
    with open(prompt_file, 'w', encoding='utf-8') as f:
        f.write(prompt)
    
    # Read the prompt back and produce translation
    # The AI will process this file and generate translation
    print(f"  ⏳ 翻訳プロンプト生成: {filename}")
    print(f"  📄 プロンプトファイル: {prompt_file}")
    print(f"  📏 本文サイズ: {len(jp_body_text)}文字, 日本語: {cnt_jp(jp_body_text)}文字")
    
    return prompt_file

def generate_vi_from_jp(jp_path, vi_path):
    """Generate VI HTML from JP source with template translation"""
    with open(jp_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    fn = os.path.basename(jp_path)
    dn = os.path.basename(os.path.dirname(jp_path))
    vn = fn.replace('.html', '.vi.html')
    
    # Labels and fixed translations
    LABELS = {
        "おことわり": "Tuyên bố miễn trừ", "本記事のポイント": "Những điểm chính",
        "見極めポイント": "Điểm chính", "具体的な内容": "Nội dung cụ thể",
        "目次": "Mục lục", "よくある質問（FAQ）": "Câu hỏi thường gặp (FAQ)",
        "情報源": "Nguồn thông tin", "出典・参考リンク": "Tham khảo", "関連記事": "Bài viết liên quan",
        "永住・帰化": "Vĩnh trú & Nhập tịch", "ビザ・更新": "Visa & Gia hạn",
        "生活・行政": "Đời sống & Hành chính", "仕事・金融": "Công việc & Tài chính",
        "トップページ": "Trang chủ", "メニュー": "Menu", "トップに戻る": "Lên đầu trang",
        "当サイトについて": "Về chúng tôi", "カテゴリー": "Danh mục",
        "永住権": "Vĩnh trú", "ビザ": "Visa", "生活": "Đời sống", "仕事": "Công việc", "帰化": "Nhập tịch",
        "⚠️": "&#x26a0;&#xfe0f;", "📝": "&#x1f4dd;", "📑": "&#x1f4d1;", "📌": "&#x1f4cc;",
        "📞": "&#x1f4de;", "📖": "&#x1f4d6;", "❓": "&#x2753;",
        "𝕏 Twitter": "&#x1d54f; Twitter", "↑": "&uarr;", "お困りですか？": "Bạn gặp khó khăn?",
    }
    
    res = []
    canon_done = False
    body_lines = []
    in_body = False
    
    for line in lines:
        s = line.strip()
        
        if 'lang="ja"' in s:
            res.append(line.replace('lang="ja"', 'lang="vi"'))
            continue
        if s.startswith('<title>') and '</title>' in s:
            res.append(re.sub(r'<title>(.+?)｜.+? \| Vietnam Japan Guide</title>',
                            r'<title>\1｜Hướng dẫn cho người Việt | Vietnam Japan Guide</title>', line))
            continue
        if '<link rel="canonical"' in s and not canon_done:
            canon_done = True
            ju = f'https://vietnam-japan-guide.com/articles/{dn}/{fn}'
            vu = f'https://vietnam-japan-guide.com/articles/{dn}/{vn}'
            res.append(f'  <link rel="canonical" href="{vu}">')
            res.append(f'  <link rel="alternate" hreflang="ja" href="{ju}">')
            res.append(f'  <link rel="alternate" hreflang="vi" href="{vu}">')
            continue
        if '"inLanguage":"ja"' in s:
            res.append(line.replace('"inLanguage":"ja"', '"inLanguage":"vi"'))
            continue
        if '"dateModified":"2026-07-16"' in s:
            res.append(line.replace('"dateModified":"2026-07-16"', '"dateModified":"2026-07-19"'))
            continue
        if '"name":"トップページ"' in s:
            res.append(line.replace('"name":"トップページ"', '"name":"Trang chủ"'))
            continue
        
        if '<body' in line:
            in_body = True
            res.append(line)
            continue
        if '</body>' in line:
            in_body = False
            res.append(line)
            continue
        
        if in_body:
            new_line = line
            # Apply labels (safe replacements)
            for jp, vi in sorted(LABELS.items(), key=lambda x: -len(x[0])):
                new_line = new_line.replace(jp, vi)
            # Fixed disclaimers
            if '本記事は日本の行政機関等の公式情報' in new_line:
                new_line = new_line.replace(
                    '本記事は日本の行政機関等の公式情報や一般的な社会ルールをもとに、制度や手続きを整理して提供するものです。個別の手続きや契約に関する判断については、必ず各管轄窓口やサービス提供会社等にてご確認ください。',
                    'Bài viết này được biên soạn dựa trên thông tin chính thức từ các cơ quan hành chính Nhật Bản và các quy tắc xã hội chung. Đối với các quyết định liên quan đến thủ tục hoặc hợp đồng cụ thể, vui lòng xác nhận tại quầy có thẩm quyền hoặc công ty cung cấp dịch vụ.'
                )
            if '初回無料相談対応の専門家があなたのケースをサポートします。' in new_line:
                new_line = new_line.replace(
                    '初回無料相談対応の専門家があなたのケースをサポートします。',
                    'Chuyên gia tư vấn miễn phí lần đầu sẽ hỗ trợ trường hợp của bạn.'
                )
            if '※ 当サイトは法律専門家ではありません。' in new_line:
                new_line = new_line.replace(
                    '※ 当サイトは法律専門家ではありません。記載内容は参考情報であり、正確な判断については各管轄窓口または専門家にご確認ください。',
                    '※ Trang web này không phải là chuyên gia pháp lý. Nội dung chỉ mang tính tham khảo. Để được tư vấn chính xác, vui lòng tham khảo các quầy có thẩm quyền hoặc chuyên gia.'
                )
            new_line = new_line.replace("永住", "Vĩnh trú")
            res.append(new_line)
        else:
            res.append(line)
    
    out = '\n'.join(res)
    with open(vi_path, 'w', encoding='utf-8') as f:
        f.write(out)
    
    jl = len(lines)
    vl = len(res)
    body = out.split('<body>')[1].split('</body>')[0] if '<body>' in out else out
    return jl, vl, min(jl,vl)/max(jl,vl)*100, cnt_jp(body)

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else 'vinh-tru'
    cats = [target]
    
    for cat in cats:
        d = os.path.join(BASE, "articles", cat)
        jf = sorted([f for f in os.listdir(d) if f.endswith('.html') and not f.endswith('.vi.html') and 'skeleton' not in f.lower()])
        
        print(f"\n📁 {cat}/ ({len(jf)} articles)")
        print("=" * 60)
        
        for i, j in enumerate(jf):
            jp = os.path.join(d, j)
            vi = os.path.join(d, j.replace('.html', '.vi.html'))
            
            # Generate template-translated version first
            jl, vl, ratio, rj = generate_vi_from_jp(jp, vi)
            
            # Read back to get body text
            with open(vi, 'r', encoding='utf-8') as f:
                vi_content = f.read()
            
            # Check remaining JP
            body = vi_content.split('<body>')[1].split('</body>')[0] if '<body>' in vi_content else vi_content
            clean = re.sub(r'<[^>]+>', '', body)
            remaining_jp = cnt_jp(clean)
            
            status = "✅" if remaining_jp == 0 else "⚠️"
            print(f"{status} [{i+1}/{len(jf)}] {j}: {jl}→{vl}行, JP残存{remaining_jp}文字")
            
            # If JP still remains, generate AI prompt for this file
            if remaining_jp > 0:
                prompt_file = translate_via_ai(body, j)
                # Small delay
                time.sleep(0.1)
        
        print(f"\n📊 {cat} 処理完了")

if __name__ == '__main__':
    main()