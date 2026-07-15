#!/usr/bin/env python3
"""Vietnam Japan Guide - スケルトン追加生成 バッチ2"""
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
    if isinstance(item, (list, tuple)):
        return item[0]
    return item

def bc_href(item):
    if isinstance(item, (list, tuple)):
        return item[1]
    return None

def gen(title, desc, h2s, cat_dir, filename, nav_active, breadcrumb_items):
    nav_links = {'1': ('pages/vinh-tru.html', '永住・帰化'),'2': ('pages/visa.html', 'ビザ・更新'),'3': ('pages/sinh-hoat.html', '生活・行政'),'4': ('pages/cong-viec.html', '仕事・金融'),'5': ('pages/chuyen-gia.html', '専門家相談')}
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
            bc_html += f'        <li class="breadcrumb__item{cls}">{bc_text(item)}</li>\n'
    h2_html = ""
    for i, h in enumerate(h2s):
        h2_html += f'    <h2 id="s{i+1}">{h}</h2>\n    <p>=== このセクションは執筆中です ===</p>\n\n'

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
    with open(os.path.join(full_dir, filename), 'w') as f:
        f.write(html)
    print(f"  Created: {cat_dir}/{filename}")

vb = ['トップページ', ['永住権・帰化','/pages/vinh-tru.html']]

# ===== 永住・帰化 追加 =====
gen('永住申請の審査で「素行善良要件」はどう判断されるか','素行善良要件の審査基準、犯罪歴・交通違反・納税状況が与える影響。',
    ['素行善良要件とは','審査で確認される事項','軽微な違反の申告方法','改善の証明方法','よくある質問'],
    'articles/vinh-tru','sokou-zenryo-yoken.html','1',vb)
gen('永住申請における交通違反（軽微なもの）の申告方法','軽微な交通違反の申告要否、記載方法、審査影響を解説。',
    ['交通違反の申告は必要か','軽微な違反の判断基準','申請書への記載方法','違反歴がある場合の理由書','まとめ'],
    'articles/vinh-tru','koutsuu-ihan-shinkoku.html','1',vb)
gen('永住申請書「理由書」で強調すべき自己アピールポイント','許可率を上げる理由書の書き方、強調すべきポイントと具体例。',
    ['理由書の役割','強調すべき3つのポイント','具体的な記載例','避けるべき表現','チェックリスト'],
    'articles/vinh-tru','riyu-sho-apiru-point.html','1',vb)
gen('永住権保持者が海外に長期間出国する場合の「みなし再入国」','みなし再入国許可のルール、1年ルール、手続き方法を解説。',
    ['みなし再入国許可とは','1年ルールの詳細','出国前の手続き','期間超過時の対応','再入国許可との違い'],
    'articles/vinh-tru','minashi-sainyukoku.html','1',vb)
gen('永住許可取得後の手続き（市区町村への届出など）','永住権取得後に市区町村で行うべき手続きを完全ガイド。',
    ['永住権取得後の流れ','市区町村での手続き','在留カードの受け取り','住所変更の徹底','その他の注意点'],
    'articles/vinh-tru','eijyu-go-tetsuzuki.html','1',vb)
gen('帰化申請における面接対策と想定質問リスト','帰化申請の面接で聞かれる質問と対策。日本語の確認事項。',
    ['面接の目的','想定質問リスト','回答のポイント','面接時の注意点','不合格になる回答例'],
    'articles/vinh-tru','kika-mensetsu-taisaku.html','1',vb)
gen('帰化許可後の戸籍作成とベトナム名の扱い','帰化後の戸籍作成手順、姓・名の扱い、通称使用のルール。',
    ['帰化許可後の流れ','戸籍作成の手続き','氏名の決め方','通称使用の可否','まとめ'],
    'articles/vinh-tru','kika-koseki-sakusei.html','1',vb)
gen('永住者・帰化者が親を「定着者」として呼び寄せる条件','親を日本に呼び寄せる「定住者」ビザの条件と手続き。',
    ['定住者ビザとは','親の呼び寄せ条件','必要書類','審査のポイント','注意点とリスク'],
    'articles/vinh-tru','teijusha-oyobi-yose.html','1',vb)
