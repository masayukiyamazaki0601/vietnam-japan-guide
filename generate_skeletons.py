#!/usr/bin/env python3
"""Vietnam Japan Guide - スケルトン一括生成スクリプト"""
import os

BASE = "/Users/masayukiyamazaki/Desktop/vietnam-japan-guide"

CTA = """<div style="background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%); padding: var(--space-xl); border-radius: var(--radius-lg); text-align: center; margin-top: var(--space-2xl);">
      <h3 style="color:white; margin-bottom:var(--space-md);">📞 専門家に相談しませんか？</h3>
      <p style="color:rgba(255,255,255,0.9); margin-bottom:var(--space-lg);">初回無料相談対応の行政書士があなたのケースをサポートします。</p>
      <a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">行政書士に相談 →</a>
    </div>"""

FOOTER = """<footer class="footer"><div class="footer__grid">
    <div><h4 class="footer__section-title">当サイトについて</h4><p style="font-size:var(--fs-sm);">Vietnam Japan Guide</p></div>
    <div><h4 class="footer__section-title">カテゴリー</h4><ul class="footer__links">
      <li><a href="/pages/vinh-tru.html">永住権</a></li><li><a href="/pages/visa.html">ビザ</a></li>
      <li><a href="/pages/sinh-hoat.html">生活</a></li><li><a href="/pages/cong-viec.html">仕事</a></li>
      <li><a href="/pages/chuyen-gia.html">専門家</a></li>
    </ul></div>
  </div><div class="footer__bottom"><p>© 2026 Vietnam Japan Guide</p></div></footer>
  <button class="back-to-top">↑</button>
  <script src="/js/main.js" defer></script>
</body>
</html>"""

def bc_text(item):
    """Extract breadcrumb label from item which may be a string or [title, url] list."""
    if isinstance(item, (list, tuple)):
        return item[0]
    return item

def bc_href(item):
    """Extract breadcrumb href from item which may be a string or [title, url] list."""
    if isinstance(item, (list, tuple)):
        return item[1]
    return None

def gen(title, desc, h2s, cat_dir, filename, nav_active, breadcrumb_items):
    nav_links = {
        '1': ('pages/vinh-tru.html', '永住・帰化'),
        '2': ('pages/visa.html', 'ビザ・更新'),
        '3': ('pages/sinh-hoat.html', '生活・行政'),
        '4': ('pages/cong-viec.html', '仕事・金融'),
        '5': ('pages/chuyen-gia.html', '専門家相談'),
    }
    nav_html = ""
    for k, (page, name) in nav_links.items():
        active = ' header__nav-link--active' if k == nav_active else ''
        nav_html += f'      <li><a href="/{page}" class="header__nav-link{active}">{name}</a></li>\n'

    bc_html = ""
    for i, item in enumerate(breadcrumb_items):
        cls = ' breadcrumb__item--current' if i == len(breadcrumb_items)-1 else ''
        if i == 0:
            bc_html += f'        <li class="breadcrumb__item{cls}"><a href="/">{bc_text(item)}</a></li>\n'
        elif i < len(breadcrumb_items) - 1:
            bc_html += f'        <li class="breadcrumb__item{cls}"><a href="{bc_href(item)}">{bc_text(item)}</a></li>\n'
        else:
            # Last item: if it's a tuple, render as text only (no link)
            # If it's a string, render as text
            bc_html += f'        <li class="breadcrumb__item{cls}">{bc_text(item)}</li>\n'

    h2_html = ""
    for i, h in enumerate(h2s):
        h2_html += f'    <h2 id="s{i+1}">{h}</h2>\n'
        h2_html += '    <p>=== このセクションは執筆中です ===</p>\n\n'

    html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Vietnam Japan Guide</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://vietnam-japan-guide.com/{cat_dir}/{filename}">
  <link rel="stylesheet" href="/css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{title}","datePublished":"2026-07-15","author":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"inLanguage":"ja"}}
  </script>
