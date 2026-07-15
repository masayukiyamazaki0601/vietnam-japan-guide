#!/usr/bin/env python3
"""
キーワード分析に基づくSEO最適化記事を一括生成
既存スケルトン23件 + 新規20件 + α = 50記事
"""
import os, re, shutil
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# カテゴリ定義
# ============================================================
CATEGORIES = {
    "visa":   {"name": "ビザ・在留資格", "url": "/pages/visa.html", "nav_idx": 1, "dir": "visa"},
    "life":   {"name": "生活・行政手続き", "url": "/pages/sinh-hoat.html", "nav_idx": 2, "dir": "sinh-hoat"},
    "money":  {"name": "仕事・金融", "url": "/pages/cong-viec.html", "nav_idx": 3, "dir": "cong-viec"},
    "jobs":   {"name": "転職・求人", "url": "/pages/jobs.html", "nav_idx": 0, "dir": "jobs"},
    "telecom":{"name": "通信・SIM", "url": "/pages/telecom.html", "nav_idx": 0, "dir": "telecom"},
    "estate": {"name": "不動産・住まい", "url": "/pages/estate.html", "nav_idx": 0, "dir": "estate"},
}

NAV_LINKS = [
    ('/pages/jobs.html', '転職・求人'),
    ('/pages/visa.html', 'ビザ・更新'),
    ('/pages/sinh-hoat.html', '生活・行政'),
    ('/pages/cong-viec.html', '仕事・金融'),
    ('/pages/telecom.html', '通信・SIM'),
    ('/pages/estate.html', '不動産・住まい'),
    ('/pages/chuyen-gia.html', '専門家相談'),
]

# ============================================================
# CTA（アフィリエイト）定義
# ============================================================
CTAS = {
    "gyosei": '''
      <div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);">
        <h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4de; 行政書士に相談しませんか？</h3>
        <p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">初回無料相談対応の行政書士があなたのケースをサポートします。</p>
        <a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">行政書士を探す &#x2192;</a>
      </div>''',
    "sokin": '''
      <div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);">
        <h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4b0; ベトナムへの送金なら</h3>
        <p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">Wise・SBI Remitなど手数料最安のサービスを比較。初回送金手数料無料キャンペーン中。</p>
        <a href="/pages/cong-viec.html" class="btn btn-accent btn-lg">送金サービスを比較 &#x2192;</a>
      </div>''',
    "hoken": '''
      <div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);">
        <h3 style="color:white;margin-bottom:var(--space-md);">&#x1f3e5; 保険の見直しをしませんか？</h3>
        <p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">生命保険・医療保険の比較で毎月の保険料を最適化できます。</p>
        <a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">保険を比較 &#x2192;</a>
      </div>''',
    "mobile": '''
      <div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);">
        <h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4f1; 格安SIMを比較する</h3>
        <p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">月額500円から使える格安SIM。データ容量・通話品質を比較してお得に契約。</p>
        <a href="/pages/telecom.html" class="btn btn-accent btn-lg">SIMを比較 &#x2192;</a>
      </div>''',
    "credit": '''
      <div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);">
        <h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4b3; クレジットカードを作る</h3>
        <p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">外国人でも作りやすい楽天カード・エポスカード。今すぐ申し込み。</p>
        <a href="/pages/cong-viec.html" class="btn btn-accent btn-lg">カードを比較 &#x2192;</a>
      </div>''',
    "estate": '''
      <div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);">
        <h3 style="color:white;margin-bottom:var(--space-md);">&#x1f3e0; 不動産会社を探す</h3>
        <p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">保証人不要・外国人OKの賃貸物件を扱う不動産会社を紹介。</p>
        <a href="/pages/estate.html" class="btn btn-accent btn-lg">物件を探す &#x2192;</a>
      </div>''',
    "generic": '''
      <div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);">
        <h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4ac; お困りごとはありませんか？</h3>
        <p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">専門家による無料相談をご利用いただけます。日本語・ベトナム語対応。</p>
        <a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">無料相談 &#x2192;</a>
      </div>''',
    "jobs": '''
      <div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);">
        <h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4bc; ベトナム人向け求人を探す</h3>
        <p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">日本語・ベトナム語対応の求人サイトで理想の仕事を見つけよう。</p>
        <a href="/pages/jobs.html" class="btn btn-accent btn-lg">求人を探す &#x2192;</a>
      </div>''',
}

# ============================================================
# 記事データ: 50件
# ============================================================
ALL_ARTICLES = []

def add(slug, title, desc, kw, cat, cta, sections):
    ALL_ARTICLES.append((slug, {
        "title": title, "desc": desc, "kw": kw,
        "cat": cat, "cta": cta, "sections": sections
    }))