gen('過去のビザ不許可歴は永住申請にどう影響するか','過去の不許可歴の影響範囲と、申告方法、理由書での説明。',
    ['不許可歴の影響','申告は必要か','理由書での説明方法','改善の証明','まとめ'],
    'articles/vinh-tru','fukyoka-reki-eikyo.html','1',vb)
gen('永住申請の必要書類「理由書」を自分で書くべきか？','理由書の自己作成と専門家依頼の比較、判断基準。',
    ['理由書の重要性','自分で書くメリット・デメリット','専門家に依頼するメリット','ケース別判断基準','費用対効果'],
    'articles/vinh-tru','riyu-sho-jibun-ka.html','1',vb)
gen('永住権が取り消されるケース（再入国許可切れなど）','永住権取消しの条件、再入国許可切れ、犯罪、虚偽申請など。',
    ['永住権取消しの要件','再入国許可切れのリスク','犯罪による取消し','取消しを防ぐ方法','まとめ'],
    'articles/vinh-tru','eijyu-torikeshi.html','1',vb)
gen('永住権保持者が離婚した場合、永住権はどうなる？','離婚後の永住権への影響と必要な手続き。',
    ['離婚と永住権の関係','離婚後の手続き','影響が出るケース','再申請の必要性','まとめ'],
    'articles/vinh-tru','rikon-go-eijyu-ken.html','1',vb)
gen('永住申請のために扶養家族を減らす際の注意点','扶養家族削減の判断基準、手続き、永住審査への影響。',
    ['扶養家族と永住審査','扶養を外す条件','手続き方法','審査への影響','注意点'],
    'articles/vinh-tru','fuyou-kazoku-gerasu.html','1',vb)
gen('永住申請における公的義務（税金・年金・保険）履行の重要性','公的義務の履行が永住審査でどう評価されるか。',
    ['公的義務とは','審査での評価基準','未納がある場合の影響','改善方法','まとめ'],
    'articles/vinh-tru','kouteki-gimu-juushi.html','1',vb)

# ===== 就労・キャリア（7件：高度専門職・特定技能・ITなど）=====
vb2 = ['トップページ', ['ビザ・更新','/pages/visa.html']]
gen('「高度専門職」ビザと「技人国」ビザの比較','高度専門職ビザと技人国ビザの違い、メリット・デメリットを比較。',
    ['2つのビザの概要','ポイント制の解説','技人国との違い','どちらを選ぶべきか','申請のコツ'],
    'articles/visa','kodo-senmonshoku-hikaku.html','2',vb2)
gen('高度専門職ポイント計算シミュレーションの解説','高度専門職ビザのポイント計算方法と加点項目の解説。',
    ['ポイント計算の基本','学歴ポイント','職歴ポイント','年収ポイント','加点項目と合計例'],
    'articles/visa','kodo-point-simulation.html','2',vb2)
gen('技人国ビザでの「特定活動（インターンシップ）」とは','インターンシップでの特定活動ビザの条件と手続き。',
    ['特定活動（インターンシップ）とは','対象となる活動','申請条件','必要書類','注意点'],
    'articles/visa','gijinkoku-internship.html','2',vb2)
gen('技能実習から特定技能への移行に伴う試験対策','技能実習から特定技能1号への移行条件と試験対策。',
    ['技能実習から特定技能へ','移行の条件','試験の種類と内容','試験対策のポイント','まとめ'],
    'articles/visa','ginou-jisshuu-tokutei.html','2',vb2)
gen('日本語レベルN1・N2がビザ審査に与える影響','日本語能力がビザ審査でどう評価されるか。技人国・永住での影響。',
    ['日本語能力とビザ審査','技人国での評価','永住申請での評価','N1・N2のメリット','まとめ'],
    'articles/visa','nihongo-n1n2-eikyo.html','2',vb2)

vb4 = ['トップページ', ['仕事・金融','/pages/cong-viec.html']]
gen('日本でITエンジニアとして働くためのビザ取得ガイド','ITエンジニア向けビザ取得の条件、必要書類、転職方法。',
    ['ITエンジニアに適したビザ','技人国の該当業務','年収基準','転職市場','まとめ'],
    'articles/cong-viec','it-engineer-visa.html','4',vb4)
