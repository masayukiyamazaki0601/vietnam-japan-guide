#!/usr/bin/env python3
"""カテゴリページに実際の記事ファイルへのリンクを反映"""
import os, re, glob

BASE = os.path.dirname(os.path.abspath(__file__))

# 各カテゴリの記事一覧を取得
CAT_ARTICLES = {}
for cat_dir in ["visa", "vinh-tru", "sinh-hoat", "cong-viec", "jobs", "telecom", "estate"]:
    articles = []
    for f in sorted(glob.glob(os.path.join(BASE, "articles", cat_dir, "*.html"))):
        slug = os.path.basename(f).replace(".html", "")
        if "skeleton" in slug:
            continue
        # Get title
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
            m = re.search(r'<title>([^|]+)', content)
            title = m.group(1).strip() if m else slug
        articles.append((slug, title))
    CAT_ARTICLES[cat_dir] = articles

# カテゴリページのパス
CAT_PAGES = {
    "visa": "pages/visa.html",
    "vinh-tru": "pages/vinh-tru.html",
    "sinh-hoat": "pages/sinh-hoat.html",
    "cong-viec": "pages/cong-viec.html",
    "jobs": "pages/jobs.html",
    "telecom": "pages/telecom.html",
    "estate": "pages/estate.html",
}

def get_nav_html():
    """Generate standard navigation"""
    links = [
        ("/pages/jobs.html", "転職・求人"),
        ("/pages/vinh-tru.html", "永住・帰化"),
        ("/pages/visa.html", "ビザ・更新"),
        ("/pages/sinh-hoat.html", "生活・行政"),
        ("/pages/cong-viec.html", "仕事・金融"),
        ("/pages/telecom.html", "通信・SIM"),
        ("/pages/estate.html", "不動産・住まい"),
        ("/pages/chuyen-gia.html", "専門家相談"),
    ]
    return links

def generate_category_page(cat_key, articles):
    """Generate full category page HTML"""
    page_path = os.path.join(BASE, CAT_PAGES[cat_key])
    
    # Category names
    CAT_NAMES = {
        "visa": ("ビザ・在留資格", "📋", "技人国（エンジニア）、特定技能、家族滞在、経営管理ビザの情報。更新手続き、転職時の入管届出、在留資格変更を詳しく解説。"),
        "vinh-tru": ("永住権・帰化", "🛂", "永住権申請の条件、必要書類、理由書の書き方、年金未納対策など全記事。出入国在留管理庁の最新情報に対応。"),
        "sinh-hoat": ("生活・行政手続き", "🏠", "住民票、納税証明書、マイナンバーカード、健康保険、ゴミ出しルール、日本語学習まで日常生活の手続きを完全ガイド。"),
        "cong-viec": ("仕事・金融", "💼", "転職、社会保険、年金、税金、確定申告、ベトナム送金サービス比較。就職・転職に役立つ情報。"),
        "jobs": ("転職・求人", "💼", "ベトナム人向けの求人サイト、人材紹介会社、転職ノウハウを網羅。ITエンジニアから特定技能まで。"),
        "telecom": ("通信・SIM", "📱", "格安SIM、ポケットWi-Fi、光回線を徹底比較。月額料金・データ容量・通話品質をランキング形式で紹介。"),
        "estate": ("不動産・住まい", "🏠", "保証人不要の賃貸、外国人OKの不動産会社、住宅ローン、初期費用まで徹底解説。"),
    }
    
    name, icon, desc = CAT_NAMES.get(cat_key, (cat_key, "📄", ""))
    
    # Build nav
    nav_links = get_nav_html()
    nav_idx = list(CAT_PAGES.keys()).index(cat_key) if cat_key in CAT_PAGES else 0
    nav_html = ""
    for i, (url, label) in enumerate(nav_links):
        active = " header__nav-link--active" if i == nav_idx else ""
        nav_html += f'          <li><a href="{url}" class="header__nav-link{active}">{label}</a></li>\n'
    
    # Build footer links
    footer_html = ""
    for url, label in nav_links:
        footer_html += f'<li><a href="{url}">{label}</a></li>'
    
    # Build article cards
    articles_html = ""
    for slug, title in articles:
        excerpt = title
        articles_html += f'''        <article class="article-card">
          <div class="article-card__image" aria-hidden="true">{icon}</div>
          <div class="article-card__content">
            <span class="article-card__category">{name}</span>
            <h3 class="article-card__title"><a href="/articles/{cat_key}/{slug}.html">{title}</a></h3>
            <p class="article-card__excerpt">{excerpt}</p>
            <div class="article-card__meta"><span>⏱ 8分</span></div>
          </div>
        </article>\n'''
    
    html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name}｜在日ベトナム人向け情報 | Vietnam Japan Guide</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://vietnam-japan-guide.com/{CAT_PAGES[cat_key]}">
  <link rel="stylesheet" href="../css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {{"@type":"ListItem","position":1,"name":"トップページ","item":"https://vietnam-japan-guide.com/"}},
    {{"@type":"ListItem","position":2,"name":"{name}","item":"https://vietnam-japan-guide.com/{CAT_PAGES[cat_key]}"}}
  ]}}</script>