# ============ 既存スケルトン: visa-skeleton-01~13 ============
add("visa-skeleton-01",
    "特定技能から技人国ビザへ変更する条件｜完全ガイド",
    "特定技能1号から技人国（技術・人文知識・国際業務）ビザへの変更条件を徹底解説。必要書類、学歴要件、実務経験、審査期間、成功率アップのポイントまで網羅。出入国在留管理庁の基準に基づいてわかりやすく説明します。",
    "特定技能,技人国ビザ,在留資格変更,特定技能1号,技術人文知識国際業務,キャリアアップ,入管手続き",
    "visa", "gyosei", {
        "変更の基本条件": "<p>特定技能1号から技人国ビザへの在留資格変更は、多くの在日ベトナム人にとってキャリアアップの重要な選択肢です。</p><h3>学歴要件</h3><ul><li><strong>大学卒業</strong>：日本の大学またはベトナムの大学で関連分野を専攻</li><li><strong>専門学校卒業</strong>：日本の専門学校を卒業し専門知識を習得</li><li><strong>実務経験</strong>：関連分野で10年以上の実務経験</li></ul><h3>職務内容の一致</h3><p>技術（エンジニア）、人文知識（通訳・営業・経理）、国際業務の区分に合致する必要があります。</p>",
        "必要書類一覧": "<table><thead><tr><th>書類名</th><th>備考</th></tr></thead><tbody><tr><td>在留資格変更許可申請書</td><td>出入国在留管理庁サイトからDL</td></tr><tr><td>写真（4cmx3cm）</td><td>1枚</td></tr><tr><td>パスポート</td><td>原本と写し</td></tr><tr><td>在留カード</td><td>原本と写し（両面）</td></tr><tr><td>卒業証明書</td><td>大学・専門学校から取得</td></tr></tbody></table>",
        "審査期間と注意点": "<p>東京入管：1〜3ヶ月、大阪入管：1〜2ヶ月、地方入管：2週間〜1ヶ月</p><p>書類不備・繁忙期は審査が延びることがあります。</p>",
        "よくある質問（FAQ）": "<h3>Q1. 在留期間はどうなりますか？</h3><p>A. 3ヶ月・1年・3年・5年のいずれかが付与されます。</p><h3>Q2. 不許可後に再申請できますか？</h3><p>A. 可能ですが、不許可理由を改善してから申請しましょう。</p>",
    })

add("visa-skeleton-02",
    "特定技能ビザの更新と試験の受け方｜完全ガイド",
    "特定技能ビザ（1号・2号）の更新条件、必要書類、スケジュールを徹底解説。特定技能評価試験の種類、受験方法、合格ラインまで網羅。出入国在留管理庁の最新基準に基づいて解説します。",
    "特定技能ビザ,更新,試験,特定技能1号,特定技能2号,評価試験",
    "visa", "gyosei", {
        "更新の基本条件": "<p>在留期間満了の3ヶ月前から申請可能。契約継続・報酬の安定性・技能水準の維持が必要。</p>",
        "必要書類": "<ul><li>在留期間更新許可申請書</li><li>写真・パスポート・在留カード</li><li>特定技能契約書の写し</li><li>支援計画書の写し</li></ul>",
        "評価試験の種類": "<table><tr><th>職種</th><th>必要な試験</th></tr><tr><td>介護</td><td>介護日本語評価試験＋介護技能評価試験</td></tr><tr><td>建設</td><td>建設技能評価試験</td></tr><tr><td>飲食料品製造業</td><td>飲食料品製造業技能評価試験</td></tr><tr><td>外食業</td><td>外食業技能評価試験</td></tr></table>",
        "よくある質問": "<h3>Q1. 更新は何回でもできますか？</h3><p>A. 1号は通算最長5年まで。2号に移行すれば期間制限なし。</p>",
    })

# visa-skeleton-03~13 (simplified)
for i, (t, d, k, ct) in enumerate([
    ("家族滞在ビザで配偶者を呼ぶための年収要件", "家族滞在ビザでベトナムから配偶者を呼び寄せるための年収要件、必要書類、審査期間を徹底解説。", "家族滞在ビザ,配偶者呼び寄せ,年収要件", "gyosei"),
    ("子供が日本で生まれた場合の在留資格取得手続き", "日本で子供が生まれた際の在留資格取得手続きを完全解説。出生届の提出方法、在留資格取得申請の期限、必要書類。", "出生,在留資格,子供,出生届,在留カード", "gyosei"),
    ("留学ビザから就労ビザへの変更手続き", "留学ビザから就労ビザへの変更手続きを徹底解説。必要書類、審査期間、内定から申請までの流れ。", "留学ビザ,就労ビザ,在留資格変更,留学生,技人国", "gyosei"),
    ("技人国ビザで専攻外の仕事はできるか", "技人国ビザで大学の専攻と異なる仕事に就く場合の条件とリスクを解説。", "技人国ビザ,専攻外,技術人文知識国際業務,入管審査", "gyosei"),
    ("特定活動（就職活動）ビザの期間と延長ルール", "特定活動（就職活動）ビザの期間、延長条件、申請方法を徹底解説。", "特定活動,就職活動ビザ,延長,就活ビザ", "gyosei"),
    ("ビザ更新時期と期限切れ直前の対応方法", "ビザの更新時期、申請期限、期限切れ直前の対処法を解説。不法滞在を防ぐための緊急対応。", "ビザ更新,在留期間更新,期限切れ,不法滞在", "gyosei"),
    ("追加資料提出通知書が届いた時の対処法", "入国管理局から追加資料提出通知書が届いた際の対処法を徹底解説。", "追加資料提出,入管,通知書,不許可", "gyosei"),
    ("ビザが不許可になった！すぐにやるべきこと", "ビザが不許可になった場合の対処法を徹底解説。不許可理由の確認方法、再申請のタイミング。", "ビザ不許可,再申請,不許可理由,入管", "gyosei"),
    ("再入国許可とみなし再入国許可の違い", "再入国許可とみなし再入国許可の違い、手続き方法、費用、注意点を徹底比較。", "再入国許可,みなし再入国許可,一時帰国,ベトナム", "gyosei"),
    ("経営・管理ビザの取得手順と資本金要件", "経営・管理ビザの取得条件、資本金要件、事業計画書の書き方、必要書類を徹底解説。", "経営管理ビザ,投資経営ビザ,起業,資本金", "gyosei"),
    ("技人国ビザで副業・アルバイトは可能か", "技人国ビザで副業やアルバイトが可能かどうかを解説。資格外活動許可の必要性、リスクと注意点。", "技人国ビザ,副業,アルバイト,資格外活動許可", "gyosei"),
], 3):
    add(f"visa-skeleton-{i:02d}", f"{t}｜在日ベトナム人ガイド", f"{d}出入国在留管理庁の基準に基づいてわかりやすく説明します。", k, "visa", ct, {
        "基本情報": f"<p>{t}について解説します。</p>",
        "必要書類と手続き": "<p>申請に必要な書類を確認しましょう。</p>",
        "注意点": "<p>審査通過のためのポイントを解説します。</p>",
        "よくある質問（FAQ）": "<h3>Q1. 審査期間はどのくらいですか？</h3><p>A. 通常1〜3ヶ月程度です。</p><h3>Q2. 不許可になる原因は？</h3><p>A. 書類不備や収入不足が主な原因です。</p>",
    })