gen('日本の労働契約書で確認すべき重要ポイント','労働契約書の読み方、重要条項、確認すべきポイント。',
    ['労働契約書の基本','確認すべき重要項目','労働条件の明示','契約書と就業規則','トラブル防止策'],
    'articles/cong-viec','roudou-keiyakusho-point.html','4',vb4)

vb2_2 = ['トップページ', ['ビザ・更新','/pages/visa.html']]
gen('試用期間中のビザ更新はどうなる？','試用期間中のビザ更新の取扱いと注意点。',
    ['試用期間とビザ更新','審査への影響','会社の状況確認','更新手続きのコツ','まとめ'],
    'articles/visa','shiyo-kikan-koushin.html','2',vb2_2)
gen('会社が倒産した！ビザへの影響と転職の猶予期間','会社倒産時のビザ取扱い、求職活動期間、手続き。',
    ['会社倒産と在留資格','転職活動の猶予期間','必要な手続き','新しい会社の条件','まとめ'],
    'articles/visa','kaisha-tousan-visa.html','2',vb2_2)
gen('転職先でビザの許可が出ない可能性と対策','転職先のビザ不許可リスクと事前確認方法。',
    ['転職とビザ審査','不許可になるケース','事前確認の方法','対策と準備','まとめ'],
    'articles/visa','tenshoku-saki-fukyoka.html','2',vb2_2)
gen('日本でフリーランスとして働く際のビザ注意点','フリーランスでの在留資格、事業内容、収入証明のポイント。',
    ['フリーランスと在留資格','事業内容の範囲','収入証明の方法','更新時の注意点','まとめ'],
    'articles/visa','freelance-visa-note.html','2',vb2_2)

vb = ['トップページ', ['永住権・帰化','/pages/vinh-tru.html']]
gen('技人国ビザ保持者が会社役員になる方法','技人国ビザ保持者が役員兼任する場合の条件と手続き。',
    ['役員兼任のルール','在留資格の範囲外問題','許可申請の要否','副業規程の確認','まとめ'],
    'articles/visa','gijinkoku-yakuin.html','2',['トップページ',['ビザ・更新','/pages/visa.html'],'役員になる方法'])
gen('派遣社員として働く場合のビザ手続き','派遣社員での就労とビザ手続き、注意点。',
    ['派遣社員と在留資格','派遣元と派遣先の関係','必要な書類','ビザ更新時の注意','まとめ'],
    'articles/visa','haken-shain-visa.html','2',['トップページ',['ビザ・更新','/pages/visa.html'],'派遣社員のビザ'])
gen('特定技能2号への変更要件とメリット','特定技能1号から2号への変更条件とメリットを解説。',
    ['特定技能2号とは','変更の条件','試験合格要件','家族帯同・永住への道','まとめ'],
    'articles/visa','tokutei-2go-henkou.html','2',['トップページ',['ビザ・更新','/pages/visa.html'],'特定技能2号'])
gen('ベトナム人エンジニアのための日本のIT業界解説','日本IT業界の特徴、需要、キャリアパスをベトナム人向けに解説。',
    ['日本のIT業界の特徴','需要の高いスキル','年収の目安','キャリアパス','転職市場の活用法'],
    'articles/cong-viec','vietnam-engineer-it.html','4',vb4)

# ===== 結婚・家族・出産（15件）=====
vb3 = ['トップページ', ['ビザ・更新','/pages/visa.html']]
gen('日本人との結婚、入管への申請手順','日本人と結婚した後のビザ申請手順と必要書類。',
    ['結婚後の在留資格','配偶者ビザの申請手順','必要書類一覧','審査期間','まとめ'],
    'articles/visa','kekkon-nyukan-shinsei.html','2',vb3)
gen('結婚ビザ（配偶者ビザ）が不許可になる理由','配偶者ビザ不許可の主な理由と対策。',
    ['不許可になる主な理由','結婚の真实性の証明','収入不足','面接・質問書の重要性','再申請のコツ'],
    'articles/visa','haiguusha-visa-fukyoka.html','2',vb3)
