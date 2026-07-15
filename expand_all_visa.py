#!/usr/bin/env python3
"""ビザ・在留資格 31記事を200行に拡充"""
import os, re, glob
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

def get_content(slug):
    """Return expanded content for each article"""
    contents = {
        # ===== 1. freelance-visa-note =====
        "freelance-visa-note": {
            "title": "フリーランス（個人事業主）として働く場合のビザ完全ガイド｜技人国・経営管理・資格外活動",
            "desc": "フリーランスとして日本で働く場合の在留資格の選択肢と注意点を徹底解説。技人国ビザでのフリーランスは可能か、業務委託契約と雇用契約の違い、資格外活動許可、経営管理ビザとの比較、確定申告の義務まで詳しく説明します。",
            "sections": [
                ("フリーランスと在留資格の基礎知識", """
<p>フリーランス（個人事業主）として日本で働く場合、在留資格によって可否が異なります。多くの就労系ビザは「雇用契約」に基づく就労を前提としているため、フリーランスとして活動する場合は注意が必要です。</p>
<h3>在留資格別のフリーランス可否一覧</h3>
<table>
<tr><th>在留資格</th><th>フリーランス可否</th><th>条件・注意点</th></tr>
<tr><td>技人国（技術・人文知識・国際業務）</td><td>原則不可</td><td>雇用契約に基づく就労が前提。単発の業務委託契約のみでは不許可リスク大</td></tr>
<tr><td>経営管理ビザ</td><td>可能</td><td>事業所と継続的な事業実績が必要。資本金500万円以上または常勤従業員2名</td></tr>
<tr><td>永住者・定住者</td><td>可能</td><td>制限なし。自由にフリーランスとして働ける</td></tr>
<tr><td>日本人の配偶者等</td><td>可能</td><td>就労制限なし。自由にフリーランスとして働ける</td></tr>
<tr><td>特定活動（フリーランス可のもの）</td><td>可能</td><td>許可された範囲内でのみ可能</td></tr>
</table>
<h3>技人国ビザでフリーランスが難しい理由</h3>
<p>技人国ビザは「本邦の公私の機関との契約に基づいて行う」活動が前提です。つまり、日本の企業との雇用契約が必要です。フリーランス（個人事業主）として複数のクライアントと業務委託契約を結ぶ形態は、この要件を満たさないと判断される可能性が高いです。</p>
<h3>フリーランスとして働くための代替手段</h3>
<ol>
<li><strong>業務委託契約を結ぶクライアントを1社に絞る</strong>：実質的に雇用契約とみなされる可能性がある</li>
<li><strong>経営管理ビザを取得する</strong>：法人を設立して代表取締役になる</li>
<li><strong>資格外活動許可を取得する</strong>：本業とは別に副業としてフリーランス活動を行う</li>
<li><strong>永住権を取得する</strong>：永住者になれば就労制限なく自由に働ける</li>
</ol>"""),
                ("技人国ビザで副業としてフリーランスをする方法", """
<p>技人国ビザで在留しながら、副業としてフリーランス活動を行うことは条件付きで可能です。</p>
<h3>資格外活動許可の取得が必要</h3>
<p>本業以外の収入を伴う活動（副業・フリーランス）を行う場合は、資格外活動許可を取得する必要があります。許可の条件は以下の通りです：</p>
<ul>
<li>本業（技人国ビザでの活動）に支障がないこと</li>
<li>副業の内容が本業のビザ区分と矛盾しないこと</li>
<li>副業の収入が本業の収入を超えないこと</li>
<li>副業先の業務内容が法令に違反しないこと</li>
</ul>
<h3>副業の収入と確定申告</h3>
<p>副業で年間20万円以上の収入がある場合は、確定申告が必要です。在留期間更新時にも収入状況が確認されるため、正しく申告しましょう。</p>"""),
                ("フリーランスの確定申告と社会保険", """
<h3>確定申告の義務</h3>
<p>フリーランスとして収入を得た場合、以下のルールがあります：</p>
<ul>
<li>年間20万円以上の所得がある場合 → 確定申告が必要</li>
<li>経費を差し引いた「所得」で判断される</li>
<li>青色申告をすると最大65万円の控除を受けられる</li>
<li>消費税の課税事業者になる場合（年間1,000万円超）は注意</li>
</ul>
<h3>社会保険の加入</h3>
<p>フリーランスの場合、以下の社会保障に自分で加入する必要があります：</p>
<ul>
<li><strong>国民健康保険</strong>：市区町村で加入手続き</li>
<li><strong>国民年金</strong>：20歳以上60歳未満は加入義務あり</li>
<li><strong>国民年金基金</strong>：上乗せ年金として任意加入可能</li>
<li><strong>小規模企業共済</strong>：フリーランスの退職金制度</li>
</ul>"""),
                ("よくある質問（FAQ）", """
<h3>Q1. 技人国ビザでフリーランスの仕事を副業としてできますか？</h3>
<p>A. 資格外活動許可を取得すれば可能です。ただし、本業（雇用契約）に支障がない範囲内である必要があります。</p>
<h3>Q2. フリーランスの収入が本業を超えた場合、問題がありますか？</h3>
<p>A. 副業の収入が本業を超えると、審査で本業の安定性が疑問視される可能性があります。</p>
<h3>Q3. 経営管理ビザでフリーランスはできますか？</h3>
<p>A. 経営管理ビザは会社経営が前提です。個人事業主としてのフリーランスは経営管理ビザの対象外です。法人を設立する必要があります。</p>
<h3>Q4. フリーランスでも永住権は申請できますか？</h3>
<p>A. 申請自体は可能ですが、安定した収入と納税実績が求められます。一般的に会社員より審査が厳しくなります。</p>
<h3>Q5. クライアントが海外の企業の場合も資格外活動許可が必要ですか？</h3>
<p>A. 日本で活動している限り、収入源泉が海外でも資格外活動許可が必要です。</p>""")
            ]
        },
    }
    return contents.get(slug)