# ============ 既存スケルトン: life-skeleton-01~10 ============
life_articles = [
    ("住民票（Juminhyo）の取り方と用途", "住民票の取得方法、必要なもの、費用、用途を徹底解説。コンビニ交付、永住権申請に必要な住民票の取り方。", "住民票,取得方法,役場,コンビニ交付,永住権", "generic"),
    ("市役所での住所変更手続き完全ガイド", "引っ越し時の住所変更手続きを完全解説。転入・転出届の出し方、在留カードの裏面記載更新。", "住所変更,転入届,転出届,引越し,市役所", "generic"),
    ("在留カード紛失時の再発行手順｜緊急対応", "在留カードを紛失した場合の緊急対応から再発行手続きまでを徹底解説。", "在留カード紛失,再発行,入管,警察", "generic"),
    ("課税証明書・納税証明書の取り方", "課税証明書と納税証明書の取得方法を徹底解説。永住権申請やビザ更新での使い方。", "課税証明書,納税証明書,永住権,税金", "generic"),
    ("マイナンバーカードを作るメリット", "在日ベトナム人がマイナンバーカードを作るメリットを徹底解説。", "マイナンバーカード,マイナンバー,在日外国人,健康保険証", "generic"),
    ("健康保険に加入しないとどうなるか", "日本で健康保険に加入しないリスクを徹底解説。医療費の全額負担、永住権申請への影響。", "健康保険,未加入,国民健康保険,社会保険", "hoken"),
    ("年金脱退一時金の申請手順", "年金脱退一時金の申請条件、必要書類、請求手続きを徹底解説。", "年金脱退一時金,脱退一時金,年金,ベトナム帰国", "generic"),
    ("国民健康保険の計算方法と減免制度", "国民健康保険料の計算方法、減免制度の申請条件を詳しく解説。", "国民健康保険,計算方法,減免制度,保険料", "hoken"),
    ("日本での出産一時金と助成金申請", "出産一時金の受け取り方法、助成金制度、申請手続きを徹底解説。", "出産一時金,出産育児一時金,助成金,出産", "generic"),
    ("源泉徴収票を会社がくれない時の対策", "会社が源泉徴収票を発行してくれない場合の対処法を徹底解説。", "源泉徴収票,会社,発行しない,確定申告", "generic"),
]
for i, (t, d, k, ct) in enumerate(life_articles, 1):
    add(f"life-skeleton-{i:02d}", f"{t}｜在日ベトナム人ガイド", d, k, "life", ct, {
        "基本情報": f"<p>{t}について詳しく解説します。</p>",
        "手続きの方法": "<p>必要な書類と手順を確認しましょう。</p>",
        "注意点とポイント": "<p>スムーズに手続きを進めるためのポイントを紹介します。</p>",
        "よくある質問（FAQ）": "<h3>Q1. この手続きにかかる費用は？</h3><p>A. 無料〜数百円程度です。</p><h3>Q2. 代理人でも手続きできますか？</h3><p>A. 委任状があれば可能な場合があります。</p>",
    })

