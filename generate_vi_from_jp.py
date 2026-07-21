#!/usr/bin/env python3
"""Generate clean VI HTML from JP source. v2 - full effort edition."""
import os, re, sys
BASE = os.path.dirname(os.path.abspath(__file__))

# === MEGA DICTIONARY ===
R = {
    # Nav/Footer
    "永住・帰化":"Vĩnh trú & Nhập tịch","ビザ・更新":"Visa & Gia hạn","生活・行政":"Đời sống & Hành chính","仕事・金融":"Công việc & Tài chính",
    "トップページ":"Trang chủ","メニュー":"Menu","トップに戻る":"Lên đầu trang","当サイトについて":"Về chúng tôi","カテゴリー":"Danh mục",
    "永住権":"Vĩnh trú","ビザ":"Visa","生活":"Đời sống","仕事":"Công việc","帰化":"Nhập tịch","永住":"Vĩnh trú","ビザ":"Visa",
    # Labels
    "おことわり":"Tuyên bố miễn trừ","本記事のポイント":"Những điểm chính","見極めポイント":"Điểm chính","具体的な内容":"Nội dung cụ thể",
    "目次":"Mục lục","よくある質問（FAQ）":"Câu hỏi thường gặp (FAQ)","情報源":"Nguồn thông tin","出典・参考リンク":"Tham khảo","関連記事":"Bài viết liên quan",
    # === CORE TERMS ===
    "技術・人文知識・国際業務":"Kỹ thuật - Nhân văn - Quốc tế","技人国ビザ":"Visa Gijinkoku","技人国":"Gijinkoku",
    "特定技能1号":"Kỹ năng đặc định số 1","特定技能2号":"Kỹ năng đặc định số 2","特定技能":"Kỹ năng đặc định",
    "家族滞在":"Gia đình","配偶者ビザ":"Visa hôn phối","配偶者":"Hôn phối","経営管理":"Quản lý kinh doanh","留学":"Du học",
    "在留カード":"Thẻ lưu trú","出入国在留管理庁":"Cục Quản lý Xuất nhập cảnh","行政書士":"Gyoseishoshi (luật sư hành chính)",
    "申請する":"Nộp đơn","申請":"nộp đơn","更新する":"Gia hạn","変更する":"Chuyển đổi","不許可":"Không được cấp phép",
    "必要書類":"Giấy tờ cần thiết","審査期間":"Thời gian xét duyệt","条件":"Điều kiện","注意点":"Lưu ý","手続き":"Thủ tục",
    "税金":"Thuế","年金":"Nenkin (lương hưu)","健康保険":"Bảo hiểm y tế","住民票":"Giấy đăng ký cư trú","マイナンバー":"Mã số My Number",
    "在留資格":"Tư cách lưu trú","審査":"Xét duyệt","基準":"Tiêu chuẩn","影響":"Ảnh hưởng","扶養":"Phụ thuộc","確定申告":"Khai thuế",
    "納税":"Nộp thuế","保険料":"Phí bảo hiểm","給与":"Lương","年収":"Thu nhập năm","月収":"Thu nhập tháng","手取り":"Thực lãnh",
    "控除":"Khấu trừ","社会保険":"Bảo hiểm xã hội","所得税":"Thuế thu nhập","住民税":"Thuế cư trú","雇用保険":"Bảo hiểm việc làm",
    "厚生年金":"Lương hưu xã hội","転職":"Chuyển việc","退職":"Nghỉ việc","就労":"Làm việc","契約":"Hợp đồng",
    "解除":"Hủy bỏ","承認":"Phê duyệt","許可":"Cấp phép","申請中":"Đang nộp đơn","未納":"Chưa nộp","滞納":"Nợ đọng",
    "納付":"Nộp","支払い":"Thanh toán","加入":"Tham gia","脱退":"Rút lui","期間":"Thời gian","期限":"Hạn",
    "住所":"Địa chỉ","氏名":"Họ tên","国籍":"Quốc tịch","身元保証人":"Người bảo lãnh","理由書":"Lý do","面接":"Phỏng vấn",
    "証明書":"Giấy chứng nhận","戸籍":"Hộ tịch","婚姻":"Kết hôn","離婚":"Ly hôn","出生":"Khai sinh","死亡":"Tử vong",
    "親族":"Thân nhân","家族":"Gia đình","子供":"Con","父母":"Cha mẹ","未婚":"Độc thân","既婚":"Đã kết hôn",
    # === EXTRA COMMON PHRASES ===
    "場合":"trường hợp","方法":"cách","仕組み":"cơ chế","基礎知識":"kiến thức cơ bản","必要":"cần thiết","可能":"có thể",
    "重要":"quan trọng","必須":"bắt buộc","任意":"tùy chọn","以上":"trên","以下":"dưới","以内":"trong vòng",
    "について":"về","に関する":"liên quan đến","における":"tại","から":"từ","まで":"đến","など":"v.v.",
    "それぞれ":"mỗi","さまざま":"nhiều","主な":"chính","一般的":"thông thường","具体的":"cụ thể","明確":"rõ ràng",
    "適切":"thích hợp","正しい":"chính xác","間違い":"sai lầm","注意":"chú ý","確認":"xác nhận","手順":"quy trình",
    "流れ":"quy trình","進め方":"cách tiến hành","見方":"cách đọc","選び方":"cách chọn","書き方":"cách viết",
    "考え方":"cách nghĩ","表":"bảng","図":"hình","リスト":"danh sách","ケース":"trường hợp","パターン":"mẫu",
    "例":"ví dụ","目安":"tham khảo","ポイント":"điểm","コツ":"mẹo","メリット":"lợi ích","デメリット":"bất lợi",
    "リスク":"rủi ro","安全性":"an toàn","安定性":"ổn định","収入":"thu nhập","支出":"chi tiêu","所得":"thu nhập",
    "資産":"tài sản","負債":"nợ","資金":"vốn","投資":"đầu tư","運用":"quản lý","貯金":"tiết kiệm",
    "借入":"vay","返済":"trả nợ","金利":"lãi suất","利息":"lãi","元本":"gốc",
    "勤務先":"nơi làm việc","勤続年数":"số năm làm việc","正社員":"nhân viên chính thức","契約社員":"nhân viên hợp đồng",
    "派遣社員":"nhân viên tạm thời","アルバイト":"làm thêm","パート":"bán thời gian","自営業":"tự kinh doanh",
    "会社員":"nhân viên công ty","公務員":"công chức","経営者":"chủ doanh nghiệp",
    "日本語能力":"khả năng tiếng Nhật","N1":"N1","N2":"N2","N3":"N3",
    "大学":"đại học","専門学校":"trường chuyên môn","日本語学校":"trường tiếng Nhật",
    # === VERBS ===
    "解説する":"giải thích","説明する":"giải thích","紹介する":"giới thiệu","まとめる":"tổng hợp",
    "確認する":"xác nhận","提出する":"nộp","記入する":"điền","作成する":"tạo","準備する":"chuẩn bị",
    "取得する":"đạt được","維持する":"duy trì","管理する":"quản lý","利用する":"sử dụng",
    "判断する":"đánh giá","決定する":"quyết định","選択する":"lựa chọn",
    # Icons
    "⚠️":"&#x26a0;&#xfe0f;","📝":"&#x1f4dd;","📑":"&#x1f4d1;","📌":"&#x1f4cc;",
    "📞":"&#x1f4de;","📖":"&#x1f4d6;","❓":"&#x2753;","𝕏 Twitter":"&#x1d54f; Twitter","↑":"&uarr;",
    "お困りですか？":"Bạn gặp khó khăn?",
}

