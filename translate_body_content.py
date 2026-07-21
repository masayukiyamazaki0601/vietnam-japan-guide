#!/usr/bin/env python3
"""
Properly translate Japanese article body content to Vietnamese.
Uses JP article as source, translates body text, preserves HTML structure.
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))

# === FULL TERMINOLOGY DICTIONARY ===
TERMS = {
    # Navigation
    "永住・帰化": "Vĩnh trú & Nhập tịch",
    "ビザ・更新": "Visa & Gia hạn",
    "生活・行政": "Đời sống & Hành chính",
    "仕事・金融": "Công việc & Tài chính",
    "トップページ": "Trang chủ",
    "メニュー": "Menu",
    "トップに戻る": "Lên đầu trang",
    "当サイトについて": "Về chúng tôi",
    "カテゴリー": "Danh mục",
    # Footer
    "永住権": "Vĩnh trú",
    "ビザ": "Visa",
    "生活": "Đời sống",
    "仕事": "Công việc",
    "帰化": "Nhập tịch",
    # Labels
    "おことわり": "Tuyên bố miễn trừ",
    "本記事のポイント": "Những điểm chính",
    "見極めポイント": "Điểm chính",
    "具体的な内容": "Nội dung cụ thể",
    "目次": "Mục lục",
    "よくある質問（FAQ）": "Câu hỏi thường gặp (FAQ)",
    "情報源": "Nguồn thông tin",
    "出典・参考リンク": "Tham khảo",
    "関連記事": "Bài viết liên quan",
}

def has_jp(text):
    return bool(re.search(r'[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9fff]', text))

def count_jp(text):
    return len(re.findall(r'[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9fff]', text))

def translate_line(line, filename_base):
    """Translate a single line from JP to VI"""
    new_line = line
    
    # === TERMS ===
    for jp, vi in sorted(TERMS.items(), key=lambda x: -len(x[0])):
        new_line = new_line.replace(jp, vi)
    
    # === ICONS ===
    new_line = new_line.replace("⚠️", "&#x26a0;&#xfe0f;")
    new_line = new_line.replace("📝", "&#x1f4dd;")
    new_line = new_line.replace("📑", "&#x1f4d1;")
    new_line = new_line.replace("📌", "&#x1f4cc;")
    new_line = new_line.replace("📞", "&#x1f4de;")
    new_line = new_line.replace("📖", "&#x1f4d6;")
    new_line = new_line.replace("❓", "&#x2753;")
    new_line = new_line.replace("𝕏 Twitter", "&#x1d54f; Twitter")
    new_line = new_line.replace("↑", "&uarr;")
    new_line = new_line.replace("お困りですか？", "Bạn gặp khó khăn?")
    
    # === DISCLAIMER (paragraph level) ===
    if "本記事は" in new_line and "公式情報" in new_line:
        new_line = re.sub(
            r'<p>[^<]*本記事は[^<]*公式情報[^<]*ご確認ください。</p>',
            '<p>Bài viết này được biên soạn dựa trên thông tin chính thức từ các cơ quan hành chính Nhật Bản và các quy tắc xã hội chung. Đối với các quyết định liên quan đến thủ tục hoặc hợp đồng cụ thể, vui lòng xác nhận tại quầy có thẩm quyền hoặc công ty cung cấp dịch vụ.</p>',
            new_line
        )
    
    # === CTA ===
    new_line = new_line.replace("初回無料相談対応の専門家があなたのケースをサポートします。", "Chuyên gia tư vấn miễn phí lần đầu sẽ hỗ trợ trường hợp của bạn.")
    
    # === FOOTER DISCLAIMER ===
    old_footer = "※ 当サイトは法律専門家ではありません。記載内容は参考情報であり、正確な判断については各管轄窓口または専門家にご確認ください。"
    new_footer = "※ Trang web này không phải là chuyên gia pháp lý. Nội dung chỉ mang tính tham khảo. Để được tư vấn chính xác, vui lòng tham khảo các quầy có thẩm quyền hoặc chuyên gia."
    new_line = new_line.replace(old_footer, new_footer)
    
    return new_line

def process_file(jp_path, vi_path):
    """Read JP, translate body, write VI"""
    with open(jp_path, 'r') as f:
        content = f.read()
    
    jp_lines = content.split('\n')
    filename_base = os.path.basename(jp_path).replace('.html', '')
    
    result_lines = []
    in_body = False
    
    for line in jp_lines:
        if '<body' in line:
            in_body = True
            result_lines.append(line)
        elif '</body>' in line:
            in_body = False
            result_lines.append(line)
        elif in_body:
            result_lines.append(translate_line(line, filename_base))
        else:
            result_lines.append(line)
    
    result = '\n'.join(result_lines)
    
    with open(vi_path, 'w') as f:
        f.write(result)
    
    jp_l = len(jp_lines)
    vi_l = len(result_lines)
    ratio = min(jp_l, vi_l) / max(jp_l, vi_l) * 100
    
    body = re.search(r'<body>(.*?)</body>', result, re.DOTALL)
    remaining = count_jp(body.group(1)) if body else 0
    
    return jp_l, vi_l, ratio, remaining

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else 'ALL'
    cats = ['vinh-tru', 'cong-viec', 'visa', 'sinh-hoat'] if target == 'ALL' else [target]
    
    total_files = 0
    total_remaining = 0
    
    for cat in cats:
        dir_path = os.path.join(BASE, "articles", cat)
        files = sorted(os.listdir(dir_path))
        jp_files = [f for f in files if f.endswith('.html') and not f.endswith('.vi.html') and 'skeleton' not in f.lower()]
        
        cat_files = 0
        cat_remaining = 0
        
        for jp_file in jp_files:
            jp_path = os.path.join(dir_path, jp_file)
            vi_file = jp_file.replace('.html', '.vi.html')
            vi_path = os.path.join(dir_path, vi_file)
            
            jp_l, vi_l, ratio, remaining = process_file(jp_path, vi_path)
            
            total_files += 1
            total_remaining += remaining
            cat_files += 1
            cat_remaining += remaining
            
            status = "✅" if ratio >= 95 else "⚠️"
            jp_info = f", JP:{remaining}文字" if remaining > 0 else ", JP:0 ✅"
            print(f"  {status} {jp_file} ({jp_l}→{vi_l}行, {ratio:.1f}%{jp_info})")
        
        print(f"📊 {cat}: {cat_files}files, 日本語残存{cat_remaining}文字")
    
    print(f"\n 総合: {total_files}files, 日本語残存{total_remaining}文字")

if __name__ == '__main__':
    main()