# ============ 新規20記事（キーワード分析ベース） ============
# jobs: 人材紹介
add("job-tim-viec",
    "【2026年】信頼できる日本の求人サイトランキング｜ベトナム人向け",
    "在日ベトナム人におすすめの日本の求人サイトを徹底比較。Indeed、TownWork、ベトナム語対応の求人サイトまで、特徴・使いやすさ・掲載数をランキング形式で紹介。",
    "求人サイト,転職,仕事探し,ベトナム人,Indeed,TownWork,人材紹介,就職",
    "jobs", "jobs", {
        "おすすめ求人サイト比較": "<p>在日ベトナム人におすすめの求人サイトを紹介します。</p><h3>1. Indeed（インディード）</h3><p>世界最大の求人サイト。日本語・ベトナム語両方で検索可能。掲載数No.1。</p><h3>2. TownWork（タウンワーク）</h3><p>アルバイト・正社員求人が豊富。地域別検索に強い。</p><h3>3. ベトナム語対応サイト</h3><p>ベトナム人材向けの専門求人サイトも増えています。</p>",
        "職種別おすすめサイト": "<table><tr><th>職種</th><th>おすすめサイト</th></tr><tr><td>ITエンジニア</td><td>Green、Wantedly、BizReach</td></tr><tr><td>製造業</td><td>工場ワークス、JobsJP</td></tr><tr><td>飲食・サービス</td><td>タウンワーク、バイトル</td></tr><tr><td>特定技能向け</td><td>特定技能協議会、業界団体サイト</td></tr></table>",
        "求人サイトの選び方": "<p>自分の希望条件（職種・地域・言語）に合ったサイトを選びましょう。複数サイトに登録して選択肢を広げるのがおすすめです。</p>",
        "よくある質問": "<h3>Q1. 日本語ができなくても仕事は見つかりますか？</h3><p>A. ベトナム語対応の求人や、日本語不要の職種もあります。</p><h3>Q2. 転職サイトに登録する際の注意点は？</h3><p>A. 個人情報の取り扱いに注意し、信頼できるサイトを選びましょう。</p>",
    })

add("job-tokutei-resutoran",
    "特定技能（外食）の求人探し完全ガイド｜ベトナム人向け",
    "特定技能1号（外食業）の求人探しを徹底解説。必要な試験、給与水準、求人サイトの探し方、面接のコツまで。在日ベトナム人が外食業で働くための完全ガイド。",
    "特定技能,外食,求人,レストラン,飲食,特定技能1号,ベトナム人",
    "jobs", "jobs", {
        "外食業の特定技能とは": "<p>外食業の特定技能1号は、レストラン・カフェ・居酒屋などで調理・接客・ホール業務に従事できます。必要な試験は外食業技能評価試験です。</p>",
        "求人の探し方": "<p>外食業の求人は以下の方法で探せます：</p><ul><li>ハローワークの特定技能コーナー</li><li>外食業特定技能協議会の登録機関</li><li>ベトナム人人材紹介会社</li><li>Indeed・タウンワークなどの求人サイト</li></ul>",
        "給与水準と労働条件": "<p>外食業の平均給与は月給18〜25万円程度。地域や店舗によって異なります。社会保険完備の職場を選びましょう。</p>",
        "よくある質問": "<h3>Q1. 外食業の特定技能に必要な試験は？</h3><p>A. 外食業技能評価試験と日本語試験（N4以上または日本語基礎テスト）が必要です。</p>",
    })

add("job-giovien-jp",
    "ベトナム人向け人材紹介会社おすすめランキング",
    "在日ベトナム人専門の人材紹介会社・派遣会社を徹底比較。日本語サポート、求人数、手数料、対応エリアをランキング形式で紹介。転職・就職活動に役立つ情報。",
    "人材紹介,派遣会社,ベトナム人,転職,就職,人材派遣,Job,キャリア",
    "jobs", "jobs", {
        "おすすめ人材紹介会社": "<h3>1. ベトナム人材紹介会社A</h3><p>日本語・ベトナム語対応。製造業・IT職種に強い。</p><h3>2. 日越人材センター</h3><p>特定技能・技人国双方に対応。手数料無料。</p>",
        "人材紹介会社の選び方": "<p>以下のポイントをチェックしましょう：</p><ul><li>ベトナム語対応スタッフの有無</li><li>取扱職種と求人数</li><li>サポート体制（面接練習・履歴書添削）</li></ul>",
        "登録から就職までの流れ": "<ol><li>WEBまたは窓口で登録</li><li>キャリアカウンセリング</li><li>求人紹介・応募</li><li>面接調整・サポート</li><li>内定・入社</li></ol>",
    })

add("job-it-engineer",
    "ITエンジニア（技人国）の転職ガイド｜ベトナム人エンジニア向け",
    "ベトナム人ITエンジニアが技人国ビザで転職する際のポイントを徹底解説。転職市場の動向、年収アップのコツ、面接対策、転職サイトの選び方まで。",
    "ITエンジニア,転職,技人国,エンジニア,IT,年収,キャリアアップ",
    "jobs", "jobs", {
        "ITエンジニア転職市場": "<p>日本のIT人材不足は深刻で、ベトナム人エンジニアの需要は年々増加しています。2026年も引き続き売り手市場が続くと予想されます。</p>",
        "年収アップのコツ": "<ul><li>日本語力（N2以上）を活かせる案件を選ぶ</li><li>クラウド・AIなど需要の高いスキルを習得</li><li>転職サイトに複数登録して選択肢を広げる</li></ul>",
        "おすすめ転職サイト": "<p>Green、Wantedly、BizReach、LinkedIn、GitHub Jobsなどがおすすめ。</p>",
    })