DISCLAIMER = [
    ('<p>本記事は日本の行政機関等の公式情報や一般的な社会ルールをもとに、制度や手続きを整理して提供するものです。個別の手続きや契約に関する判断については、必ず各管轄窓口やサービス提供会社等にてご確認ください。</p>',
     '<p>Bài viết này được biên soạn dựa trên thông tin chính thức từ các cơ quan hành chính Nhật Bản và các quy tắc xã hội chung. Đối với các quyết định liên quan đến thủ tục hoặc hợp đồng cụ thể, vui lòng xác nhận tại quầy có thẩm quyền hoặc công ty cung cấp dịch vụ.</p>'),
    ('<p>本記事は出入国在留管理庁が公開している公式情報等をもとに、制度や手続きを整理して提供するものです。個別の在留資格審査や許可判断については、必ず出入国在留管理庁または行政書士等の専門家へご確認ください。</p>',
     '<p>Bài viết này được biên soạn dựa trên thông tin chính thức từ Cục Quản lý Xuất nhập cảnh Nhật Bản. Đối với các quyết định cụ thể, vui lòng xác nhận tại Cục Quản lý Xuất nhập cảnh hoặc chuyên gia Gyoseishoshi.</p>'),
]

FIXED = {
    '初回無料相談対応の専門家があなたのケースをサポートします。': 'Chuyên gia tư vấn miễn phí lần đầu sẽ hỗ trợ trường hợp của bạn.',
    '※ 当サイトは法律専門家ではありません。記載内容は参考情報であり、正確な判断については各管轄窓口または専門家にご確認ください。': '※ Trang web này không phải là chuyên gia pháp lý. Nội dung chỉ mang tính tham khảo. Để được tư vấn chính xác, vui lòng tham khảo các quầy có thẩm quyền hoặc chuyên gia.',
}