# Common template
def gen_html(slug, data):
    today = datetime.now().strftime("%Y-%m-%d")
    t = data["title"]; hl = t.split("｜")[0]
    desc = data["desc"]; sections = data["sections"]
    
    nav_links = [("/pages/jobs.html","転職・求人"),("/pages/vinh-tru.html","永住・帰化"),("/pages/visa.html","ビザ・更新"),("/pages/sinh-hoat.html","生活・行政"),("/pages/cong-viec.html","仕事・金融"),("/pages/telecom.html","通信・SIM"),("/pages/estate.html","不動産・住まい"),("/pages/chuyen-gia.html","専門家相談")]
    nav_h = ""
    for i, (u, l) in enumerate(nav_links):
        ac = " header__nav-link--active" if i == 2 else ""
        nav_h += f'          <li><a href="{u}" class="header__nav-link{ac}">{l}</a></li>\n'
    
    toc_items = ""
    sections_html = ""
    for i, (heading, content) in enumerate(sections, 1):
        hid = f"s{i}"
        toc_items += f'          <li><a href="#{hid}">{heading}</a></li>\n'
        sections_html += f'      <h2 id="{hid}">{heading}</h2>\n{content}\n'
    
    ou = f"https://vietnam-japan-guide.com/articles/visa/{slug}.html"
    df = desc.split("。")[0] + "。"
    
    # FAQ schema
    faq_items = []
    if "よくある質問（FAQ）" in [s[0] for s in sections]:
        for s_h, s_c in sections:
            if s_h == "よくある質問（FAQ）":
                qas = re.findall(r"<h3>Q\d+\.\s*([^<]+)</h3>\s*<p>A\.\s*([^<]+)</p>", s_c)
                for q, a in qas:
                    faq_items.append(f'{{"@type":"Question","name":"{q.strip()}","acceptedAnswer":{{"@type":"Answer","text":"{a.strip()}"}}}}')
    faq_schema = ""
    if faq_items:
        faq_schema = '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n' + ",\n".join(faq_items) + "\n]}\n</script>"
    
    bc = '{"@type":"ListItem","position":3,"name":"' + hl + '","item":"' + ou + '"}'
    
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{t} | Vietnam Japan Guide</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index,follow">
  <meta property="og:title" content="{t}"><meta property="og:description" content="{desc}">
  <meta property="og:type" content="article"><meta property="og:url" content="{ou}">
  <link rel="canonical" href="{ou}"><link rel="stylesheet" href="../../css/style.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{hl}","description":"{df}","datePublished":"{today}","dateModified":"{today}","author":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"publisher":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"inLanguage":"ja"}}</script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"トップページ","item":"https://vietnam-japan-guide.com/"}},{{"@type":"ListItem","position":2,"name":"ビザ・在留資格","item":"https://vietnam-japan-guide.com/pages/visa.html"}},{bc}]}}</script>
  {faq_schema}