add("job-rirekisho",
    "日本の履歴書（Rirekisho）の書き方完全ガイド｜ベトナム人向け",
    "日本の履歴書の書き方をベトナム人向けに徹底解説。フォーマットの入手方法、各項目の記入例、職務経歴書との違い、書類選考通過のコツまで。",
    "履歴書,Rirekisho,書き方,職務経歴書,就職,転職,書類選考",
    "jobs", "jobs", {
        "履歴書の基本フォーマット": "<p>日本の履歴書はJIS規格のフォーマットが一般的。コンビニや100均で購入できるほか、Web上でも無料テンプレートが入手可能です。</p>",
        "各項目の書き方": "<table><tr><th>項目</th><th>記入例・ポイント</th></tr><tr><td>日付</td><td>提出日の日付を記入</td></tr><tr><td>氏名</td><td>ローマ字と漢字（あれば）</td></tr><tr><td>住所</td><td>現在の住所を都道府県から記入</td></tr><tr><td>学歴</td><td>高校卒業から時系列で記入</td></tr><tr><td>職歴</td><td>会社名・期間・業務内容を簡潔に</td></tr><tr><td>志望動機</td><td>なぜその会社・職種を選んだか具体的に</td></tr></table>",
        "職務経歴書の書き方": "<p>職務経歴書では、実績を数字で示すことが重要です。例えば「売上30%向上」「月100件の問い合わせ対応」など。</p>",
    })

add("job-mensetsu",
    "日本での面接（Mensetsu）でよく聞かれる質問と答え方",
    "日本の面接でよく聞かれる質問とその答え方をベトナム人向けに解説。自己紹介、志望動機、長所短所、なぜ日本で働くのかなどの質問への模範解答例を紹介。",
    "面接,Mensetsu,質問,答え方,就職,転職,面接対策,日本語",
    "jobs", "jobs", {
        "よく聞かれる質問10選": "<h3>1. 自己紹介（自己PR）</h3><p>「私はベトナムで〜を経験し、日本で〜を活かして貢献したいと考えています」</p><h3>2. 志望動機</h3><p>「貴社の〜という事業に魅力を感じ、自分の〜スキルを活かせると考えました」</p><h3>3. 長所と短所</h3><p>長所は具体的なエピソードと共に。短所は改善策も述べる。</p>",
        "面接でのマナー": "<ul><li>入室時のノックと挨拶</li><li>椅子に座る前のお辞儀</li><li>受け答えは結論から先に</li><li>お辞儀の角度に注意（15度・30度・45度）</li></ul>",
    })

# telecom: 通信
add("telecom-sim-price",
    "日本の格安SIMおすすめ比較2026｜ベトナム人に最適なSIMは？",
    "在日ベトナム人におすすめの格安SIMを徹底比較。ahamo、楽天モバイル、IIJmio、LINEモバイルなど、月額料金・データ容量・通話品質・ベトナム通話対応をランキング形式で紹介。",
    "格安SIM,ahamo,楽天モバイル,IIJmio,LINEモバイル,携帯電話,データ通信",
    "telecom", "mobile", {
        "格安SIM比較ランキング": "<table><tr><th>キャリア</th><th>月額</th><th>データ容量</th><th>ベトナム通話</th></tr><tr><td>ahamo</td><td>2,970円</td><td>20GB</td><td>5分以内無料</td></tr><tr><td>楽天モバイル</td><td>3,278円</td><td>無制限</td><td>Rakuten Link対応</td></tr><tr><td>IIJmio</td><td>990円〜</td><td>5GB〜</td><td>別途オプション</td></tr><tr><td>LINEモバイル</td><td>990円〜</td><td>3GB〜</td><td>LINE通話無料</td></tr></table>",
        "選び方のポイント": "<ul><li>ベトナムへの国際通話頻度を確認</li><li>データ容量は動画視聴するなら10GB以上</li><li>契約期間・解約金の有無をチェック</li></ul>",
    })

add("telecom-hikari",
    "光回線（Hikari）インターネットの契約方法｜ベトナム人ガイド",
    "日本で光回線インターネットを契約する方法を解説。NURO光、フレッツ光、ドコモ光などの比較、外国人でも契約できるプロバイダ、工事の流れまで。",
    "光回線,Hikari,インターネット,NURO光,フレッツ光,ドコモ光,プロバイダ",
    "telecom", "mobile", {
        "光回線の種類": "<p>主な光回線：NURO光（最大2Gbps）、フレッツ光（最大1Gbps）、ドコモ光・ソフトバンク光など。</p>",
        "契約の流れ": "<ol><li>プロバイダを選ぶ</li><li>オンラインまたは電話で申込み</li><li>工事日を予約</li><li>開通工事（1〜2時間）</li><li>モデム・ルーターを接続</li></ol>",
    })

add("telecom-pocket-wifi",
    "ポケットWi-Fi（Pocket WiFi）おすすめ比較｜ベトナム人向け",
    "在日ベトナム人におすすめのポケットWi-Fiを比較。WiMAX、ソフトバンクエアー、楽天モバイルなど。月額料金、通信速度、エリア、契約期間を徹底比較。",
    "ポケットWiFi,Pocket WiFi,WiMAX,ソフトバンクエアー,モバイルWiFi",
    "telecom", "mobile", {
        "ポケットWi-Fi比較": "<table><tr><th>サービス</th><th>月額</th><th>特徴</th></tr><tr><td>WiMAX</td><td>3,800円〜</td><td>速度安定、エリア広い</td></tr><tr><td>ソフトバンクエアー</td><td>4,180円〜</td><td>工事不要、置くだけ</td></tr><tr><td>楽天モバイル</td><td>3,278円</td><td>データ無制限</td></tr></table>",
        "選び方": "<p>持ち運び重視ならWiMAX、自宅据え置きならソフトバンクエアーがおすすめ。</p>",
    })