gen('配偶者ビザの質問書（Shitsumonsho）の書き方','配偶者ビザ申請時の質問書の書き方と注意点。',
    ['質問書とは','質問項目と意図','効果的な回答方法','よくあるミス','まとめ'],
    'articles/visa','shitsumonsho-kakikata.html','2',vb3)
gen('日本で婚約中（短期滞在）に結婚手続きはできる？','短期滞在ビザでの結婚手続きの可否と方法。',
    ['短期滞在と結婚','結婚手続きの流れ','入国後のビザ変更','注意点','まとめ'],
    'articles/visa','konyaku-tanki-kekkon.html','2',vb3)
gen('夫婦別居が配偶者ビザに与える影響','別居中の配偶者ビザ更新への影響と対策。',
    ['別居と配偶者ビザ','正当な別居理由','別居中の更新手続き','審査での説明方法','まとめ'],
    'articles/visa','bekkyo-haiguusha-visa.html','2',vb3)
gen('配偶者が来日した後の住民登録手続き','配偶者の来日後の市区町村手続き完全ガイド。',
    ['来日後の初期手続き','住民登録の方法','国民健康保険の加入','その他の手続き','まとめ'],
    'articles/sinh-hoat','haiguusha-raiyu-toroku.html','3',['トップページ',['生活・行政','/pages/sinh-hoat.html'],'配偶者来日手続き'])
gen('日本での出産・育児休暇とビザの継続','出産・育児休暇中のビザ取扱いと手続き。',
    ['育児休業制度','ビザへの影響','休暇中の収入とビザ','復職時の手続き','まとめ'],
    'articles/visa','shussan-ikuji-visa.html','2',vb3)
gen('子供を日本で育てたい場合の在留資格ガイド','子育て中の在留資格の選択肢と条件。',
    ['子育てと在留資格','家族滞在ビザ','定住者ビザへの変更','子供の教育','まとめ'],
    'articles/visa','kodomo-sodateru-zairyu.html','2',vb3)
gen('国際結婚で必要なベトナム側の独身証明書取得','ベトナムでの独身証明書取得手順と必要書類。',
    ['独身証明書とは','ベトナムでの取得手順','翻訳・公証','注意点','まとめ'],
    'articles/visa','dokushin-shomeisho.html','2',vb3)
gen('日本人と離婚した後、日本に留まる方法','離婚後の在留資格選択肢と定住者ビザへの変更。',
    ['離婚後の在留資格','定住者ビザへの変更条件','必要書類','審査のポイント','まとめ'],
    'articles/visa','rikon-go-taizai-hoho.html','2',vb3)
gen('離婚調停中のビザ更新について','離婚調停中でもビザ更新は可能か、注意点。',
    ['離婚調停と在留資格','更新申請のポイント','審査への影響','専門家への相談','まとめ'],
    'articles/visa','rikon-chotei-koushin.html','2',vb3)
gen('配偶者ビザ保持者の就労制限について','配偶者ビザの就労制限の有無と可能な業務範囲。',
    ['配偶者ビザと就労','就労制限の有無','資格外活動許可の要不要','就労可能な業務','まとめ'],
    'articles/visa','haiguusha-shuro-seigen.html','2',vb3)
gen('家族滞在ビザでのアルバイト許可申請','家族滞在ビザ保持者の資格外活動許可と週28時間ルール。',
    ['家族滞在ビザの就労制限','資格外活動許可の申請','週28時間ルール','許可の範囲','まとめ'],
    'articles/visa','kazoku-taizai-arubaito.html','2',vb3)
gen('配偶者ビザでの扶養控除申請方法','配偶者ビザ保持者の扶養控除申請手順と注意点。',
    ['扶養控除の基本','配偶者ビザと扶養','申請手順','必要書類','注意点'],
    'articles/visa','haiguusha-fuyou-koujo.html','2',vb3)

# ===== 税金・年金・金融（14件）=====
gen('年金の「脱退一時金」申請後の将来の年金への影響','脱退一時金受給後の年金加入期間の取扱いと将来への影響。',
    ['脱退一時金と年金記録','将来の年金受給への影響','再び日本で働く場合','まとめ'],
    'articles/cong-viec','nenkin-dattai-ikiru-eikyo.html','4',vb4)
