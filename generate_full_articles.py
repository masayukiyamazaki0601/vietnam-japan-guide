#!/usr/bin/env python3
"""
スケルトン記事をSEO最適化された本記事に変換するスクリプト
"""
import os
import re
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Article content definitions
ARTICLES = {
    "visa-skeleton-01": {
        "title": "特定技能から技人国ビザへ変更する条件｜在日ベトナム人向け完全ガイド",
        "meta_desc": "特定技能1号から技人国（技術・人文知識・国際業務）ビザへの変更条件を徹底解説。必要書類、学歴要件、実務経験、審査期間、成功率アップのポイントまで網羅。出入国在留管理庁の基準に基づいてわかりやすく説明します。",
        "meta_keywords": "特定技能,技人国ビザ,在留資格変更,特定技能1号,技術人文知識国際業務,キャリアアップ,入管手続き",
        "category_name": "ビザ・更新",
        "category_url": "/pages/visa.html",
        "content_sections": {
            "変更の基本条件": """
<p>特定技能1号から技人国（技術・人文知識・国際業務）ビザへの在留資格変更は、多くの在日ベトナム人にとってキャリアアップの重要な選択肢です。ここでは、出入国在留管理庁の審査基準に基づいて、変更に必要な基本条件を詳しく解説します。</p>

<h3>学歴要件</h3>
<p>技人国ビザを取得するためには、原則として以下のいずれかの学歴要件を満たす必要があります：</p>
<ul>
  <li><strong>大学卒業</strong>：日本の大学、またはベトナムの大学で「技術」または「人文知識」に関連する分野を専攻し卒業していること</li>
  <li><strong>短期大学・専門学校卒業</strong>：日本の短期大学または専門学校を卒業し、「技術」または「人文知識」に関する専門知識を習得していること</li>
  <li><strong>実務経験</strong>：大学卒業でない場合でも、関連分野での実務経験が10年以上あれば申請可能なケースがあります</li>
</ul>

<h3>職務内容との一致</h3>
<p>現在の職務内容が、技人国ビザで認められる業務範囲と一致している必要があります。</p>
<ul>
  <li><strong>技術（エンジニア）</strong>：ソフトウェア開発、機械設計、品質管理、IT関連業務など</li>
  <li><strong>人文知識</strong>：通訳・翻訳、営業、マーケティング、経理、人事など</li>
  <li><strong>国際業務</strong>：国際取引、海外事業開発、ベトナム語を活かした業務など</li>
</ul>

<h3>雇用契約の安定性</h3>
<p>変更後の雇用契約が安定していることも重要な審査ポイントです。</p>
<ul>
  <li>雇用期間が無期または1年以上の有期契約であること</li>
  <li>給与が日本人と同等以上であること（目安：月額20万円以上）</li>
  <li>社会保険（健康保険・厚生年金）に加入していること</li>
  <li>雇用先の企業が安定した経営状況であること</li>
</ul>
""",
            "必要書類一覧": """
<p>特定技能から技人国ビザへの変更申請に必要な書類を一覧で紹介します。事前にすべて準備しておくことで、申請をスムーズに進められます。</p>

<h3>申請者本人が準備する書類</h3>
<table>
  <thead>
    <tr><th>書類名</th><th>取得先・備考</th></tr>
  </thead>
  <tbody>
    <tr><td>在留資格変更許可申請書</td><td>出入国在留管理庁の公式サイトからダウンロード</td></tr>
    <tr><td>写真（縦4cm×横3cm）</td><td>1枚、申請前3ヶ月以内に撮影</td></tr>
    <tr><td>パスポート</td><td>原本と写し</td></tr>
    <tr><td>在留カード</td><td>原本と写し（両面）</td></tr>
    <tr><td>卒業証明書</td><td>大学・専門学校から取得</td></tr>
    <tr><td>成績証明書</td><td>大学・専門学校から取得</td></tr>
    <tr><td>履歴書</td><td>学歴・職歴を詳細に記載</td></tr>
  </tbody>
</table>

<h3>雇用先（企業）が準備する書類</h3>
<table>
  <thead>
    <tr><th>書類名</th><th>備考</th></tr>
  </thead>
  <tbody>
    <tr><td>雇用契約書</td><td>職務内容、給与、勤務時間が明記されているもの</td></tr>
    <tr><td>雇用理由書</td><td>なぜ外国人を雇用する必要があるかの説明</td></tr>
    <tr><td>会社の登記簿謄本</td><td>履歴事項全部証明書</td></tr>
    <tr><td>会社の決算報告書</td><td>直近年度の損益計算書など</td></tr>
    <tr><td>従業員名簿</td><td>日本人従業員と外国人従業員の一覧</td></tr>
    <tr><td>労働条件通知書</td><td>雇用条件を明示した書類</td></tr>
  </tbody>
</table>

<p>※ 書類は原本と写しの両方を準備し、写しはA4サイズで提出します。ベトナムの大学を卒業した場合は、卒業証明書の日本語訳も必要です。</p>
""",
            "審査期間の目安": """
<p>特定技能から技人国ビザへの変更審査期間は、通常以下の通りです。</p>

<h3>標準的な審査期間</h3>
<ul>
  <li><strong>東京入国管理局</strong>：申請から許可まで約1〜3ヶ月</li>
  <li><strong>大阪入国管理局</strong>：約1〜2ヶ月</li>
  <li><strong>その他の地方入国管理局</strong>：約2週間〜1ヶ月</li>
</ul>

<h3>審査に影響する要因</h3>
<ul>
  <li>書類に不備があると審査期間が延びる</li>
  <li>追加資料の提出を求められる場合がある（申請から1〜2週間後に通知）</li>
  <li>繁忙期（卒業シーズンの3月〜4月、入社シーズンの4月〜5月）は審査が混み合う</li>
  <li>企業の財務状況や事業内容によっては追加調査が入ることもある</li>
</ul>

<p>審査中も現在の特定技能ビザの有効期間内であれば、引き続き就労可能です。変更許可が下りるまでは、特定技能の範囲内での業務のみ行ってください。</p>
""",
            "注意点とリスク": """
<p>特定技能から技人国ビザへの変更には、いくつかの注意点とリスクがあります。事前に理解しておくことで、不許可のリスクを減らせます。</p>

<h3>主な不許可リスク</h3>
<ul>
  <li><strong>職務内容の不一致</strong>：現在の業務内容が技人国ビザの対象範囲と一致しない場合、不許可となる可能性が高い</li>
  <li><strong>学歴要件を満たしていない</strong>：大学卒業でなく、実務経験も不十分な場合は不許可</li>
  <li><strong>企業の経営状況</strong>：雇用先が赤字続きや小規模すぎる場合、安定性が疑問視される</li>
  <li><strong>給与が低すぎる</strong>：日本人と同等以上の給与でない場合</li>
</ul>

<h3>変更中の注意点</h3>
<ul>
  <li>審査中は現在の特定技能ビザの範囲内でのみ就労可能</li>
  <li>審査中に転職すると申請がやり直しになる</li>
  <li>不許可の場合、特定技能ビザの残存期間内であれば継続就労は可能</li>
  <li>不許可後に再度申請する場合は、不許可理由を改善してから申請すること</li>
</ul>
""",
            "行政書士に相談すべきケース": """
<p>以下のようなケースでは、行政書士に相談することを強くおすすめします。</p>

<ul>
  <li><strong>学歴要件を満たしていないが実務経験で申請したい</strong>：10年の実務経験の証明方法や職務経歴書の書き方に専門知識が必要</li>
  <li><strong>職務内容が技人国の範囲に合っているか不安</strong>：業務内容のどの部分が該当するかの判断に専門性が必要</li>
  <li><strong>過去にビザの不許可歴がある</strong>：不許可理由を分析し、改善策を立てるのに専門家の助言が有効</li>
  <li><strong>雇用先の企業が初めて外国人を雇う</strong>：企業側の書類準備にサポートが必要なケースが多い</li>
  <li><strong>審査期間をできるだけ短縮したい</strong>：書類の完全性を高めることで、追加資料提出を防げる</li>
</ul>

<p>行政書士への依頼費用は、申請書類の作成代行で5万円〜10万円程度が相場です。成功率を上げるための投資として検討する価値があります。</p>

<p><a href="/articles/vinh-tru/cach-chon-gyoseishoshi.html">行政書士の選び方についてはこちらの記事</a>もご覧ください。</p>
""",
            "よくある質問（FAQ）": """
<h3>Q1. 特定技能1号から技人国に変わると、在留期間はどうなりますか？</h3>
<p>A. 技人国ビザの在留期間は「3ヶ月」「1年」「3年」「5年」のいずれかが付与されます。特定技能1号の最長5年よりも短くなる場合もありますが、更新が可能です。</p>

<h3>Q2. 特定技能2号からも変更できますか？</h3>
<p>A. 特定技能2号から技人国への変更も可能です。特定技能2号は2023年に開始された制度で、該当するのは一部の職種のみですが、要件を満たせば変更できます。</p>

<h3>Q3. 変更許可が下りるまで現在の仕事は続けられますか？</h3>
<p>A. はい、現在の特定技能ビザの有効期間内であれば、特定技能の範囲内で就労を継続できます。</p>

<h3>Q4. 不許可になった場合、すぐに再申請できますか？</h3>
<p>A. 再申請自体は可能ですが、不許可理由を十分に改善せずに再申請すると、再度不許可となる可能性が高いです。必ず不許可理由を確認し、改善してから申請しましょう。</p>

<h3>Q5. 日本語能力は必要ですか？</h3>
<p>A. 技人国ビザに明確な日本語能力要件はありませんが、業務で日本語を使用する場合は、N2以上が望ましいとされます。実務で日本語ができないと業務に支障が出ると判断された場合、不許可理由になり得ます。</p>
""",
        }
    },
    "visa-skeleton-02": {
        "title": "特定技能ビザの更新と試験の受け方｜完全ガイド",
        "meta_desc": "特定技能ビザ（1号・2号）の更新条件、必要書類、スケジュールを徹底解説。特定技能評価試験の種類、受験方法、合格ラインまで網羅。出入国在留管理庁の最新基準に基づいて解説します。",
        "meta_keywords": "特定技能ビザ,更新,試験,特定技能1号,特定技能2号,評価試験,技能測定試験,日本語試験",
        "category_name": "ビザ・更新",
        "category_url": "/pages/visa.html",
        "content_sections": {
            "特定技能ビザ更新の基本条件": """
<p>特定技能ビザ（1号・2号）の更新は、在留期間の満了前に適切な手続きを行うことで在留を継続できます。ここでは更新の基本条件を解説します。</p>

<h3>特定技能1号の更新条件</h3>
<ul>
  <li><strong>在留期間の更新申請</strong>：在留期間満了の3ヶ月前から申請可能</li>
  <li><strong>契約の継続</strong>：受け入れ機関（雇用先）との契約が継続していること</li>
  <li><strong>報酬の安定性</strong>：日本人と同等以上の報酬が支払われていること</li>
  <li><strong>技能水準の維持</strong>：従事する業務に必要な技能を有していること</li>
</ul>

<h3>特定技能2号の更新条件</h3>
<ul>
  <li>特定技能1号からの移行後、さらに高度な技能を要する業務に従事していること</li>
  <li>試験合格または技能検定の合格が条件（職種により異なる）</li>
  <li>在留期間の上限がなく、無期での更新が可能</li>
</ul>
""",
            "必要書類一覧": """
<p>特定技能ビザの更新申請に必要な書類は以下の通りです。</p>

<h3>基本書類</h3>
<table>
  <thead>
    <tr><th>書類名</th><th>備考</th></tr>
  </thead>
  <tbody>
    <tr><td>在留期間更新許可申請書</td><td>出入国在留管理庁サイトから取得</td></tr>
    <tr><td>写真（縦4cm×横3cm）</td><td>1枚</td></tr>
    <tr><td>パスポート</td><td>原本と写し</td></tr>
    <tr><td>在留カード</td><td>原本と写し（両面）</td></tr>
    <tr><td>特定技能契約書の写し</td><td>雇用契約書</td></tr>
    <tr><td>特定技能支援計画書の写し</td><td>支援機関が作成</td></tr>
  </tbody>
</table>

<h3>雇用先が準備する書類</h3>
<ul>
  <li>法定調書合計表（写し）</li>
  <li>源泉徴収票などの給与所得の証明書類</li>
  <li>社会保険の加入証明書類</li>
  <li>会社の登記簿謄本（法人の場合）</li>
</ul>
""",
            "特定技能評価試験の種類と受け方": """
<p>特定技能ビザを取得・更新するためには、職種に応じた試験に合格する必要があります。</p>

<h3>試験の種類</h3>
<ul>
  <li><strong>特定技能1号評価試験</strong>：各職種ごとに実施される技能試験</li>
  <li><strong>日本語試験</strong>：日本語能力試験（JLPT）N4以上、または国際交流基金日本語基礎テスト</li>
</ul>

<h3>主な職種と試験</h3>
<table>
  <thead>
    <tr><th>職種</th><th>必要な試験</th></tr>
  </thead>
  <tbody>
    <tr><td>介護</td><td>介護日本語評価試験＋介護技能評価試験</td></tr>
    <tr><td>ビルクリーニング</td><td>ビルクリーニング技能評価試験</td></tr>
    <tr><td>素形材産業</td><td>素形材産業技能評価試験</td></tr>
    <tr><td>産業機械製造業</td><td>産業機械製造業技能評価試験</td></tr>
    <tr><td>電気・電子情報関連産業</td><td>電気・電子情報関連産業技能評価試験</td></tr>
    <tr><td>建設</td><td>建設技能評価試験</td></tr>
    <tr><td>造船・舶用工業</td><td>造船・舶用工業技能評価試験</td></tr>
    <tr><td>自動車整備</td><td>自動車整備技能評価試験</td></tr>
    <tr><td>航空</td><td>航空技能評価試験</td></tr>
    <tr><td>宿泊</td><td>宿泊技能評価試験</td></tr>
    <tr><td>農業</td><td>農業技能評価試験</td></tr>
    <tr><td>漁業</td><td>漁業技能評価試験</td></tr>
    <tr><td>飲食料品製造業</td><td>飲食料品製造業技能評価試験</td></tr>
    <tr><td>外食業</td><td>外食業技能評価試験</td></tr>
  </tbody>
</table>

<h3>試験の申込み方法</h3>
<p>各試験は、一般社団法人各業界団体が実施しています。試験日程や申込み方法は、各団体の公式サイトで確認できます。試験は全国主要都市で定期的に開催されています。</p>
""",
            "更新手続きのスケジュールと注意点": """
<p>特定技能ビザの更新手続きは、余裕を持って計画的に進めることが重要です。</p>

<h3>推奨スケジュール</h3>
<ul>
  <li><strong>在留期間満了の6ヶ月前</strong>：更新に必要な書類の準備開始</li>
  <li><strong>満了の3〜4ヶ月前</strong>：雇用先に更新の意向を確認、書類依頼</li>
  <li><strong>満了の2〜3ヶ月前</strong>：入国管理局に申請</li>
  <li><strong>満了の1ヶ月前</strong>：審査状況の確認</li>
  <li><strong>満了日</strong>：期限切れまでに許可を得る</li>
</ul>

<h3>注意点</h3>
<ul>
  <li>在留期間が切れると不法滞在となるため、必ず期限内に申請すること</li>
  <li>申請中（審査中）で在留期間が切れた場合でも、審査中は在留が認められる（法定特別在籍者）</li>
  <li>更新申請中に転職する場合は、新しい雇用先との契約書類も提出する必要がある</li>
  <li>試験の有効期限に注意（合格から一定期間内に申請する必要がある場合もある）</li>
</ul>
""",
            "よくある質問（FAQ）": """
<h3>Q1. 特定技能ビザの更新は何回でもできますか？</h3>
<p>A. 特定技能1号は通算で最長5年までです。ただし、特定技能2号に移行すれば期間の制限なく更新可能です。</p>

<h3>Q2. 更新時に日本語試験は必要ですか？</h3>
<p>A. すでに合格している場合は不要ですが、初回申請時に日本語試験に合格していなかった場合は、更新時までに合格する必要があります。</p>

<h3>Q3. 転職した場合も特定技能ビザは更新できますか？</h3>
<p>A. 同じ職種区分内であれば転職先でも更新可能です。ただし、新しい雇用先との契約書類が必要です。</p>

<h3>Q4. 更新不許可になる原因は？</h3>
<p>A. 主な原因は、収入が日本人と同等でない、社会保険未加入、技能水準を満たしていない、などです。</p>
""",
        }
    },
}