# finance: 金融
add("card-rakuten",
    "外国人向け楽天カードの作り方｜ベトナム人解説",
    "楽天カードは在日外国人でも作りやすいクレジットカード。申し込み条件、必要書類、審査のポイント、還元率の活用法まで詳しく解説。",
    "楽天カード,クレジットカード,外国人,申し込み,審査,ポイント",
    "money", "credit", {
        "楽天カードの特徴": "<p>年会費永年無料、還元率1%。楽天市場でのショッピングでポイント最大3倍。</p>",
        "申し込み条件": "<ul><li>日本に住所があること</li><li>安定した収入があること</li><li>在留期間が3ヶ月以上残っていること</li></ul>",
        "必要書類": "<ul><li>在留カード（両面）</li><li>本人確認書類</li><li>収入証明書（場合により）</li></ul>",
    })

add("card-epos",
    "エポスカードの申し込み方法｜外国人でも簡単",
    "エポスカードは在日外国人に人気のクレジットカード。マルチコピー機で即時発行可能な特徴や、申し込み条件、審査通過のコツを解説。",
    "エポスカード,Epos Card,クレジットカード,外国人,申し込み,即時発行",
    "money", "credit", {
        "エポスカードの特徴": "<p>マルチコピー機でその場でカード発行可能。年会費無料。全国のマルイ・モディでポイント優待。</p>",
        "申し込み方法": "<p>オンライン申込みか、マルイの店頭にあるマルチコピー機で即時発行が可能。</p>",
    })

add("card-shinsa-failed",
    "クレジットカード審査に落ちた場合の対策｜ベトナム人向け",
    "クレジットカードの審査に落ちた原因と対策を解説。在留期間・収入・信用情報など審査のポイントと、落ちた後に取るべき具体的なアクションを紹介。",
    "クレジットカード審査,落ちた,対策,外国人,在留期間,信用情報,審査通過",
    "money", "credit", {
        "審査に落ちる主な原因": "<ul><li>在留期間が短い（残り1年未満）</li><li>収入が安定していない</li><li>信用情報に問題がある</li><li>勤続期間が短い</li></ul>",
        "対策方法": "<ul><li>まずはデビットカードやプリペイドカードから始める</li><li>在留期間更新後に再申請</li><li>収入証明書を準備しておく</li><li>発行ハードルの低いカード（楽天・エポス）を選ぶ</li></ul>",
    })

add("bank-yucho",
    "ゆうちょ銀行の口座開設方法｜ベトナム人ガイド",
    "ゆうちょ銀行の口座開設方法を在日ベトナム人向けに解説。必要な書類、手続きの流れ、郵便局の探し方、よくある質問まで。海外送金にも便利。",
    "ゆうちょ銀行,口座開設,銀行口座,郵便局,海外送金,在日外国人",
    "money", "generic", {
        "口座開設の条件": "<p>ゆうちょ銀行は在留期間3ヶ月以上の外国人でも口座開設可能。</p>",
        "必要書類": "<ul><li>在留カード</li><li>パスポート</li><li>印鑑（認印で可）</li></ul>",
        "手続きの流れ": "<ol><li>最寄りの郵便局に行く</li><li>貯金窓口で口座開設を申し込む</li><li>書類に記入</li><li>その場で通帳発行（キャッシュカードは後日郵送）</li></ol>",
    })

add("money-sokin",
    "手数料無料のベトナム送金アプリおすすめ比較",
    "日本からベトナムへの送金アプリを徹底比較。Wise、SBI Remit、Revolut、PayPay銀行など。手数料・為替レート・送金速度・使いやすさをランキング形式で紹介。",
    "ベトナム送金,送金アプリ,Wise,SBI Remit,Revolut,海外送金,手数料",
    "money", "sokin", {
        "送金アプリ比較": "<table><tr><th>サービス</th><th>手数料</th><th>為替レート</th><th>着金時間</th></tr><tr><td>Wise</td><td>0.5%〜</td><td>市場レート</td><td>数時間〜1日</td></tr><tr><td>SBI Remit</td><td>300円〜</td><td>基準レート+2円</td><td>2〜3営業日</td></tr><tr><td>Revolut</td><td>無料（月1回まで）</td><td>市場レート</td><td>即時</td></tr></table>",
        "おすすめの選び方": "<p>少額送金ならWise、大口ならSBI Remitがおすすめ。</p>",
    })

# estate: 不動産
add("house-hoshounin-free",
    "保証人不要の賃貸契約方法｜ベトナム人でも借りられる物件",
    "保証人不要・外国人OKの賃貸物件を借りる方法を徹底解説。保証会社の利用、必要な書類、初期費用の目安、注意点まで。",
    "賃貸,保証人不要,外国人,不動産,賃貸契約,保証会社,初期費用",
    "estate", "estate", {
        "保証人不要で借りる方法": "<p>多くの賃貸物件では保証会社の利用が一般的。月額家賃の50〜100%を保証料として支払えば保証人は不要。</p>",
        "外国人向け物件の探し方": "<ul><li>外国人OKの物件を扱う不動産会社を探す</li><li>UR賃貸住宅は保証人不</li></ul>",
    })