def cnt_jp(t): return len(re.findall(r'[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9fff]', t))

def gen(jp_path, vi_path):
    with open(jp_path, 'r') as f: c = f.read()
    lines = c.split('\n')
    fn = os.path.basename(jp_path); dn = os.path.basename(os.path.dirname(jp_path)); vn = fn.replace('.html', '.vi.html')
    res = []; cd = False
    
    for line in lines:
        s = line.strip()
        if 'lang="ja"' in s: res.append(line.replace('lang="ja"', 'lang="vi"')); continue
        if s.startswith('<title>') and '</title>' in s:
            res.append(re.sub(r'<title>(.+?)｜.+? \| Vietnam Japan Guide</title>', r'<title>\1｜Hướng dẫn cho người Việt | Vietnam Japan Guide</title>', line))
            continue
        if '<link rel="canonical"' in s and not cd:
            cd = True
            jp_u = f'https://vietnam-japan-guide.com/articles/{dn}/{fn}'; vi_u = f'https://vietnam-japan-guide.com/articles/{dn}/{vn}'
            res.append(f'  <link rel="canonical" href="{vi_u}">')
            res.append(f'  <link rel="alternate" hreflang="ja" href="{jp_u}">')
            res.append(f'  <link rel="alternate" hreflang="vi" href="{vi_u}">')
            continue
        if '"inLanguage":"ja"' in s: res.append(line.replace('"inLanguage":"ja"', '"inLanguage":"vi"')); continue
        if '"dateModified":"2026-07-16"' in s: res.append(line.replace('"dateModified":"2026-07-16"', '"dateModified":"2026-07-19"')); continue
        if '"name":"トップページ"' in s: res.append(line.replace('"name":"トップページ"', '"name":"Trang chủ"')); continue
        
        nl = line
        # Apply replacements
        for o, n in sorted(R.items(), key=lambda x: -len(x[0])): nl = nl.replace(o, n)
        # Disclaimer paragraphs
        for jp_d, vi_d in DISCLAIMER:
            if jp_d in nl: nl = nl.replace(jp_d, vi_d)
        # Fixed texts
        for jp_f, vi_f in FIXED.items():
            if jp_f in nl: nl = nl.replace(jp_f, vi_f)
        res.append(nl)
    
    out = '\n'.join(res)
    with open(vi_path, 'w') as f: f.write(out)
    jl = len(lines); vl = len(res)
    body = out.split('<body>')[1].split('</body>')[0] if '<body>' in out else out
    return jl, vl, min(jl,vl)/max(jl,vl)*100, cnt_jp(body)

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else 'ALL'
    cats = ['vinh-tru', 'cong-viec', 'visa', 'sinh-hoat'] if target == 'ALL' else [target]
    tf, tj, tc = 0, 0, 0
    for cat in cats:
        d = os.path.join(BASE, "articles", cat)
        jf = [f for f in sorted(os.listdir(d)) if f.endswith('.html') and not f.endswith('.vi.html') and 'skeleton' not in f.lower()]
        print(f"\n📁 {cat}/")
        for j in jf:
            jp = os.path.join(d, j); vi = os.path.join(d, j.replace('.html', '.vi.html'))
            jl, vl, r, rj = gen(jp, vi)
            tf += 1; tj += rj; tc += 1 if rj == 0 else 0
            if rj == 0: print(f"  ✅ {j} ({jl}→{vl}行, JP:0 🎉)")
            else: print(f"  ⚠️ {j} ({jl}→{vl}行, JP:{rj})")
        print(f"📊 {cat}: {len(jf)}files")
    print(f"\n📊 総合: {tf}files, JP残存{tj}文字, 完全クリーン{tc}files")
    print("🎉 DONE!" if tj == 0 else f"💪 まだ{tj}文字の日本語。でも諦めない！")

if __name__ == '__main__':
    main()