def fix_breadcrumb(html, category_name, category_url, article_name):
    """Fix breadcrumb with proper category link"""
    pattern = r'(<li class="breadcrumb__item"><a href="/">トップページ</a></li>\s*<li class="breadcrumb__item") breadcrumb__item--current(">.*?</li>)'
    replacement = r'\1><a href="' + category_url + r'">' + category_name + r'</a></li>\n        <li class="breadcrumb__item breadcrumb__item--current">' + article_name + r'</li>'
    return re.sub(pattern, replacement, html)


def make_html(title, meta_desc, meta_keywords, category_name, category_url,
              slug, toc_items, sections_html, faq_schema, og_url, canonical):
    """Build final HTML"""
    today = datetime.now().strftime("%Y-%m-%d")
    headline = title.split('｜')[0]

    # Active nav
    if 'life' in slug:
        active_idx = 2
    elif 'visa' in slug:
        active_idx = 1
    elif 'vinh-tru' in slug:
        active_idx = 0
    else:
        active_idx = -1

    nav_links = [
        ('/pages/vinh-tru.html', '永住・帰化'),
        ('/pages/visa.html', 'ビザ・更新'),
        ('/pages/sinh-hoat.html', '生活・行政'),
        ('/pages/cong-viec.html', '仕事・金融'),
        ('/pages/chuyen-gia.html', '専門家相談'),
    ]

    nav_html = ''
    for i, (url, label) in enumerate(nav_links):
        active_attr = ' header__nav-link--active' if i == active_idx else ''
        nav_html += f'          <li><a href="{url}" class="header__nav-link{active_attr}">{label}</a></li>\n'

    article_schema = '''{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "''' + headline + '''",
    "description": "''' + meta_desc.split('。')[0] + '''。",
    "datePublished": "''' + today + '''",
    "dateModified": "''' + today + '''",
    "author": {"@type": "Organization", "name": "Vietnam Japan Guide"},
    "publisher": {"@type": "Organization", "name": "Vietnam Japan Guide"},
    "inLanguage": "ja"
  }'''

    breadcrumb_schema = '''{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "トップページ", "item": "https://vietnam-japan-guide.com/"},
      {"@type": "ListItem", "position": 2, "name": "''' + category_name + '''", "item": "https://vietnam-japan-guide.com''' + category_url + '''"},
      {"@type": "ListItem", "position": 3, "name": "''' + headline + '''", "item": "''' + og_url + '''"}
    ]
  }'''

    html = '''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>''' + title + ''' | Vietnam Japan Guide</title>
  <meta name="description" content="''' + meta_desc + '''">
  <meta name="keywords" content="''' + meta_keywords + '''">
  <meta name="robots" content="index, follow">
  <meta property="og:title" content="''' + title + '''">
  <meta property="og:description" content="''' + meta_desc + '''">
  <meta property="og:type" content="article">
  <meta property="og:url" content="''' + og_url + '''">
  <link rel="canonical" href="''' + canonical + '''">
  <link rel="stylesheet" href="../../css/style.css">
  <script type="application/ld+json">
  ''' + article_schema + '''
  </script>
  <script type="application/ld+json">
  ''' + breadcrumb_schema + '''
  </script>
  ''' + faq_schema + '''
</head>
<body>
  <header class="header" role="banner">
    <div class="header__inner">
      <a href="/" class="header__logo"><span class="header__logo-icon" aria-hidden="true">VN</span>Vietnam Japan Guide</a>
      <nav class="header__nav">
        <ul class="header__nav-list">
''' + nav_html + '''        </ul>
      </nav>
      <button class="header__menu-toggle" aria-label="メニュー"><span></span><span></span><span></span></button>
    </div>
  </header>

  <nav class="breadcrumb">
    <div class="container">
      <ol class="breadcrumb__list">
        <li class="breadcrumb__item"><a href="/">トップページ</a></li>
        <li class="breadcrumb__item"><a href="''' + category_url + '''">''' + category_name + '''</a></li>
        <li class="breadcrumb__item breadcrumb__item--current">''' + headline + '''</li>
      </ol>
    </div>
  </nav>

  <article class="article-content">
    <div class="container">
      <h1>''' + headline + '''</h1>
      <div class="info-box info-box--warning">
        <div class="info-box__title">&#x26a0;&#xfe0f; おことわり</div>
        <p>この記事は、出入国在留管理庁などの公的機関が公開している公式情報をもとに解説しています。当サイトは法律専門家ではなく、正確な判断が必要な場合は必ず出入国在留管理庁または行政書士・弁護士などの専門家にご確認ください。</p>
      </div>
      <div class="info-box">
        <div class="info-box__title"><span class="icon">&#x1f4dd;</span> この記事のポイント</div>
        <p>''' + meta_desc + '''</p>
      </div>

      <div class="toc">
        <div class="toc__title">&#x1f4d1; 目次</div>
        <ul class="toc__list">
''' + toc_items + '''        </ul>
      </div>

''' + sections_html + '''
      <div style="background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%); padding: var(--space-xl); border-radius: var(--radius-lg); text-align: center; margin-top: var(--space-2xl);">
        <h3 style="color:white; margin-bottom:var(--space-md);">&#x1f4de; 専門家に相談しませんか？</h3>
        <p style="color:rgba(255,255,255,0.9); margin-bottom:var(--space-lg);">初回無料相談対応の行政書士があなたのケースをサポートします。</p>
        <a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">行政書士に相談 &#x2192;</a>
      </div>
    </div>
  </article>

  <footer class="footer"><div class="footer__grid">
    <div><h4 class="footer__section-title">当サイトについて</h4><p style="font-size:var(--fs-sm);">在日ベトナム人のための生活総合情報サイト。ビザ、永住権、日常生活の手続きをわかりやすく解説します。</p></div>
    <div><h4 class="footer__section-title">カテゴリー</h4><ul class="footer__links">
      <li><a href="/pages/vinh-tru.html">永住権・帰化</a></li><li><a href="/pages/visa.html">ビザ・更新</a></li>
      <li><a href="/pages/sinh-hoat.html">生活・行政</a></li><li><a href="/pages/cong-viec.html">仕事・金融</a></li>
      <li><a href="/pages/chuyen-gia.html">専門家相談</a></li>
    </ul></div>
  </div><div class="footer__bottom"><p>※ 当サイトは法律専門家ではありません。記載内容は参考情報であり、正確な判断については出入国在留管理庁または行政書士にご確認ください。</p><p>&copy; 2026 Vietnam Japan Guide</p></div></footer>
  <button class="back-to-top" aria-label="トップに戻る">&uarr;</button>
  <script src="../../js/main.js" defer></script>
</body>
</html>'''
    return html