</head>
<body>
  <header class="header" role="banner">
    <div class="header__inner">
      <a href="/" class="header__logo"><span class="header__logo-icon" aria-hidden="true">VN</span>Vietnam Japan Guide</a>
      <nav class="header__nav"><ul class="header__nav-list">
{nav_html}        </ul></nav>
      <button class="header__menu-toggle" aria-label="メニュー"><span></span><span></span><span></span></button>
    </div>
  </header>
  <nav class="breadcrumb"><div class="container"><ol class="breadcrumb__list">
    <li class="breadcrumb__item"><a href="/">トップページ</a></li>
    <li class="breadcrumb__item breadcrumb__item--current">{name}</li>
  </ol></div></nav>
  <section class="page-header">
    <div class="container">
      <h1 class="page-header__title">{icon} {name}</h1>
      <div class="info-box info-box--warning">
        <div class="info-box__title">⚠️ おことわり</div>
        <p>この記事は、出入国在留管理庁などの公的機関が公開している公式情報をもとに解説しています。当サイトは法律専門家ではなく、正確な判断が必要な場合は必ず専門家にご確認ください。</p>
      </div>
      <p class="page-header__description">{desc}</p>
    </div>
  </section>
  <section class="section section--gray">
    <div class="container">
      <div class="section__title">
        <h2>{name}に関する記事一覧（全{len(articles)}記事）</h2>
      </div>
      <div class="articles-grid">
{articles_html}      </div>
    </div>
  </section>
  <section class="cta-section">
    <div class="container">
      <h2>📞 専門家に相談しませんか？</h2>
      <p>初回無料相談対応の行政書士があなたのケースをサポートします。</p>
      <a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">専門家を探す →</a>
    </div>
  </section>
  <footer class="footer"><div class="footer__grid">
    <div><h4 class="footer__section-title">当サイトについて</h4><p style="font-size:var(--fs-sm);">在日ベトナム人のための生活総合情報サイト。</p></div>
    <div><h4 class="footer__section-title">カテゴリー</h4><ul class="footer__links">{footer_html}</ul></div>
  </div><div class="footer__bottom"><p>※ 当サイトは法律専門家ではありません。正確な判断は専門家にご確認ください。</p><p>© 2026 Vietnam Japan Guide</p></div></footer>
  <button class="back-to-top" aria-label="トップに戻る">↑</button>
  <script src="../js/main.js" defer></script>
</body>
</html>'''
    
    return html.replace("{{", "{").replace("}}", "}")

# Update all category pages
for cat_key, page_file in CAT_PAGES.items():
    articles = CAT_ARTICLES[cat_key]
    html = generate_category_page(cat_key, articles)
    filepath = os.path.join(BASE, page_file)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {page_file} with {len(articles)} articles")

print("Done! All category pages updated.")