gen('確定申告（Kakutei shinkoku）が必要な人とは','確定申告が必要なケースと不要なケースの判断基準。',
    ['確定申告の基本','必要な人・不要な人','年末調整との違い','申告期限と方法','まとめ'],
    'articles/cong-viec','kakutei-shinkoku-hitsuyo.html','4',vb4)
gen('日本で生命保険に加入すべき理由と選び方','在日ベトナム人が生命保険に加入するメリットと選び方。',
    ['生命保険の重要性','加入すべき理由','保険の種類と選び方','注意点','まとめ'],
    'articles/sinh-hoat','seimei-hoken-erabikata.html','3',['トップページ',['生活・行政','/pages/sinh-hoat.html'],'生命保険の選び方'])
gen('クレジットカード審査に通らない時の対策','外国人でも通りやすいクレジットカードと審査通過のコツ。',
    ['クレジットカード審査の仕組み','通りやすいカード','審査通過のコツ','審査落ち後の対策','まとめ'],
    'articles/sinh-hoat','credit-card-shinsa.html','3',['トップページ',['生活・行政','/pages/sinh-hoat.html'],'クレジットカード審査'])
gen('外国人向け住宅ローンの条件（永住権あり・なし）','永住権の有無による住宅ローン審査の違いと条件。',
    ['住宅ローンの基本','永住権ありの場合','永住権なしの場合','頭金と金利','まとめ'],
    'articles/cong-viec','juutaku-loan-gaikokujin.html','4',vb4)
gen('住民税の特別徴収と普通徴収の違い','住民税の納付方法の違いと、退職時の手続き。',
    ['住民税の納付方法','特別徴収（給与天引き）','普通徴収（自分で納付）','退職時の手続き','まとめ'],
    'articles/sinh-hoat','juminzei-choshu-hikaku.html','3',['トップページ',['生活・行政','/pages/sinh-hoat.html'],'住民税の納付方法'])
gen('会社を辞めた後の住民税の支払い方法','退職後の住民税の支払い方法と手続き。',
    ['退職と住民税','一括納付か分割か','納付書の送付先','滞納防止策','まとめ'],
    'articles/cong-viec','taishoku-go-juminzei.html','4',vb4)
gen('日本の銀行での海外送金サービス比較','銀行と送金サービスの手数料・為替レート比較。',
    ['銀行送金の特徴','送金サービスの比較','手数料と為替レート','おすすめの方法','まとめ'],
    'articles/cong-viec','ginko-sokin-hikaku.html','4',vb4)
gen('扶養家族を日本に呼んだ後の税金への影響','家族呼び寄せ後の税金や社会保険料の変化。',
    ['家族呼び寄せと税金','扶養控除の適用','社会保険料の変化','注意点','まとめ'],
    'articles/cong-viec','fuyou-kazoku-yobiyose-zei.html','4',vb4)
gen('外国人が日本で資産運用する際のリスク','在日外国人の資産運用の注意点と税金。',
    ['資産運用の基本','注意すべきリスク','税金の取扱い','おすすめの運用方法','まとめ'],
    'articles/cong-viec','gaikokujin-shisan-unyou.html','4',vb4)
gen('日本での相続税・贈与税の基礎知識','相続税・贈与税の基礎と在日ベトナム人への影響。',
    ['相続税の基本','贈与税の基本','ベトナムとの違い','注意点','まとめ'],
    'articles/cong-viec','souzoku-zozei-kiso.html','4',vb4)
gen('日本の医療保険（健康保険）の仕組み','健康保険の種類、加入方法、給付内容を解説。',
    ['健康保険の種類','加入方法と保険料','ケガ・病気時の給付','高額療養費制度','まとめ'],
    'articles/sinh-hoat','kenko-hoken-shikumi.html','3',['トップページ',['生活・行政','/pages/sinh-hoat.html'],'健康保険の仕組み'])
gen('会社設立時の資本金準備の注意点','経営管理ビザ取得のための資本金準備と注意点。',
    ['資本金の役割','500万円要件の詳細','資金の出所証明','資金管理の注意点','まとめ'],
    'articles/cong-viec','shihonkin-junbi-note.html','4',vb4)

