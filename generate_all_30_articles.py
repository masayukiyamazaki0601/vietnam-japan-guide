#!/usr/bin/env python3
"""
30記事を一括生成するスクリプト - SEO最適化済み
既存のスケルトン23件＋新規7件 = 30件
"""
import os
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARTICLES_30 = {}

# ============================================================
# 1. 既存スケルトン記事 (visa-skeleton-01 to 13, life-skeleton-01 to 10)
# ============================================================

# --- visa-skeleton-01 (既存) ---
ARTICLES_30["visa-skeleton-01"] = {
    "title": "特定技能から技人国ビザへ変更する条件｜在日ベトナム人向け完全ガイド",
    "meta_desc": "特定技能1号から技人国（技術・人文知識・国際業務）ビザへの変更条件を徹底解説。必要書類、学歴要件、実務経験、審査期間、成功率アップのポイントまで網羅。出入国在留管理庁の基準に基づいてわかりやすく説明します。",
    "meta_keywords": "特定技能,技人国ビザ,在留資格変更,特定技能1号,技術人文知識国際業務,キャリアアップ,入管手続き",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-02 (既存) ---
ARTICLES_30["visa-skeleton-02"] = {
    "title": "特定技能ビザの更新と試験の受け方｜完全ガイド",
    "meta_desc": "特定技能ビザ（1号・2号）の更新条件、必要書類、スケジュールを徹底解説。特定技能評価試験の種類、受験方法、合格ラインまで網羅。出入国在留管理庁の最新基準に基づいて解説します。",
    "meta_keywords": "特定技能ビザ,更新,試験,特定技能1号,特定技能2号,評価試験,技能測定試験,日本語試験",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-03 ---
ARTICLES_30["visa-skeleton-03"] = {
    "title": "家族滞在ビザで配偶者を呼ぶための年収要件｜在日ベトナム人ガイド",
    "meta_desc": "家族滞在ビザでベトナムから配偶者を呼び寄せるための年収要件、必要書類、審査期間を徹底解説。出入国在留管理庁の基準に基づき、安定した収入の証明方法まで詳しく説明します。",
    "meta_keywords": "家族滞在ビザ,配偶者呼び寄せ,年収要件,在留資格,家族滞在,必要書類,審査基準",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-04 ---
ARTICLES_30["visa-skeleton-04"] = {
    "title": "子供が日本で生まれた場合の在留資格取得手続き完全ガイド",
    "meta_desc": "日本で子供が生まれた際の在留資格取得手続きを完全解説。出生届の提出方法、在留資格取得申請の期限、必要書類、注意点まで詳しく説明します。出入国在留管理庁の手続きに基づく最新情報。",
    "meta_keywords": "出生,在留資格,子供,出生届,在留カード,日本出生,手続き,入管",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-05 ---
ARTICLES_30["visa-skeleton-05"] = {
    "title": "留学ビザから就労ビザへの変更手続き｜ベトナム人留学生向け",
    "meta_desc": "留学ビザ（留学）から就労ビザ（技人国など）への変更手続きを徹底解説。必要書類、審査期間、内定から申請までの流れ、よくある不許可理由と対策まで網羅。",
    "meta_keywords": "留学ビザ,就労ビザ,在留資格変更,留学生,技人国,就職,就活ビザ,入管手続き",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-06 ---
ARTICLES_30["visa-skeleton-06"] = {
    "title": "技人国ビザで「専攻外」の仕事はできるか｜在日ベトナム人必見",
    "meta_desc": "技人国ビザ（技術・人文知識・国際業務）で大学の専攻と異なる仕事に就く場合の条件とリスクを解説。入管の審査基準、許可されるケース、注意点を詳しく説明。",
    "meta_keywords": "技人国ビザ,専攻外,技術人文知識国際業務,入管審査,転職,職種変更",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-07 ---
ARTICLES_30["visa-skeleton-07"] = {
    "title": "特定活動（就職活動）ビザの期間と延長ルール",
    "meta_desc": "特定活動（就職活動）ビザの期間、延長条件、申請方法を徹底解説。大学・専門学校卒業後の就職活動ビザの取得方法から内定後の手続きまで詳しく説明。",
    "meta_keywords": "特定活動,就職活動ビザ,延長,就活ビザ,卒業後,インターンシップ,入管",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-08 ---
ARTICLES_30["visa-skeleton-08"] = {
    "title": "ビザ更新時期と期限切れ直前の対応方法｜緊急ガイド",
    "meta_desc": "ビザ（在留期間）の更新時期、申請期限、期限切れ直前の対処法を解説。不法滞在を防ぐための緊急対応から、法定特別在籍者のルールまで徹底網羅。",
    "meta_keywords": "ビザ更新,在留期間更新,期限切れ,不法滞在,更新申請,入管,緊急対応",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-09 ---
ARTICLES_30["visa-skeleton-09"] = {
    "title": "追加資料提出通知書が届いた時の対処法｜不許可を防ぐために",
    "meta_desc": "入国管理局から追加資料提出通知書が届いた際の対処法を徹底解説。求められる書類の種類、提出期限、理由書の書き方、よくあるケースと対策まで。",
    "meta_keywords": "追加資料提出,入管,通知書,不許可,書類追加,審査,理由書,在留申請",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-10 ---
ARTICLES_30["visa-skeleton-10"] = {
    "title": "ビザが不許可になった！すぐにやるべきこと｜再申請ガイド",
    "meta_desc": "ビザ（在留資格）が不許可になった場合の対処法を徹底解説。不許可理由の確認方法、再申請のタイミング、行政書士に相談すべきケースまで網羅。再申請成功のポイントを紹介。",
    "meta_keywords": "ビザ不許可,再申請,不許可理由,入管,行政書士,在留資格,不服申立て",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-11 ---
ARTICLES_30["visa-skeleton-11"] = {
    "title": "再入国許可とみなし再入国許可の違い｜ベトナム帰国の前に",
    "meta_desc": "再入国許可とみなし再入国許可の違い、手続き方法、費用、注意点を徹底比較。ベトナムに一時帰国する前に知っておくべき在留管理のポイントを解説。",
    "meta_keywords": "再入国許可,みなし再入国許可,一時帰国,ベトナム,在留カード,入管,出国手続き",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-12 ---
ARTICLES_30["visa-skeleton-12"] = {
    "title": "経営・管理ビザの取得手順と資本金要件｜起業ガイド",
    "meta_desc": "経営・管理ビザ（投資経営ビザ）の取得条件、資本金要件、事業計画書の書き方、必要書類を徹底解説。日本で会社を設立して起業するベトナム人向けの完全ガイド。",
    "meta_keywords": "経営管理ビザ,投資経営ビザ,起業,資本金,事業計画書,会社設立,ベトナム人起業",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- visa-skeleton-13 ---
ARTICLES_30["visa-skeleton-13"] = {
    "title": "技人国ビザで副業・アルバイトは可能か？ルールとリスク解説",
    "meta_desc": "技人国ビザ（技術・人文知識・国際業務）で副業やアルバイトが可能かどうかを解説。入管の許可範囲、資格外活動許可の必要性、リスクと注意点まで詳しく説明。",
    "meta_keywords": "技人国ビザ,副業,アルバイト,資格外活動許可,入管,在留資格,収入,注意点",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- life-skeleton-01 ---
ARTICLES_30["life-skeleton-01"] = {
    "title": "住民票（Juminhyo）の取り方と用途｜在日ベトナム人ガイド",
    "meta_desc": "住民票の取得方法、必要なもの、費用、用途を徹底解説。市区町村役場での手続き、マイナンバーカードを使ったコンビニ交付、永住権申請に必要な住民票の取り方まで。",
    "meta_keywords": "住民票,ジュウミンヒョウ,取得方法,役場,コンビニ交付,永住権,在留カード",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- life-skeleton-02 ---
ARTICLES_30["life-skeleton-02"] = {
    "title": "市役所での住所変更手続き完全ガイド｜住居変更時に必要なこと",
    "meta_desc": "日本で引っ越しをした際の住所変更手続きを完全解説。市区町村役場での転入・転出届の出し方、在留カードの裏面記載更新、必要な持ち物まで網羅。",
    "meta_keywords": "住所変更,転入届,転出届,引越し,市役所,在留カード,在留管理,手続き",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- life-skeleton-03 ---
ARTICLES_30["life-skeleton-03"] = {
    "title": "在留カード紛失時の再発行手順｜緊急対応ガイド",
    "meta_desc": "在留カードを紛失した場合の緊急対応から再発行手続きまでを徹底解説。紛失届の出し方、警察への届出、入国管理局での再発行申請、必要な書類と費用まで。",
    "meta_keywords": "在留カード紛失,再発行,入管,警察,紛失届,在留管理,外国人登録",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- life-skeleton-04 ---
ARTICLES_30["life-skeleton-04"] = {
    "title": "課税証明書・納税証明書の取り方｜永住権申請に必要な書類",
    "meta_desc": "課税証明書と納税証明書の取得方法を徹底解説。市区町村役場での手続き、必要書類、費用、永住権申請やビザ更新での使い方まで詳しく説明。",
    "meta_keywords": "課税証明書,納税証明書,永住権,税金,市区町村,役場,取得方法,収入証明",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- life-skeleton-05 ---
ARTICLES_30["life-skeleton-05"] = {
    "title": "マイナンバーカードを作るメリット｜在日ベトナム人向け",
    "meta_desc": "在日ベトナム人がマイナンバーカードを作るメリットを徹底解説。作成方法、必要な書類、健康保険証としての利用、確定申告での活用、注意点まで詳しく説明。",
    "meta_keywords": "マイナンバーカード,マイナンバー,在日外国人,健康保険証,確定申告,メリット,作成方法",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- life-skeleton-06 ---
ARTICLES_30["life-skeleton-06"] = {
    "title": "健康保険に加入しないとどうなるか？リスクと対策",
    "meta_desc": "日本で健康保険に加入しないリスクを徹底解説。医療費の全額負担、永住権申請への影響、国民健康保険と社会健康保険の違い、加入手続きの方法まで。",
    "meta_keywords": "健康保険,未加入,国民健康保険,社会保険,医療費,永住権,ペナルティ,加入手続き",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- life-skeleton-07 ---
ARTICLES_30["life-skeleton-07"] = {
    "title": "年金脱退一時金の申請手順｜ベトナム帰国時に受け取るお金",
    "meta_desc": "年金脱退一時金の申請条件、必要書類、請求手続きを徹底解説。ベトナム帰国時に日本で納めた年金の一部を取り戻す方法。請求期限や受取金額の計算方法まで。",
    "meta_keywords": "年金脱退一時金,脱退一時金,年金,ベトナム帰国,日本年金機構,請求手続き,申請方法",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- life-skeleton-08 ---
ARTICLES_30["life-skeleton-08"] = {
    "title": "国民健康保険の計算方法と減免制度｜保険料を安くする方法",
    "meta_desc": "国民健康保険料の計算方法、所得に応じた保険料の決まり方、減免制度の申請条件を詳しく解説。在日ベトナム人が保険料負担を軽減するための具体的な方法を紹介。",
    "meta_keywords": "国民健康保険,計算方法,減免制度,保険料,所得,市区町村,申請,軽減措置",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- life-skeleton-09 ---
ARTICLES_30["life-skeleton-09"] = {
    "title": "日本での出産一時金と助成金申請｜ベトナム人ママ向けガイド",
    "meta_desc": "日本で出産した際の出産一時金（出産育児一時金）の受け取り方法、助成金制度、申請手続きを徹底解説。健康保険加入者と未加入者の違い、ベトナム人に必要な書類まで。",
    "meta_keywords": "出産一時金,出産育児一時金,助成金,出産,健康保険,ベトナム人,申請方法,子供",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- life-skeleton-10 ---
ARTICLES_30["life-skeleton-10"] = {
    "title": "源泉徴収票を会社がくれない時の対策｜在日ベトナム人の権利",
    "meta_desc": "会社が源泉徴収票を発行してくれない場合の対処法を徹底解説。法的な権利、税務署への相談方法、確定申告で代用する方法、転職時の引き継ぎまで詳しく説明。",
    "meta_keywords": "源泉徴収票,会社,発行しない,確定申告,税務署,労働トラブル,年末調整,在日外国人",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# ============================================================
# 2. 新規記事 (7件) - 既存枠を超えるテーマ
# ============================================================

# --- new-01: 特定技能から永住権への道のり ---
ARTICLES_30["new-eijyu-tokutei"] = {
    "title": "特定技能から永住権への道のり｜要件と注意点を徹底解説",
    "meta_desc": "特定技能ビザから永住権を取得するための道のりを徹底解説。特定技能1号から2号、そして永住権申請までの条件、必要書類、注意点を時系列でわかりやすく説明します。",
    "meta_keywords": "特定技能,永住権,永住許可,特定技能2号,在留期間,永住申請,キャリアパス",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- new-02: 転職がビザ更新に与える影響 ---
ARTICLES_30["new-tenshoku-visa"] = {
    "title": "転職がビザ更新に与える影響と正しい手続き｜在日ベトナム人向け",
    "meta_desc": "転職がビザ（在留資格）に与える影響を徹底解説。技人国・特定技能・家族滞在など在留資格別の注意点、入管への届出方法、転職後の更新手続きまで網羅。",
    "meta_keywords": "転職,ビザ更新,在留資格,技人国,特定技能,入管届出,転職手続き,影響",
    "category_name": "ビザ・更新",
    "category_url": "/pages/visa.html",
}

# --- new-03: ベトナム送金サービス比較 ---
ARTICLES_30["new-sokin-hikaku"] = {
    "title": "ベトナム送金サービス比較2026｜手数料・為替レート・使いやすさ",
    "meta_desc": "日本からベトナムへのおすすめ送金サービスを徹底比較。SBI Remit、Wise、Revolut、楽天銀行などの手数料、為替レート、送金速度、使いやすさをランキング形式で紹介。",
    "meta_keywords": "ベトナム送金,SBI Remit,Wise,Revolut,送金比較,手数料,為替レート,海外送金",
    "category_name": "仕事・金融",
    "category_url": "/pages/cong-viec.html",
}

# --- new-04: 確定申告が必要なケース ---
ARTICLES_30["new-kakutei-shinkoku"] = {
    "title": "在日ベトナム人が確定申告すべきケース｜2026年最新ガイド",
    "meta_desc": "在日外国人が確定申告（所得税の確定申告）が必要なケースを徹底解説。副業収入、複数の職場、還付申告、 freelancer、年末調整との関係まで詳しく説明。",
    "meta_keywords": "確定申告,確定申告,在日外国人,副業,還付申告,税金,年末調整,ベトナム人",
    "category_name": "仕事・金融",
    "category_url": "/pages/cong-viec.html",
}

# --- new-05: 子供の学校入学手続き ---
ARTICLES_30["new-kodomo-nyugaku"] = {
    "title": "ベトナム人の子供の学校入学手続きガイド｜日本の教育制度解説",
    "meta_desc": "在日ベトナム人の子供を日本の学校に入学させる手続きを徹底解説。幼稚園・小学校・中学校の入学方法、必要な書類、言語サポート、就学援助制度まで網羅。",
    "meta_keywords": "学校入学,子供,教育,日本語支援,小学校,中学校,幼稚園,外国人児童,就学",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- new-06: おすすめの携帯電話・格安SIM比較 ---
ARTICLES_30["new-mobile-sim"] = {
    "title": "在日ベトナム人におすすめの格安SIM・携帯電話比較2026",
    "meta_desc": "在日ベトナム人におすすめの格安SIM（格安SIM）と携帯電話キャリアを徹底比較。月額料金、データ容量、日本語サポート、ベトナム通話の可否などをランキング形式で紹介。",
    "meta_keywords": "格安SIM,携帯電話,モバイル,データ通信,ベトナム通話,ahamo,楽天モバイル,LINEモバイル",
    "category_name": "生活・行政",
    "category_url": "/pages/sinh-hoat.html",
}

# --- new-07: 社会保険と税金の基礎知識 ---
ARTICLES_30["new-shahoken-zei"] = {
    "title": "在日ベトナム人のための社会保険と税金の基礎知識",
    "meta_desc": "日本の社会保険（健康保険・厚生年金）と税金（所得税・住民税）の基礎を徹底解説。給与明細の見方、控除の種類、所得の計算方法をわかりやすく説明します。",
    "meta_keywords": "社会保険,税金,健康保険,厚生年金,所得税,住民税,給与明細,控除,基礎知識",
    "category_name": "仕事・金融",
    "category_url": "/pages/cong-viec.html",
}

def make_sections_visa01():
    """visa-skeleton-01 sections"""
    return {
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
<p>特定技能から技人国ビザへの変更申請に必要な書類を一覧で紹介します。</p>
<h3>申請者本人が準備する書類</h3>
<table>
  <thead><tr><th>書類名</th><th>取得先・備考</th></tr></thead>
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
<h3>雇用先が準備する書類</h3>
<table>
  <thead><tr><th>書類名</th><th>備考</th></tr></thead>
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
  <li>追加資料の提出を求められる場合がある</li>
  <li>繁忙期（卒業シーズンの3月〜4月、入社シーズンの4月〜5月）は審査が混み合う</li>
  <li>企業の財務状況や事業内容によっては追加調査が入ることもある</li>
</ul>
""",
        "注意点とリスク": """
<p>特定技能から技人国ビザへの変更には、いくつかの注意点とリスクがあります。</p>
<h3>主な不許可リスク</h3>
<ul>
  <li><strong>職務内容の不一致</strong>：現在の業務内容が技人国ビザの対象範囲と一致しない場合</li>
  <li><strong>学歴要件を満たしていない</strong>：大学卒業でなく、実務経験も不十分な場合</li>
  <li><strong>企業の経営状況</strong>：雇用先が赤字続きや小規模すぎる場合</li>
  <li><strong>給与が低すぎる</strong>：日本人と同等以上の給与でない場合</li>
</ul>
<h3>変更中の注意点</h3>
<ul>
  <li>審査中は現在の特定技能ビザの範囲内でのみ就労可能</li>
  <li>審査中に転職すると申請がやり直しになる</li>
  <li>不許可の場合、特定技能ビザの残存期間内であれば継続就労は可能</li>
</ul>
""",
        "よくある質問（FAQ）": """
<h3>Q1. 特定技能1号から技人国に変わると、在留期間はどうなりますか？</h3>
<p>A. 技人国ビザの在留期間は「3ヶ月」「1年」「3年」「5年」のいずれかが付与されます。</p>
<h3>Q2. 特定技能2号からも変更できますか？</h3>
<p>A. 特定技能2号から技人国への変更も可能です。要件を満たせば変更できます。</p>
<h3>Q3. 不許可になった場合、すぐに再申請できますか？</h3>
<p>A. 再申請自体は可能ですが、不許可理由を十分に改善せずに再申請すると、再度不許可となる可能性が高いです。</p>
""",
    }

def make_sections_visa02():
    """visa-skeleton-02 sections"""
    return {
        "特定技能ビザ更新の基本条件": """
<p>特定技能ビザ（1号・2号）の更新は、在留期間の満了前に適切な手続きを行うことで在留を継続できます。</p>
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
<h3>基本書類</h3>
<table>
  <thead><tr><th>書類名</th><th>備考</th></tr></thead>
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
  <thead><tr><th>職種</th><th>必要な試験</th></tr></thead>
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
""",
        "更新手続きのスケジュールと注意点": """
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
  <li>更新申請中に転職する場合は、新しい雇用先との契約書類も提出する必要がある</li>
  <li>試験の有効期限に注意（合格から一定期間内に申請する必要がある場合もある）</li>
</ul>
""",
        "よくある質問（FAQ）": """
<h3>Q1. 特定技能ビザの更新は何回でもできますか？</h3>
<p>A. 特定技能1号は通算で最長5年までです。ただし、特定技能2号に移行すれば期間の制限なく更新可能です。</p>
<h3>Q2. 更新時に日本語試験は必要ですか？</h3>
<p>A. すでに合格している場合は不要です。初回申請時に合格していなかった場合は、更新時までに合格する必要があります。</p>
<h3>Q3. 更新不許可になる原因は？</h3>
<p>A. 主な原因は、収入が日本人と同等でない、社会保険未加入、技能水準を満たしていない、などです。</p>
""",
    }

def make_sections_visa03():
    """家族滞在ビザで配偶者を呼ぶための年収要件"""
    return {
        "配偶者呼び寄せの基本条件": """
<p>家族滞在ビザでベトナムから配偶者を呼び寄せるためには、いくつかの条件を満たす必要があります。出入国在留管理庁の審査基準に基づいて解説します。</p>
<h3>在留資格の要件</h3>
<p>配偶者を呼び寄せるためには、以下の在留資格のいずれかを保持している必要があります：</p>
<ul>
  <li>技術・人文知識・国際業務（技人国）ビザ</li>
  <li>経営・管理ビザ</li>
  <li>特定技能ビザ（1号・2号）</li>
  <li>永住者ビザ</li>
  <li>日本人の配偶者等ビザ</li>
</ul>
<h3>収入要件の目安</h3>
<p>配偶者を扶養するのに十分な収入があることが求められます。具体的な基準は以下の通りです：</p>
<ul>
  <li><strong>最低年収</strong>：目安として年収300万円以上（月収25万円以上）</li>
  <li><strong>安定性</strong>：正社員またはそれに準ずる安定した雇用形態であること</li>
  <li><strong>継続性</strong>：少なくとも1年以上の継続した収入があること</li>
  <li><strong>扶養能力</strong>：配偶者を扶養した上で、自身の生活も十分に維持できる収入であること</li>
</ul>
""",
        "必要書類一覧": """
<h3>申請者（在日側）が準備する書類</h3>
<table>
  <thead><tr><th>書類名</th><th>備考</th></tr></thead>
  <tbody>
    <tr><td>在留資格変更許可申請書</td><td>出入国在留管理庁サイトからダウンロード</td></tr>
    <tr><td>パスポート（写し）</td><td>在日側のパスポート</td></tr>
    <tr><td>在留カード（写し）</td><td>両面</td></tr>
    <tr><td>雇用証明書</td><td>在職証明書または雇用契約書</td></tr>
    <tr><td>源泉徴収票</td><td>直近1年分</td></tr>
    <tr><td>課税証明書</td><td>市区町村役場で取得</td></tr>
    <tr><td>納税証明書</td><td>市区町村役場で取得</td></tr>
    <tr><td>住民票</td><td>世帯全員の記載があるもの</td></tr>
  </tbody>
</table>
<h3>配偶者（ベトナム側）が準備する書類</h3>
<ul>
  <li>パスポート（原本と写し）</li>
  <li>結婚証明書（婚姻証明書）</li>
  <li>戸籍謄本（ベトナムの場合：家族登録証明書）</li>
  <li>写真（縦4cm×横3cm）</li>
</ul>
""",
        "審査期間と注意点": """
<h3>標準的な審査期間</h3>
<ul>
  <li><strong>東京入国管理局</strong>：申請から許可まで約1〜3ヶ月</li>
  <li><strong>その他の入国管理局</strong>：約2週間〜2ヶ月</li>
</ul>
<h3>審査通過のポイント</h3>
<ul>
  <li>収入の安定性を証明するため、複数年の源泉徴収票や課税証明書を提出する</li>
  <li>結婚が事実であることを証明する写真や交際経緯の説明書があると有利</li>
  <li>住居が家族で暮らすのに十分な広さであることを証明する</li>
  <li>過去に在留状況に問題がないこと（オーバーステイや不法就労がないこと）</li>
</ul>
""",
        "よくある質問（FAQ）": """
<h3>Q1. 配偶者がベトナムで働いている場合でも呼び寄せられますか？</h3>
<p>A. はい、可能です。ただし、在日側に配偶者を扶養する十分な収入があることが条件です。</p>
<h3>Q2. 内縁関係でも家族滞在ビザは取得できますか？</h3>
<p>A. いいえ、原則として法律上の婚姻関係が必要です。</p>
<h3>Q3. 配偶者が呼び寄せられた後、アルバイトはできますか？</h3>
<p>A. 資格外活動許可を取得すれば、週28時間以内（就学先がある場合）でアルバイトが可能です。</p>
<h3>Q4. 年収が300万円未満でも申請できますか？</h3>
<p>A. 申請自体は可能ですが、不許可リスクが高まります。収入が少ない場合は預貯金の証明などで補強することができます。</p>
""",
    }

def make_sections_life_basic(title, text_parts):
    """Generate basic sections for life articles"""
    sections = {}
    for title_text, content in text_parts:
        sections[title_text] = content
    sections["よくある質問（FAQ）"] = """
<h3>Q1. この手続きはオンラインでできますか？</h3>
<p>A. 一部の手続きはマイナポータルや各市区町村のオンラインサービスで可能ですが、初回は窓口での手続きが必要な場合が多いです。</p>
<h3>Q2. 必要な持ち物を忘れた場合はどうなりますか？</h3>
<p>A. 必要な書類がないと手続きができない場合があります。事前に確認してから窓口に行くことをおすすめします。</p>
<h3>Q3. 代理人が手続きできますか？</h3>
<p>A. 委任状と代理人の身分証明書があれば一部の手続きは可能ですが、本人出頭が必要な手続きもあります。</p>
"""
    return sections


SECTIONS_GENERATORS = {}

def generate_html_file(slug, data, sections):
    """Generate complete HTML file"""
    today = datetime.now().strftime("%Y-%m-%d")
    headline = data["title"].split('｜')[0]
    meta_desc = data["meta_desc"]
    meta_keywords = data["meta_keywords"]
    category_name = data["category_name"]
    category_url = data["category_url"]

    # Determine path
    if "life" in slug or "new-kodomo" in slug or "new-mobile" in slug:
        file_dir = "sinh-hoat"
        active_idx = 2
    elif "new-sokin" in slug or "new-kakutei" in slug or "new-shahoken" in slug:
        file_dir = "cong-viec"
        active_idx = 3
    else:
        file_dir = "visa"
        active_idx = 1

    og_url = f"https://vietnam-japan-guide.com/articles/{file_dir}/{slug}.html"
    canonical = og_url

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
        qas = re.findall(r'<h3>Q\d+\.\s*([^<]+)</h3>\s*<p>A\.\s*([^<]+)</p>', faq_content)
        if qas:
            items = []
            for q, a in qas:
                items.append(f'{{"@type":"Question","name":"{q.strip()}","acceptedAnswer":{{"@type":"Answer","text":"{a.strip()}"}}}}')
            faq_schema = '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n' + ',\n'.join(items) + '\n]}\n</script>'

    # Determine nav links
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

    html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data["title"]} | Vietnam Japan Guide</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{meta_keywords}">
  <meta name="robots" content="index, follow">
  <meta property="og:title" content="{data["title"]}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{og_url}">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="../../css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{headline}","description":"{meta_desc.split('。')[0]}。","datePublished":"{today}","dateModified":"{today}","author":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"publisher":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"inLanguage":"ja"}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {{"@type":"ListItem","position":1,"name":"トップページ","item":"https://vietnam-japan-guide.com/"}},
    {{"@type":"ListItem","position":2,"name":"{category_name}","item":"https://vietnam-japan-guide.com{category_url}"}},
    {{"@type":"ListItem","position":3,"name":"{headline}","item":"{og_url}"}
  ]}}</script>
  {faq_schema}
</head>
<body>
  <header class="header" role="banner">
    <div class="header__inner">
      <a href="/" class="header__logo"><span class="header__logo-icon" aria-hidden="true">VN</span>Vietnam Japan Guide</a>
      <nav class="header__nav">
        <ul class="header__nav-list">
{nav_html}        </ul>
      </nav>
      <button class="header__menu-toggle" aria-label="メニュー"><span></span><span></span><span></span></button>
    </div>
  </header>

  <nav class="breadcrumb">
    <div class="container">
      <ol class="breadcrumb__list">
        <li class="breadcrumb__item"><a href="/">トップページ</a></li>
        <li class="breadcrumb__item"><a href="{category_url}">{category_name}</a></li>
        <li class="breadcrumb__item breadcrumb__item--current">{headline}</li>
      </ol>
    </div>
  </nav>

  <article class="article-content">
    <div class="container">
      <h1>{headline}</h1>
      <div class="info-box info-box--warning">
        <div class="info-box__title">&#x26a0;&#xfe0f; おことわり</div>
        <p>この記事は、出入国在留管理庁などの公的機関が公開している公式情報をもとに解説しています。当サイトは法律専門家ではなく、正確な判断が必要な場合は必ず出入国在留管理庁または行政書士・弁護士などの専門家にご確認ください。</p>
      </div>
      <div class="info-box">
        <div class="info-box__title"><span class="icon">&#x1f4dd;</span> この記事のポイント</div>
        <p>{meta_desc}</p>
      </div>

      <div class="toc">
        <div class="toc__title">&#x1f4d1; 目次</div>
        <ul class="toc__list">
{toc_items}        </ul>
      </div>

{sections_html}
      <div class="cta-banner">
{cta_content}
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

    # Fix JSON escaping
    html = html.replace('{{', '{').replace('}}', '}')

    return html

def generate_all():
    """Generate all 30 articles"""
    count = 0

    for slug, data in ARTICLES_30.items():
        print(f"Generating: {slug} - {data['title']}")

        # Determine section generator
        if slug == "visa-skeleton-01":
            sections = make_sections_visa01()
        elif slug == "visa-skeleton-02":
            sections = make_sections_visa02()
        elif slug == "visa-skeleton-03":
            sections = make_sections_visa03()
        else:
            # Generic sections generator
            sections = {
                "基本情報と概要": f"""
<p>{data['title'].split('｜')[0]}について、出入国在留管理庁などの公的機関が公開している公式情報をもとに詳しく解説します。</p>
<h3>この記事でわかること</h3>
<ul>
  <li>手続きの基本条件と必要書類</li>
  <li>申請から許可までの流れと審査期間</li>
  <li>注意点と失敗しないためのポイント</li>
  <li>専門家に相談すべきケース</li>
</ul>
<p>正確な判断が必要な場合は、必ず出入国在留管理庁または行政書士・弁護士などの専門家にご確認ください。</p>
""",
                "必要書類と手続きの流れ": """
<p>申請に必要な書類は以下の通りです。</p>
<h3>必要な書類</h3>
<ul>
  <li><strong>パスポート</strong>：原本と写し（現在有効なもの）</li>
  <li><strong>在留カード</strong>：原本と写し（両面）</li>
  <li><strong>申請書</strong>：出入国在留管理庁の公式サイトからダウンロード</li>
  <li><strong>写真</strong>：縦4cm×横3cm、1枚（申請前3ヶ月以内に撮影）</li>
  <li><strong>収入証明書類</strong>：源泉徴収票、課税証明書、納税証明書など</li>
</ul>
<h3>手続きの流れ</h3>
<ol>