</head>
<body>
  <header class="header"><div class="header__inner">
    <a href="/" class="header__logo"><span class="header__logo-icon" aria-hidden="true">VN</span>Vietnam Japan Guide</a>
    <nav class="header__nav"><ul class="header__nav-list">
{nav_html}    </ul></nav>
    <button class="header__menu-toggle" aria-label="メニュー"><span></span><span></span><span></span></button>
  </div></header>
  <nav class="breadcrumb"><div class="container"><ol class="breadcrumb__list">
{bc_html}  </ol></div></nav>
  <article class="article-content">
    <h1>{title}</h1>
    <div class="info-box"><div class="info-box__title"><span class="icon">📝</span> この記事のポイント</div><p>{desc}</p></div>
    <div class="toc"><div class="toc__title">📑 目次</div><ul class="toc__list"></ul></div>
{h2_html}    {CTA}
  </article>
  {FOOTER}'''

    full_dir = os.path.join(BASE, cat_dir)
    os.makedirs(full_dir, exist_ok=True)
    filepath = os.path.join(full_dir, filename)
    with open(filepath, 'w') as f:
        f.write(html)
    print(f"  Created: {cat_dir}/{filename}")

# ============ 1. 永住・帰化 残りスケルトン (6件) ============
vbc = ['トップページ', ['永住権・帰化','/pages/vinh-tru.html']]
gen('永住申請の審査で「年収」はどう判断されるか','永住権審査における年収の判断基準。安全ライン、配偶者収入の合算、不安定な収入の扱い。',
    ['年収の審査基準とは','安全圏の年収ライン','配偶者収入の合算ルール','不安定な収入と審査への影響','年収証明の方法'],
    'articles/vinh-tru','nenshuu-shinsa-kijun.html','1',vbc)
gen('ベトナム国籍離脱の手続きと必要書類','帰化申請に伴うベトナム国籍離脱の手続き、必要書類、期間、注意点。',
    ['国籍離脱が必要な理由','ベトナム大使館での手続き','必要書類一覧','離脱にかかる期間','離脱後の注意点'],
    'articles/vinh-tru','vietnam-kokuseki-ridatsu.html','1',vbc)
gen('永住申請における扶養控除の計算と注意点','扶養家族がいる場合の永住申請への影響、扶養控除の計算方法、審査での評価。',
    ['扶養控除とは','扶養家族の範囲と条件','扶養控除が永住審査に与える影響','適切な扶養申請の方法','よくあるミスと対策'],
    'articles/vinh-tru','fuyou-koujo-eikyo.html','1',vbc)
gen('永住申請中に転職・退職した場合の対応','永住申請中の転職・退職の影響と必要な手続き。審査への影響を最小限にする方法。',
    ['申請中の転職は可能か','転職時の入管への連絡','退職した場合のリスク','審査への影響を最小限にする方法','行政書士に相談すべきケース'],
    'articles/vinh-tru','tenshoku-taishoku-chu.html','1',vbc)
gen('日本人と結婚して永住権を取るまでの期間','日本人配偶者の永住権申請条件、必要な在留期間（3年+1年）、必要書類。',
    ['婚姻を基にした永住権申請の条件','必要在留期間：3年＋1年','必要書類一覧','審査のポイント','注意点とリスク'],
    'articles/vinh-tru','kekkon-eijyu-kikan.html','1',vbc)
gen('永住権更新は必要？在留カードとの関係','永住権取得後の在留カード7年更新ルール、手続き、更新忘れのリスク。',
    ['永住権に「更新」は必要か','在留カードの7年更新ルール','更新手続きの流れ','更新忘れのリスク','在留カードの住所変更義務'],
    'articles/vinh-tru','eijyu-zairyu-card-kankei.html','1',vbc)

# ============ 2. ビザ スケルトン (13件) ============
vbc2 = ['トップページ', ['ビザ・更新','/pages/visa.html']]
visa_data = [
    ('特定技能から技人国ビザへ変更する条件','キャリアアップのための変更条件、書類、審査期間。',['変更の基本条件','必要書類一覧','審査期間の目安','注意点とリスク','行政書士に相談すべきケース']),
    ('特定技能ビザの更新と試験の受け方','特定技能ビザの更新条件、試験要件、必要書類とスケジュール。',['更新に必要な条件','試験の合格要件','必要書類','更新時期の目安','不許可になるケース']),
    ('家族滞在ビザで配偶者を呼ぶための年収要件','家族滞在ビザの収入要件、必要書類、審査ポイント。',['家族滞在ビザの基本','収入要件の目安','必要書類','審査のポイント','注意点']),
    ('子供が日本で生まれた場合の在留資格取得手続き','出生後の手続き、在留資格取得の条件、必要書類。',['出生後の手続きの流れ','在留資格取得の条件','必要書類','期間と注意点','帰化との関係']),
    ('留学ビザから就労ビザへの変更手続き','留学から就労への在留資格変更の条件と手続き。',['変更の条件','必要書類','就職活動の期間','審査のポイント','不許可リスクと対策']),
    ('技人国ビザで「専攻外」の仕事はできるか','技人国ビザの対象業務範囲と専攻外の仕事が認められる条件。',['技人国ビザの活動範囲','専攻外の仕事が認められる例外','手続き方法','リスクと注意点']),
    ('特定活動（就職活動）ビザの期間と延長ルール','就職活動ビザの基本、延長条件、手続き方法。',['特定活動ビザの基本','就職活動期間','延長条件','必要な手続き','期間切れのリスク']),
    ('ビザ更新時期と期限切れ直前の対応方法','更新スケジュールとギリギリの場合の対応。',['更新申請のスケジュール','3ヶ月前からの受付','ギリギリの場合の対応','更新中の出国ルール']),
    ('追加資料提出通知書が届いた時の対処法','入管からの追加資料請求への迅速な対応方法。',['追加資料の意味','よくある追加資料の種類','迅速な対応方法','行政書士に頼むメリット']),
    ('ビザが不許可になった！すぐにやるべきこと','不許可後の対応、理由分析、再申請の準備。',['不許可通知を受け取ったら','不許可理由の分析','再申請までの期間','行政書士に相談すべきケース']),
    ('再入国許可とみなし再入国許可の違い','出国時の手続き、制限、注意点。',['再入国許可とは','みなし再入国許可との違い','手続き方法','出国期間の制限','違反した場合の影響']),
    ('経営・管理ビザの取得手順と資本金要件','経営管理ビザの条件、資本金500万円要件、事業計画書。',['経営管理ビザの基本条件','資本金500万円要件','事業計画書の書き方','必要書類','審査のポイント']),
    ('技人国ビザで副業・アルバイトは可能か','副業ルール、資格外活動許可、認められる範囲。',['副業のルール','資格外活動許可の取得','副業が認められる範囲','リスクと注意点']),
]
for i, (title, desc, h2s) in enumerate(visa_data):
    fname = f'visa-skeleton-{i+1:02d}.html'
    gen(title, desc, h2s, 'articles/visa', fname, '2', vbc2)

# ============ 3. 生活・行政 スケルトン (10件) ============
vbc3 = ['トップページ', ['生活・行政','/pages/sinh-hoat.html']]
life_data = [
    ('住民票（Juminhyo）の取り方と用途','住民票の取得方法、必要なもの、費用、用途を解説。',
     ['住民票とは','取得方法（窓口・コンビニ）','必要なものと費用','住民票の用途','よくある質問']),
    ('市役所での住所変更手続き完全ガイド','引っ越し時の住所変更手続きを完全ガイド。',
     ['住所変更のタイミング','市役所での手続きの流れ','必要な持ち物','手続き後の注意点','よくあるミス']),
    ('在留カード紛失時の再発行手順','紛失時の警察届出から入管での再発行まで。',
     ['紛失発覚時の対応','警察への遺失届','入管での再発行申請','再発行までの期間','よくある質問']),
    ('課税証明書・納税証明書の取り方','各証明書の取得方法と必要な場面。',
     ['課税証明書とは','納税証明書とは','取得方法と費用','それぞれ必要な場面','注意点']),
    ('マイナンバーカードを作るメリット','マイナンバーカードのメリットと申請手順。',
     ['マイナンバーカードの基本','健康保険証との一体化','申請方法','メリットとデメリット','よくある質問']),
    ('健康保険に加入しないとどうなるか','未加入のリスク、加入義務、罰則。',
     ['健康保険の種類','加入義務と罰則','未加入の場合のリスク','加入手続きの方法','よくある質問']),
    ('年金脱退一時金の申請手順','帰国時の年金一時金受給手続き。',
     ['年金脱退一時金とは','受給条件','申請手順','必要書類','受け取りまでの期間']),
    ('国民健康保険の計算方法と減免制度','保険料計算と減免申請の方法。',
     ['国民健康保険料の計算','保険料の目安','減免制度の条件','申請方法','注意点']),
    ('日本での出産一時金と助成金申請','出産費用、42万円の一時金申請方法。',
     ['出産にかかる費用','出産一時金42万円','直接支払制度','申請手続き','その他の助成金']),
    ('源泉徴収票を会社がくれない時の対策','会社への請求方法と発行されない場合の対処。',
     ['源泉徴収票の重要性','会社に請求する方法','発行されない場合の対策','税務署への相談','どうしても必要な場面']),
]
for i, (title, desc, h2s) in enumerate(life_data):
    fname = f'life-skeleton-{i+1:02d}.html'
    gen(title, desc, h2s, 'articles/sinh-hoat', fname, '3', vbc3)

# ============ 4. 仕事・金融 スケルトン (4件) ============
vbc4 = ['トップページ', ['仕事・金融','/pages/cong-viec.html']]
gen('特定技能の求人探しとおすすめ転職サイト','特定技能ビザ保持者向けの求人探し方法とサイト比較。',
    ['特定技能の求人市場','おすすめ転職サイト比較','求人票の見方','応募時の注意点','面接のコツ'],
    'articles/cong-viec','tokutei-ginou-kyuujin.html','4',vbc4)
gen('技人国ビザの年収基準と手取り額計算','年収基準と社会保険料・税金を差し引いた手取り額の計算。',
    ['年収基準の目安','社会保険料の内訳','手取り額の計算方法','年収アップの方法','よくある質問'],
    'articles/cong-viec','gijinkoku-nenshuu.html','4',vbc4)
gen('日本の給与明細の読み方','給与明細の各項目の意味と読み方を解説。',
    ['給与明細の基本構成','支給項目の説明','控除項目の説明','手取り額の確認方法','よくある疑問'],
    'articles/cong-viec','kyuuryou-meisai-yomikata.html','4',vbc4)
gen('扶養控除で節税する方法','扶養控除の活用方法と永住申請への影響。',
    ['扶養控除の基本','対象となる家族','控除額の計算','申請方法','永住申請との関係'],
    'articles/cong-viec','fuyou-koujo-setsuzei.html','4',vbc4)

# ============ 5. 専門家比較 スケルトン (3件) ============
vbc5 = ['トップページ', ['専門家相談','/pages/chuyen-gia.html']]
gen('永住申請に強い行政書士の見極め方','行政書士選びのチェックポイントと比較方法。',
    ['行政書士選びの重要性','実績の確認方法','料金体系の比較','ベトナム語対応の確認','口コミ・評判の調べ方'],
    'articles/vinh-tru','cach-chon-gyoseishoshi.html','1',['トップページ',['永住権・帰化','/pages/vinh-tru.html'],'行政書士の見極め方'])
gen('成功報酬型と相談料型の違い','行政書士の料金体系を比較。',
    ['2つの料金体系','成功報酬型の特徴','相談料型の特徴','どちらを選ぶべきか','費用の相場'],
    'articles/vinh-tru','so-sanh-chi-phi-gyoseishoshi.html','1',['トップページ',['永住権・帰化','/pages/vinh-tru.html'],'行政書士費用比較'])
gen('行政書士に無料相談前に準備すべきこと','無料相談を最大活用するための事前準備。',
    ['持参すべき書類','質問リストの作成','相談時の注意点','相談後の流れ'],
    'articles/vinh-tru','muryou-soudan-junbi.html','1',['トップページ',['永住権・帰化','/pages/vinh-tru.html'],'無料相談の準備'])

print("\n✅ 全スケルトン生成完了！")