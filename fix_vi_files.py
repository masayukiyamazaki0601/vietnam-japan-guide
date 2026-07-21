#!/usr/bin/env python3
"""
Fix issues in generated .vi.html files:
1. Remove duplicate </title> tags
2. Fix titles to Vietnamese
3. Fix descriptions
4. Fix JSON-LD headline and breadcrumb names
5. Verify hreflang tags
"""
import os
import re

ARTICLES_DIR = os.path.dirname(os.path.abspath(__file__)) + "/articles/cong-viec"

TITLE_MAP = {
    "ふるさと納税のやり方": "Cách thực hiện Furusato Nozei (quyên góp địa phương)",
    "扶養家族を日本に呼んだ後の税金への影響": "Ảnh hưởng thuế sau khi gọi gia đình phụ thuộc sang Nhật",
    "扶養控除で節税する方法": "Cách giảm thuế với khấu trừ người phụ thuộc",
    "外国人が日本で資産運用する際のリスク": "Rủi ro khi người nước ngoài quản lý tài sản tại Nhật",
    "銀行送金の比較：銀行・インターネット送金サービス": "So sánh chuyển tiền ngân hàng: Ngân hàng & dịch vụ chuyển tiền online",
    "外国人の住宅ローンの組み方": "Cách vay mua nhà cho người nước ngoài tại Nhật",
    "確定申告が必要なケースとは": "Các trường hợp cần khai thuế thu nhập (Kakutei Shinkoku)",
    "給与明細書の見方と控除の基本": "Cách đọc phiếu lương và cơ bản về các khoản khấu trừ",
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
    "特定技能の求人を探す方法": "Cách tìm việc cho Kỹ năng đặc định",
    "ベトナム人エンジニアの転職ガイド": "Hướng dẫn chuyển việc cho kỹ sư người Việt",
    "在日ベトナム人向けキャリアアップガイド": "Hướng dẫn thăng tiến sự nghiệp cho người Việt tại Nhật",
}

DESC_MAP = {
    "ふるさと納税のやり方": "Giải thích cách thực hiện Furusato Nozei. Cơ chế, giới hạn khấu trừ, thủ tục, lợi ích, lưu ý cho người nước ngoài.",
    "扶養控除で節税する方法": "Giải thích cách giảm thuế bằng khấu trừ người phụ thuộc. Điều kiện, số tiền khấu trừ, thủ tục đăng ký tại nơi làm việc.",
    "外国人が日本で資産運用する際のリスク": "Giải thích rủi ro khi người nước ngoài quản lý tài sản tại Nhật. Rủi ro tỷ giá, thuế, pháp lý, lừa đảo.",
    "銀行送金の比較：銀行・インターネット送金サービス": "So sánh chuyển tiền ngân hàng và dịch vụ chuyển tiền online. Phí, tỷ giá, thời gian, an toàn.",
    "外国人の住宅ローンの組み方": "Giải thích cách vay mua nhà cho người nước ngoài. Điều kiện, tư cách lưu trú, lãi suất, giấy tờ.",
    "確定申告が必要なケースとは": "Giải thích các trường hợp cần khai thuế thu nhập. Điều kiện, thời hạn, thủ tục, nộp thuế.",
    "給与明細書の見方と控除の基本": "Giải thích cách đọc phiếu lương và các khoản khấu trừ. Bảo hiểm, thuế, phụ cấp.",
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
    "特定技能の求人を探す方法": "Giải thích cách tìm việc cho Kỹ năng đặc định. Trang web, điều kiện, thủ tục.",
    "ベトナム人エンジニアの転職ガイド": "Hướng dẫn chuyển việc cho kỹ sư IT người Việt tại Nhật. Chuẩn bị, tìm việc, thủ tục.",
}