# ===== トラブル・リスク管理（25件）=====
traffic_titles = [
    ('日本の交通ルール違反の罰則一覧','交通違反の罰則、反則金、点数制度を解説。',
     ['交通違反の種類','反則金制度','違反点数','外国人への影響','まとめ']),
    ('警察に呼び出されたらどうなる？','警察での取調べの流れと対応方法。',
     ['呼出しの理由','取調べの流れ','権利と対応','通訳の依頼','まとめ']),
    ('悪質な詐欺業者・ビザブローカーへの対策','偽の行政書士やビザ詐欺の見分け方と対策。',
     ['ビザブローカーの手口','行政書士の確認方法','相談先','被害にあった場合','まとめ']),
    ('職場でのハラスメント相談先','パワハラ・セクハラの相談窓口と対処法。',
     ['ハラスメントの種類','社内相談窓口','社外相談機関','証拠の保全','まとめ']),
    ('日本の消費者センターへの相談方法','商品トラブル・悪質商法の相談先。',
     ['消費者センターの役割','相談の流れ','必要な情報','外国人向けサポート','まとめ']),
    ('賃貸物件の退去トラブルと敷金返還','退去時の原状回復義務と敷金トラブル対策。',
     ['退去時のルール','原状回復の範囲','敷金の精算','トラブル防止策','まとめ']),
    ('日本の医療機関で使える通訳サービス','医療通訳サービスの種類と利用方法。',
     ['医療通訳の必要性','利用できるサービス','予約方法','費用','まとめ']),
    ('日本の緊急連絡先リスト','緊急時の連絡先一覧（警察・消防・病院・入管）。',
     ['緊急連絡先一覧','各機関の役割','外国人向けサポート','まとめ']),
    ('外国人向け日本語学習リソース','無料・低料金の日本語学習リソース紹介。',
     ['日本語学習の重要性','オンラインリソース','地域の日本語教室','おすすめ教材','まとめ']),
    ('災害時の避難場所と防災用品リスト','地震・台風に備えた防災対策。',
     ['日本の自然災害','避難場所の確認','防災用品リスト','外国人向け情報','まとめ']),
    ('日本のゴミ出しルールの厳しさについて','地域ごとのゴミ分別ルールと違反時の注意。',
     ['ゴミ出しの基本ルール','分別方法','違反時の罰則','引っ越し時の確認','まとめ']),
    ('近隣トラブルの対処法','騒音・ペット・駐車場トラブルの解決方法。',
     ['よくある近隣トラブル','当事者間での解決','管理者への相談','警察・役所の活用','まとめ']),
    ('遺失物の届出と見つけ方','忘れ物・落とし物をした時の届出方法。',
     ['遺失物の届出','交番での手続き','駅・施設での確認','見つかる確率','まとめ']),
    ('日本の郵便システムの便利な使い方','郵便局のサービスと便利な活用法。',
     ['郵便局のサービス','転送届','国際郵便','各種支払い','まとめ']),
    ('マイナンバー通知カードとマイナンバーカードの違い','通知カードとカードの違い、切り替え方法。',
     ['通知カードとは','マイナンバーカードとは','違いと注意点','切り替え方法','まとめ']),
]
for i, (title, desc, h2s) in enumerate(traffic_titles):
    gen(title, desc, h2s, 'articles/sinh-hoat', f'trouble-skeleton-{i+1:02d}.html', '3',
        ['トップページ',['生活・行政','/pages/sinh-hoat.html'],title])