def generate_article_html(slug, article_data):
    """Generate full HTML for an article"""
    title = article_data["title"]
    meta_desc = article_data["meta_desc"]
    meta_keywords = article_data["meta_keywords"]
    category_name = article_data["category_name"]
    category_url = article_data["category_url"]
    og_url = "https://vietnam-japan-guide.com/articles/" + ("visa/" if "visa" in slug else "sinh-hoat/") + slug + ".html"
    canonical = og_url
    sections = article_data["content_sections"]

    # Build TOC and section HTML
    toc_items = ""
    sections_html = ""
    for i, (heading, content) in enumerate(sections.items(), 1):
        hid = f"s{i}"
        toc_items += f'          <li><a href="#{hid}">{heading}</a></li>\n'
        sections_html += f'      <h2 id="{hid}">{heading}</h2>\n{content}\n'

    # Build FAQ schema
    faq_schema = ""
    if "よくある質問（FAQ）" in sections:
        faq_content = sections["よくある質問（FAQ）"]
        qas = re.findall(r'<h3>(Q\d+[^<]*)</h3>\s*<p>A\.\s*([^<]+)</p>', faq_content)
        if qas:
            items = []
            for q, a in qas:
                items.append(f'{{"@type":"Question","name":"{q.strip()}","acceptedAnswer":{{"@type":"Answer","text":"{a.strip()}"}}}}')
            faq_schema = '<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@type": "FAQPage",\n  "mainEntity": [\n' + ',\n'.join(items) + '\n  ]\n}\n</script>'

    return make_html(title, meta_desc, meta_keywords, category_name, category_url,
                      slug, toc_items, sections_html, faq_schema, og_url, canonical)


def process_articles():
    """Process all article skeletons"""
    for slug, data in ARTICLES.items():
        # Determine file path
        if "visa" in slug:
            filepath = os.path.join(BASE_DIR, "articles", "visa", f"{slug}.html")
        elif "life" in slug:
            filepath = os.path.join(BASE_DIR, "articles", "sinh-hoat", f"{slug}.html")
        else:
            continue

        if not os.path.exists(filepath):
            print(f"SKIP: {filepath} not found")
            continue

        print(f"Processing: {slug}")
        html = generate_article_html(slug, data)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  -> Written to {filepath}")


if __name__ == "__main__":
    process_articles()
    print("\nDone! All articles generated.")