def fix_file(vi_path):
    """Fix common issues in a VI file"""
    with open(vi_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix 1: Remove duplicate </title>
    content = content.replace('</title></title>', '</title>')
    
    # Fix 2: Fix title to Vietnamese
    for jp_title, vi_title in TITLE_MAP.items():
        old_title = f'<title>{jp_title}｜Hướng dẫn cho người Việt | Vietnam Japan Guide</title>'
        new_title = f'<title>{vi_title}｜Hướng dẫn cho người Việt | Vietnam Japan Guide</title>'
        if old_title in content:
            content = content.replace(old_title, new_title)
        
        # Also fix the pattern without "Hướng dẫn"
        old_title2 = f'<title>{jp_title}｜Vietnam Japan Guide | Vietnam Japan Guide</title>'
        new_title2 = f'<title>{vi_title}｜Hướng dẫn cho người Việt | Vietnam Japan Guide</title>'
        if old_title2 in content:
            content = content.replace(old_title2, new_title2)
        
        # Fix JSON-LD headline
        content = content.replace(f'"headline":"{jp_title}"', f'"headline":"{vi_title}"')
        
        # Fix breadcrumb name at position 3
        content = content.replace(f'"position":3,"name":"{jp_title}"', f'"position":3,"name":"{vi_title}"')
    
    # Fix 3: Fix meta description
    for jp_title, vi_desc in DESC_MAP.items():
        vi_title = TITLE_MAP.get(jp_title, jp_title)
        # Look for description with Japanese content
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'name="description"' in line and 'content="' in line:
                # Check if it's still Japanese
                if any('\u4e00' <= c <= '\u9fff' for c in line):
                    lines[i] = f'  <meta name="description" content="{vi_desc}">'
                    break
        content = '\n'.join(lines)
    
    # Fix 4: Fix canonical URLs - some may still point to .html
    content = re.sub(
        r'(href="https://vietnam-japan-guide\.com/articles/cong-viec/[^"]*)\.html(\?[^"]*)?"',
        lambda m: m.group(0).replace('.html', '.vi.html') if not m.group(0).endswith('.vi.html') else m.group(0),
        content
    )
    
    # Fix 5: Fix breadcrumb item name (not JSON-LD, the HTML one)
    for jp_title, vi_title in TITLE_MAP.items():
        if f'breadcrumb__item--current">{jp_title}</li>' in content:
            content = content.replace(
                f'breadcrumb__item--current">{jp_title}</li>',
                f'breadcrumb__item--current">{vi_title}</li>'
            )
    
    # Fix 6: Fix article h1
    for jp_title, vi_title in TITLE_MAP.items():
        content = content.replace(f'<h1>{jp_title}</h1>', f'<h1>{vi_title}</h1>')
    
    # Only write if changed
    if content != original:
        with open(vi_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def validate_file(vi_path):
    """Validate a VI file"""
    with open(vi_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check lang
    if 'lang="ja"' in content:
        issues.append("lang=ja")
    
    # Check duplicate title
    if content.count('</title>') > 1:
        issues.append(f"dup title ({content.count('</title>')})")
    
    # Check hreflang
    if 'hreflang="ja"' not in content:
        issues.append("missing hreflang ja")
    if 'hreflang="vi"' not in content:
        issues.append("missing hreflang vi")
    
    # Check footer translated
    if '当サイトについて' in content:
        issues.append("JP footer text")
    
    return issues

def main():
    files = sorted([f for f in os.listdir(ARTICLES_DIR) if f.endswith('.vi.html')])
    
    # Fix all
    fixed_count = 0
    for f in files:
        vi_path = os.path.join(ARTICLES_DIR, f)
        if fix_file(vi_path):
            fixed_count += 1
    
    print(f"Fixed {fixed_count} files\n")
    
    # Validate all
    print("Validation report:")
    print("-" * 60)
    for f in files:
        vi_path = os.path.join(ARTICLES_DIR, f)
        issues = validate_file(vi_path)
        jp_file = f.replace('.vi.html', '.html')
        jp_path = os.path.join(ARTICLES_DIR, jp_file)
        
        if os.path.exists(jp_path):
            with open(jp_path, 'r') as fj:
                jp_lines = fj.read().count('\n')
            with open(vi_path, 'r') as fv:
                vi_lines = fv.read().count('\n')
            ratio = min(jp_lines, vi_lines) / max(jp_lines, vi_lines) * 100
        
        status = "✅" if not issues else "⚠️"
        issue_str = ", ".join(issues) if issues else "OK"
        print(f"{status} {f:50s} {issue_str} ({vi_lines}行, {ratio:.1f}%一致)")

if __name__ == '__main__':
    main()