more_trouble = [
    ('ビザの有効期限切れと「仮放免」とは','在留期限切れ後の仮放免制度の説明と手続き。',
     ['在留期限切れのリスク','仮放免とは','申請手続き','仮放免中の制限','まとめ']),
    ('「オーバーステイ」の自主出頭と帰国手続き','不法残留者の自主出頭と帰国までの流れ。',
     ['オーバーステイとは','自主出頭のメリット','出国手続き','再入国の可能性','まとめ']),
    ('外国人相談窓口の活用法','地域の外国人相談窓口と利用方法。',
     ['相談窓口の種類','利用方法','対応言語','相談事例','まとめ']),
    ('日本の図書館や公共施設でできること','図書館の利用方法と便利なサービス。',
     ['図書館の基本サービス','外国人向けサービス','無料WiFi','その他の公共施設','まとめ']),
    ('日本のネットオークションでのトラブル防止','メルカリ・ヤフオクの安全な利用方法。',
     ['ネットオークションの基本','よくあるトラブル','安全な取引方法','トラブル時の対応','まとめ']),
    ('日本の冠婚葬祭マナーと香典相場','結婚式・葬式のマナーと費用の目安。',
     ['冠婚葬祭の基本','結婚式のマナー','葬式のマナー','香典・ご祝儀の相場','まとめ']),
    ('日本の敬語（ビジネス日本語）の基礎','職場で使える敬語の基本ルールと例文。',
     ['敬語の種類','尊敬語・謙譲語・丁寧語','よく使う表現','ビジネスメール','まとめ']),
    ('ビザ申請時の「身元保証書」の法的責任','身元保証人の法的責任とリスク。',
     ['身元保証書の法的性質','保証人の責任範囲','リスクと注意点','保証人への説明','まとめ']),
]
for i, (title, desc, h2s) in enumerate(more_trouble):
    gen(title, desc, h2s, 'articles/sinh-hoat', f'trouble-skeleton-{11+i:02d}.html', '3',
        ['トップページ',['生活・行政','/pages/sinh-hoat.html'],title])

# ===== 労働・雇用（5件）=====
work_titles = [
    ('会社が社会保険料を未納の場合の確認方法','社会保険料未納の確認方法と会社への対応依頼。',
     ['社会保険料未納のリスク','確認方法','会社への問合せ','年金事務所への相談','まとめ']),
    ('労働契約書の読み方と重要ポイント','労働契約書の各条項の意味と確認ポイント。',
     ['労働契約書の構成','労働条件の確認','知っておくべき条項','サイン前のチェック','まとめ']),
    ('会社退職時の離職票の受け取り方','離職票の役割と退職時の受け取り方法。',
     ['離職票とは','退職時の手続き','失業保険申請との関係','受け取れない場合','まとめ']),
    ('失業保険（雇用保険）がもらえる条件','雇用保険の受給資格と手続き。',
     ['雇用保険の基本','受給条件','給付額と期間','申請手続き','まとめ']),
    ('外国人労働者の健康診断とストレスチェック','法定健康診断とストレスチェックの義務と内容。',
     ['健康診断の義務','定期健康診断の内容','ストレスチェック制度','受診方法','まとめ']),
]
for i, (title, desc, h2s) in enumerate(work_titles):
    gen(title, desc, h2s, 'articles/cong-viec', f'work-skeleton-{i+1:02d}.html', '4', vb4)

# ===== 生活・その他（15件）=====
other_titles = [
    ('日本の出産一時金の申請ガイド','出産一時金42万円の申請方法と受け取り手順。',
     ['出産一時金とは','支給額42万円','申請方法','直接支払制度','まとめ']),
    ('児童手当の申請条件と手続き','児童手当の対象条件と申請方法。',
     ['児童手当の概要','受給条件','申請手続き','支給額','まとめ']),
    ('永住申請前の健康診断は必要か？','永住申請における健康診断の要否と基準。',
     ['永住申請と健康状態','健康診断の提出義務','健康上の問題がある場合','まとめ']),
    ('日本でのレンタカー利用時の保険とルール','レンタカー保険の種類と注意点。',
     ['レンタカー利用の流れ','保険の種類','補償内容の確認','事故時の対応','まとめ']),
    ('スマートフォン契約（店舗とネットの違い）','携帯電話契約の店舗とオンラインの比較。',
     ['契約方法の種類','店舗契約の特徴','オンライン契約の特徴','おすすめの方法','まとめ']),
    ('格安SIM（MVNO）への乗り換え手続き','格安SIMの選び方と乗り換え手順。',
     ['格安SIMとは','おすすめの格安SIM','乗り換え手順','注意点','まとめ']),
    ('光回線の契約縛りと解約違約金','光回線の契約期間と解約時の費用。',
     ['光回線の契約形態','縛り期間と違約金','違約金なしの選択肢','乗り換えのコツ','まとめ']),
    ('コンビニでの公共料金支払い方法','コンビニでの料金支払い手順と注意点。',
     ['支払可能な料金','支払い手順','領収書の保管','便利な活用法','まとめ']),
    ('ビザ申請用写真の規定','ビザ申請写真のサイズ・背景・服装ルール。',
     ['写真の基本規定','サイズと背景','服装と表情','よくある不備','まとめ']),
    ('入管手数料（収入印紙）の買い方','収入印紙の購入方法と必要な金額。',
     ['収入印紙とは','必要な金額','購入場所','貼付方法','まとめ']),
    ('日本での印鑑登録の手続き','印鑑登録の方法と実印の必要性。',
     ['印鑑登録とは','登録手順','実印の用途','認印との違い','まとめ']),
    ('住民票の写しのオンライン請求方法','マイナポータルを使った住民票のオンライン請求。',
     ['オンライン請求の条件','マイナポータルの準備','請求手順','受け取り方法','まとめ']),
    ('在留資格申請の電子申請（オンライン）のやり方','入管のオンライン申請システムの利用方法。',
     ['電子申請の概要','利用条件','申請手順','メリット・デメリット','まとめ']),
    ('就労証明書の依頼の仕方','ビザ申請に必要な就労証明書を会社に依頼する方法。',
     ['就労証明書の重要性','依頼のタイミング','依頼の仕方','会社側の準備','まとめ']),
    ('ビザ申請における立証資料の収集方法','効果的な立証資料の集め方と整理方法。',
     ['立証資料の役割','種類と内容','収集の順序','整理方法','まとめ']),
]
for i, (title, desc, h2s) in enumerate(other_titles):
    gen(title, desc, h2s, 'articles/sinh-hoat', f'other-skeleton-{i+1:02d}.html', '3',
        ['トップページ',['生活・行政','/pages/sinh-hoat.html'],title])