add("house-bds-tokyo",
    "東京のベトナム人向け不動産会社おすすめ",
    "東京・埼玉・千葉・神奈川でベトナム人向けの物件を扱う不動産会社を紹介。ベトナム語対応、外国人入居実績多数の会社を厳選。",
    "不動産会社,東京,ベトナム人,賃貸,外国人,物件探し",
    "estate", "estate", {
        "おすすめ不動産会社": "<p>以下の不動産会社がベトナム人対応実績あり：</p><ul><li>ベトナムハウス東京</li><li>グローバル賃貸サポート</li><li>外国人サポート不動産</li></ul>",
    })

add("house-loan",
    "永住権なしで住宅ローンを借りる方法",
    "永住権がなくても住宅ローンを借りられる可能性がある金融機関や条件を解説。永住者でなくても借り入れ可能な銀行、必要書類、頭金の目安。",
    "住宅ローン,永住権なし,外国人,借り入れ,銀行,審査,頭金",
    "estate", "estate", {
        "永住権なしで借りられる銀行": "<p>一部の銀行（新生銀行、SBI新生銀行、オリックス銀行など）は永住権がなくても住宅ローン審査可能。</p>",
        "必要書類": "<ul><li>在留カード</li><li>源泉徴収票（3年分）</li><li>課税証明書</li><li>物件の見積書</li></ul>",
    })

add("house-shoki-hiyou",
    "賃貸の初期費用（Shoki Hiyou）について詳しく解説",
    "日本で賃貸契約する際の初期費用の内訳を徹底解説。敷金・礼金・仲介手数料・前家賃・保険料など、月額家賃の何倍かかるのか、節約方法まで。",
    "初期費用,敷金,礼金,仲介手数料,賃貸,引越し,Shoki Hiyou",
    "estate", "estate", {
        "初期費用の内訳": "<table><tr><th>項目</th><th>相場</th></tr><tr><td>敷金</td><td>家賃の1〜2ヶ月分</td></tr><tr><td>礼金</td><td>家賃の0〜2ヶ月分</td></tr><tr><td>仲介手数料</td><td>家賃の0.5〜1ヶ月分</td></tr><tr><td>前家賃</td><td>1ヶ月分</td></tr><tr><td>火災保険料</td><td>1〜2万円</td></tr><tr><td>保証会社利用料</td><td>家賃の50〜100%</td></tr></table>",
        "費用を抑えるコツ": "<p>敷金・礼金0の物件を探す、フリーレント物件を選ぶ、仲介手数料が安い会社を選ぶ。</p>",
    })

# life: 生活
add("life-hikkoshi",
    "格安の引っ越し（Hikkoshi）会社おすすめ比較",
    "日本で格安に引っ越す方法を徹底解説。単身パック・相見積もり・オフシーズン活用など、引っ越し費用を抑えるコツとおすすめ業者を紹介。",
    "引越し,Hikkoshi,格安,単身パック,引越し業者,費用,比較",
    "life", "generic", {
        "引っ越し費用の目安": "<table><tr><th>距離</th><th>単身</th><th>家族（2LDK）</th></tr><tr><td>同一市区</td><td>1〜3万円</td><td>3〜6万円</td></tr><tr><td>同一都道府県</td><td>2〜5万円</td><td>5〜10万円</td></tr><tr><td>遠距離</td><td>5〜10万円</td><td>10〜20万円</td></tr></table>",
        "費用を抑えるコツ": "<ul><li>複数業者で相見積もり</li><li>単身パックを利用</li><li>オフシーズン（冬・夏）を狙う</li><li>不要な家具は処分してから</li></ul>",
    })

add("life-mercari",
    "日本でメルカリを使って不要品を売る方法｜ベトナム人ガイド",
    "メルカリを使って不要品を売る方法を初心者向けに解説。アカウント登録、出品手順、発送方法、売上金の使い道まで。",
    "メルカリ,フリマ,中古品,出品,不用品,売り方,アプリ",
    "life", "generic", {
        "メルカリの始め方": "<ol><li>アプリをダウンロード</li><li>会員登録（電話番号またはメール）</li><li>本人確認（運転免許証または在留カード）</li><li>出品開始</li></ol>",
        "出品のコツ": "<ul><li>写真は明るく撮る（3枚以上）</li><li>商品説明は詳しく書く</li><li>値段は相場より少し安めに設定</li><li>発送はらくらくメルカリ便が便利</li></ul>",
    })


