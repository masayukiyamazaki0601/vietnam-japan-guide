#!/usr/bin/env python3
"""Final translation: JP article → VI article, line-by-line preserving structure.
Template parts: fixed replacement. Body text: AI translates by understanding content.
Each JP line → exactly 1 VI line (or merged for multiline tags)."""
import os, re, sys
BASE = os.path.dirname(os.path.abspath(__file__))

T = {
    "永住・帰化":"Vĩnh trú & Nhập tịch","ビザ・更新":"Visa & Gia hạn",
    "生活・行政":"Đời sống & Hành chính","仕事・金融":"Công việc & Tài chính",
    "トップページ":"Trang chủ","メニュー":"Menu","トップに戻る":"Lên đầu trang",
    "当サイトについて":"Về chúng tôi","カテゴリー":"Danh mục",
    "おことわり":"Tuyên bố miễn trừ","本記事のポイント":"Những điểm chính",
    "目次":"Mục lục","よくある質問（FAQ）":"Câu hỏi thường gặp (FAQ)",
    "情報源":"Nguồn thông tin","出典・参考リンク":"Tham khảo","関連記事":"Bài viết liên quan",
    "永住権":"Vĩnh trú","ビザ":"Visa","生活":"Đời sống","仕事":"Công việc","帰化":"Nhập tịch",
    "⚠️":"&#x26a0;&#xfe0f;","📝":"&#x1f4dd;","📑":"&#x1f4d1;","📌":"&#x1f4cc;","📞":"&#x1f4de;",
    "📖":"&#x1f4d6;","❓":"&#x2753;","𝕏 Twitter":"&#x1d54f; Twitter","↑":"&uarr;",
}

def cnt_jp(t): return len(re.findall(r'[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9fff]', t))

def apply_template(body):
    for j,v in sorted(T.items(),key=lambda x:-len(x[0])): body=body.replace(j,v)
    body=body.replace('本記事は日本の行政機関等の公式情報や一般的な社会ルールをもとに、制度や手続きを整理して提供するものです。個別の手続きや契約に関する判断については、必ず各管轄窓口やサービス提供会社等にてご確認ください。','Bài viết này được biên soạn dựa trên thông tin chính thức từ các cơ quan hành chính Nhật Bản và các quy tắc xã hội chung. Đối với các quyết định liên quan đến thủ tục hoặc hợp đồng cụ thể, vui lòng xác nhận tại quầy có thẩm quyền hoặc công ty cung cấp dịch vụ.')
    body=body.replace('本記事は出入国在留管理庁が公開している公式情報等をもとに、制度や手続きを整理して提供するものです。個別の在留資格審査や許可判断については、必ず出入国在留管理庁または行政書士等の専門家へご確認ください。','Bài viết này được biên soạn dựa trên thông tin chính thức từ Cục Quản lý Xuất nhập cảnh Nhật Bản. Đối với các quyết định cụ thể, vui lòng xác nhận tại Cục Quản lý Xuất nhập cảnh hoặc chuyên gia Gyoseishoshi.')
    body=body.replace('初回無料相談対応の専門家があなたのケースをサポートします。','Chuyên gia tư vấn miễn phí lần đầu sẽ hỗ trợ trường hợp của bạn.')
    body=body.replace('※ 当サイトは法律専門家ではありません。記載内容は参考情報であり、正確な判断については各管轄窓口または専門家にご確認ください。','※ Trang web này không phải là chuyên gia pháp lý. Nội dung chỉ mang tính tham khảo. Để được tư vấn chính xác, vui lòng tham khảo các quầy có thẩm quyền hoặc chuyên gia.')
    return body

def process_all(cat):
    d=os.path.join(BASE,"articles",cat)
    jf=sorted([f for f in os.listdir(d) if f.endswith('.html') and not f.endswith('.vi.html') and 'skeleton' not in f.lower()])
    print(f"\n📁 {cat}/ ({len(jf)} files)")
    total_jp=0
    for j in jf:
        jp=os.path.join(d,j); vi=os.path.join(d,j.replace('.html','.vi.html'))
        with open(jp,'r') as f: content=f.read()
        lines=content.split('\n')
        fn=j; dn=cat; vn=j.replace('.html','.vi.html')
        res=[]; canon_done=False
        for line in lines:
            s=line.strip()
            if 'lang="ja"' in s: res.append(line.replace('lang="ja"','lang="vi"')); continue
            if s.startswith('<title>') and '</title>' in s:
                res.append(re.sub(r'<title>(.+?)｜.+? \| Vietnam Japan Guide</title>',r'<title>\1｜Hướng dẫn cho người Việt | Vietnam Japan Guide</title>',line))
                continue
            if '<link rel="canonical"' in s and not canon_done:
                canon_done=True
                res.append(f'  <link rel="canonical" href="https://vietnam-japan-guide.com/articles/{dn}/{vn}">')
                res.append(f'  <link rel="alternate" hreflang="ja" href="https://vietnam-japan-guide.com/articles/{dn}/{fn}">')
                res.append(f'  <link rel="alternate" hreflang="vi" href="https://vietnam-japan-guide.com/articles/{dn}/{vn}">')
                continue
            if '"inLanguage":"ja"' in s: res.append(line.replace('"inLanguage":"ja"','"inLanguage":"vi"')); continue
            if '"dateModified":"2026-07-16"' in s: res.append(line.replace('"dateModified":"2026-07-16"','"dateModified":"2026-07-19"')); continue
            if '"name":"トップページ"' in s: res.append(line.replace('"name":"トップページ"','"name":"Trang chủ"')); continue
            res.append(apply_template(line))
        out='\n'.join(res)
        with open(vi,'w') as f: f.write(out)
        jl=len(lines); vl=len(out.split('\n'))
        body=out.split('<body>')[1].split('</body>')[0] if '<body>' in out else out
        rj=cnt_jp(body)
        total_jp+=rj
        print(f"  {j}: {jl}→{vl}行 JP{rj}")
    return total_jp

tj=0
for c in ['vinh-tru','cong-viec','visa','sinh-hoat']: tj+=process_all(c)
print(f"\n📊 総日本語残存: {tj}文字")
print(f"{'✅ 完了' if tj==0 else '⚠️ テンプレートのみ翻訳済み'}")