# ===== 配偶者ビザ・離婚関連の追記（2件）=====
gen('日本人配偶者と別居中のビザ更新','別居中の配偶者ビザ更新の可否と必要書類、審査ポイント。',
    ['別居と配偶者ビザ','更新申請のポイント','必要書類','審査での説明','まとめ'],
    'articles/visa','betsukyo-koushin.html','2',['トップページ',['ビザ・更新','/pages/visa.html'],'別居中のビザ更新'])
gen('会社経営が厳しい時の経営管理ビザ更新','赤字・債務超過時の経営管理ビザ更新のリスクと対策。',
    ['経営管理ビザの更新要件','赤字時のリスク','改善計画の提出','更新時期の戦略','まとめ'],
    'articles/visa','keiei-iken-shin.html','2',['トップページ',['ビザ・更新','/pages/visa.html'],'経営難時の更新'])
gen('特定技能1号と2号の違い','特定技能1号と2号の在留期間、家族帯同、永住への道の違い。',
    ['特定技能の2類型','在留期間の違い','家族帯同の可否','永住権申請への道','まとめ'],
    'articles/visa','tokutei-1go-2go-sai.html','2',['トップページ',['ビザ・更新','/pages/visa.html'],'特定技能1号と2号'])
gen('国際運転免許証（IDP）で日本を運転できる期間','国際免許での運転可能期間と日本の免許への切替え。',
    ['国際運転免許証とは','運転可能期間','切替え手続き','注意点','まとめ'],
    'articles/sinh-hoat','idp- unten-kikan.html','3',['トップページ',['生活・行政','/pages/sinh-hoat.html'],'国際運転免許'])
gen('外国人向け賃貸保証会社の利用方法','賃貸契約時の保証会社利用の流れと費用。',
    ['保証会社とは','利用の流れ','費用の目安','保証人がいらない場合','まとめ'],
    'articles/sinh-hoat','hoshou-gaisha-riyou.html','3',['トップページ',['生活・行政','/pages/sinh-hoat.html'],'賃貸保証会社'])
gen('専門家へ相談するタイミングまとめ','永住権・ビザ手続きで専門家に相談すべきタイミングの総まとめ。',
    ['自分でできること・できないこと','相談すべきタイミング一覧','専門家の選び方','費用の目安','まとめ'],
    'articles/chuyen-gia','soudan-taimingu-matome.html','5',['トップページ',['専門家相談','/pages/chuyen-gia.html'],'相談タイミングまとめ'])

print("\n✅ 追加スケルトン全91件生成完了！")