</head>
<body>
  <header class="header" role="banner">
    <div class="header__inner">
      <a href="/" class="header__logo" aria-label="Vietnam Japan Guide - トップページ">
        <span class="header__logo-icon" aria-hidden="true">VN</span>
        <span>Vietnam Japan Guide</span>
      </a>
      <nav class="header__nav" role="navigation" aria-label="メインナビゲーション">
        <ul class="header__nav-list">
{nav_h}        </ul>
      </nav>
      <button class="header__menu-toggle" aria-label="メニュー" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </header>
  <nav class="breadcrumb"><div class="container"><ol class="breadcrumb__list">
    <li class="breadcrumb__item"><a href="/">トップページ</a></li>
    <li class="breadcrumb__item"><a href="/pages/visa.html">ビザ・在留資格</a></li>
    <li class="breadcrumb__item breadcrumb__item--current">{hl}</li>
  </ol></div></nav>
  <article class="article-content"><div class="container">
    <h1>{hl}</h1>
    <div class="info-box info-box--warning"><div class="info-box__title">&#x26a0;&#xfe0f; おことわり</div><p>この記事は公的機関の公式情報をもとに解説しています。法律専門家ではないため、正確な判断は専門家にご確認ください。</p></div>
    <div class="info-box"><div class="info-box__title">&#x1f4dd; この記事のポイント</div><p>{desc}</p></div>
    <div class="toc"><div class="toc__title">&#x1f4d1; 目次</div><ul class="toc__list">
{toc_items}        </ul></div>
    {sections_html}
    <div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4de; 行政書士に相談しませんか？</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">初回無料相談対応の行政書士がサポートします。</p><a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">行政書士を探す &#x2192;</a></div>
  </div></article>
  <footer class="footer"><div class="footer__grid">
    <div><h4>当サイトについて</h4><p>在日ベトナム人のための生活総合情報サイト。</p></div>
    <div><h4>カテゴリー</h4><ul class="footer__links">
      <li><a href="/pages/jobs.html">転職・求人</a></li><li><a href="/pages/visa.html">ビザ・更新</a></li>
      <li><a href="/pages/sinh-hoat.html">生活・行政</a></li><li><a href="/pages/cong-viec.html">仕事・金融</a></li>
      <li><a href="/pages/telecom.html">通信・SIM</a></li><li><a href="/pages/estate.html">不動産・住まい</a></li>
      <li><a href="/pages/chuyen-gia.html">専門家相談</a></li></ul></div>
  </div><div class="footer__bottom"><p>&copy; 2026 Vietnam Japan Guide</p></div></footer>
  <button class="back-to-top">&uarr;</button><script src="../../js/main.js" defer></script>
</body>
</html>'''

# Just one for now to test
slug = "freelance-visa-note"
data = get_content(slug)
if data:
    html = gen_html(slug, data)
    html = html.replace("{{", "{").replace("}}", "}")
    fp = os.path.join(BASE, "articles", "visa", f"{slug}.html")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(html)
    lines = len(html.split("\n"))
    print(f"[1/1] {slug} -> {lines}行")
    print("Done!")
else:
    print("No content found")