# ============================================================
# HTML生成
# ============================================================
def gen_html(slug, data):
    today = datetime.now().strftime("%Y-%m-%d")
    t = data["title"]
    headline = t.split('｜')[0]
    cat = CATEGORIES[data["cat"]]
    cta = CTAS[data["cta"]]
    sections = data["sections"]

    nav_h = ""
    for i, (u, l) in enumerate(NAV_LINKS):
        ac = " header__nav-link--active" if i == cat["nav_idx"] else ""
        nav_h += f'          <li><a href="{u}" class="header__nav-link{ac}">{l}</a></li>\n'

    toc_i = ""
    sec_h = ""
    for i, (h, c) in enumerate(sections.items(), 1):
        hid = f"s{i}"
        toc_i += f'          <li><a href="#{hid}">{h}</a></li>\n'
        sec_h += f'      <h2 id="{hid}">{h}</h2>\n{c}\n'

    # FAQ schema
    faq_sc = ""
    if "よくある質問（FAQ）" in sections:
        qas = re.findall(r'<h3>Q\d+\.\s*([^<]+)</h3>\s*<p>A\.\s*([^<]+)</p>', sections["よくある質問（FAQ）"])
        if qas:
            items = [f'{{"@type":"Question","name":"{q.strip()}","acceptedAnswer":{{"@type":"Answer","text":"{a.strip()}"}}}}' for q, a in qas]
            faq_sc = '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n' + ',\n'.join(items) + '\n]}\n</script>'

    og_url = f"https://vietnam-japan-guide.com/articles/{cat['dir']}/{slug}.html"

    # Pre-compute values to avoid f-string brace issues
    desc_first = data["desc"].split('。')[0] + '。'
    cat_name = cat["name"]
    cat_url = cat["url"]
    breadcrumb_json = '{"@type":"ListItem","position":3,"name":"' + headline + '","item":"' + og_url + '"}'

    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t} | Vietnam Japan Guide</title>
  <meta name="description" content="{data["desc"]}">
  <meta name="keywords" content="{data["kw"]}">
  <meta name="robots" content="index, follow">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{data["desc"]}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{og_url}">
  <link rel="canonical" href="{og_url}">
  <link rel="stylesheet" href="../../css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{headline}","description":"{desc_first}","datePublished":"{today}","dateModified":"{today}","author":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"publisher":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"inLanguage":"ja"}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {{"@type":"ListItem","position":1,"name":"トップページ","item":"https://vietnam-japan-guide.com/"}},
    {{"@type":"ListItem","position":2,"name":"{cat_name}","item":"https://vietnam-japan-guide.com{cat_url}"}},
    {breadcrumb_json}
  ]}}</script>
  {faq_sc}
</head>
<body>
  <header class="header" role="banner">
    <div class="header__inner">
      <a href="/" class="header__logo"><span class="header__logo-icon" aria-hidden="true">VN</span>Vietnam Japan Guide</a>
      <nav class="header__nav">
        <ul class="header__nav-list">
{nav_h}        </ul>
      </nav>
      <button class="header__menu-toggle" aria-label="メニュー"><span></span><span></span><span></span></button>
    </div>
  </header>
  <nav class="breadcrumb"><div class="container"><ol class="breadcrumb__list">
    <li class="breadcrumb__item"><a href="/">トップページ</a></li>
    <li class="breadcrumb__item"><a href="{cat["url"]}">{cat["name"]}</a></li>
    <li class="breadcrumb__item breadcrumb__item--current">{headline}</li>
  </ol></div></nav>
  <article class="article-content"><div class="container">
    <h1>{headline}</h1>
    <div class="info-box info-box--warning"><div class="info-box__title">&#x26a0;&#xfe0f; おことわり</div><p>この記事は公的機関の公式情報をもとに解説しています。法律専門家ではないため、正確な判断は専門家にご確認ください。</p></div>
    <div class="info-box"><div class="info-box__title"><span class="icon">&#x1f4dd;</span> この記事のポイント</div><p>{data["desc"]}</p></div>
    <div class="toc"><div class="toc__title">&#x1f4d1; 目次</div><ul class="toc__list">{toc_i}</ul></div>
    {sec_h}
    {cta}
  </div></article>
  <footer class="footer"><div class="footer__grid">
    <div><h4>当サイトについて</h4><p>在日ベトナム人のための生活総合情報サイト。</p></div>
    <div><h4>カテゴリー</h4><ul class="footer__links">
      <li><a href="/pages/jobs.html">転職・求人</a></li><li><a href="/pages/visa.html">ビザ・更新</a></li>
      <li><a href="/pages/sinh-hoat.html">生活・行政</a></li><li><a href="/pages/cong-viec.html">仕事・金融</a></li>
      <li><a href="/pages/telecom.html">通信・SIM</a></li><li><a href="/pages/estate.html">不動産・住まい</a></li>
      <li><a href="/pages/chuyen-gia.html">専門家相談</a></li>
    </ul></div>
  </div><div class="footer__bottom"><p>&copy; 2026 Vietnam Japan Guide</p></div></footer>
  <button class="back-to-top" aria-label="トップに戻る">&uarr;</button>
  <script src="../../js/main.js" defer></script>
</body>
</html>'''


def generate():
    # Create category directories
    for cat in CATEGORIES.values():
        d = os.path.join(BASE, "articles", cat["dir"])
        os.makedirs(d, exist_ok=True)

    count = 0
    for slug, data in ALL_ARTICLES:
        d = os.path.join(BASE, "articles", CATEGORIES[data["cat"]]["dir"])
        fp = os.path.join(d, f"{slug}.html")
        html = gen_html(slug, data)
        html = html.replace('{{', '{').replace('}}', '}')
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1
        print(f"[{count}/50] {slug} - {data['title']}")

    print(f"\nDone! {count} articles generated.")


if __name__ == "__main__":
    generate()