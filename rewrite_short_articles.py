#!/usr/bin/env python3
"""71-77行のショート記事を150-200行の長文に書き直す"""
import os, re
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

ARTICLES = {}
def set_article(slug, title, desc, kw, cat, sections):
    ARTICLES[slug] = {"title": title, "desc": desc, "kw": kw, "cat": cat, "sections": sections}

# ===== 1. credit-card-shinsa - クレジットカード審査（金融） =====
set_article("credit-card-shinsa",
    "外国人でも通るクレジットカード審査のコツ｜在日ベトナム人向け完全ガイド",
    "在日ベトナム人がクレジットカード審査に通るためのポイントを徹底解説。審査基準、落ちる原因、通過するための条件、おすすめカード、在留期間と収入の関係、申し込みのタイミングまで詳しく説明。",
    "クレジットカード,審査,外国人,ベトナム人,在留期間,収入,通過条件",
    "cong-viec",
    {"クレジットカード審査の基本": """
<p>在日外国人がクレジットカードを作るのは、日本人よりもハードルが高いと言われています。しかし、審査の基準を理解し、適切な準備をすれば十分に通過可能です。</p>
<h3>審査で重視されるポイント</h3>
<table><tr><th>項目</th><th>重要度</th><th>詳細</th></tr>
<tr><td>在留期間</td><td>最重要</td><td>残りの在留期間が1年以上あること</td></tr>
<tr><td>収入</td><td>重要</td><td>安定した収入があり、日本人と同等以上であること</td></tr>
<tr><td>勤続年数</td><td>重要</td><td>同じ職場で1年以上勤務していること</td></tr>
<tr><td>在留資格</td><td>普通</td><td>永住者・定住者・技人国が有利。特定技能・留学はやや厳しい</td></tr></table>
""",
    "審査に落ちる主な原因": """
<h3>在留期間が短い</h3>
<p>最も多い不通過理由。在留カードの残存期間が1年未満だと審査に通りにくくなります。更新後に再申請しましょう。</p>
<h3>収入が不安定</h3>
<p>アルバイトや派遣社員の場合、正社員より審査が厳しくなります。源泉徴収票で2〜3年の安定した収入を示せるかがポイント。</p>
<h3>勤続期間が短い</h3>
<p>転職したばかりの場合は、最低でも3ヶ月以上経ってから申し込むのがベターです。</p>
<h3>信用情報に問題</h3>
<p>過去の支払い遅延や債務整理があると審査に通りません。まずは信用情報機関（CIC・JICC）で自分の情報を確認しましょう。</p>""",
    "外国人におすすめのクレジットカード": """
<h3>1. 楽天カード</h3><p>年会費永年無料、還元率1%。在留期間が残り3ヶ月以上あれば申し込み可能な場合が多い。</p>
<h3>2. エポスカード</h3><p>マルイのマルチコピー機で即時発行可能。在留期間1年以上が望ましい。</p>
<h3>3. イオンカード</h3><p>イオングループでの買い物に便利。留学生でも作りやすい。</p>""",
    "審査通過率を上げる方法": """
<p>以下の方法で審査通過率を上げられます：</p>
<ol>
<li>在留期間更新後に申し込む（残り2年以上がベスト）</li>
<li>安定した収入があることを証明する（源泉徴収票を提出）</li>
<li>まずはデビットカードやプリペイドカードから始める</li>
<li>キャッシング枠は0円で申し込む</li>
<li>申し込みは1社ずつ行う（複数同時申し込みは逆効果）</li>
</ol>""",
    "よくある質問（FAQ）": """
<h3>Q1. 在留期間が1年未満でも審査に通ることはありますか？</h3><p>A. まれに通る場合もありますが、基本的には在留期間更新後に申し込むことをおすすめします。</p>
<h3>Q2. 留学生でもクレジットカードは作れますか？</h3><p>A. 作れるカードは限られますが、イオンカードや楽天カードは留学生でも申し込み実績があります。</p>
<h3>Q3. 審査に落ちた場合、どのくらい期間を空けて再申請すべきですか？</h3><p>A. 最低でも3ヶ月以上空けましょう。改善点を明確にしてから再申請することが重要です。</p>
<h3>Q4. 家族カードは作りやすいですか？</h3><p>A. 本会員（日本人または在留期間の長い外国人）がいる場合、家族カードは審査が緩和されます。</p>"""
})

# ===== 2. kenko-hoken-shikumi - 健康保険の仕組み =====
set_article("kenko-hoken-shikumi",
    "日本の健康保険の仕組みを完全解説｜在日ベトナム人向けガイド",
    "日本の健康保険制度（国民健康保険・社会健康保険）の仕組みをベトナム人向けに徹底解説。加入方法、保険料の計算、医療費の負担割合、保険証の使い方、病院のかかり方まで詳しく説明。",
    "健康保険,国民健康保険,社会保険,医療費,保険証,病院,加入方法",
    "sinh-hoat",
    {"健康保険制度の基礎知識": """
<p>日本には<strong>国民皆保険制度</strong>があり、すべての住民が何らかの健康保険に加入する義務があります。在日外国人も例外ではありません。</p>
<h3>健康保険の種類</h3>
<table><tr><th>種類</th><th>対象</th><th>保険料</th></tr>
<tr><td>国民健康保険</td><td>自営業者、フリーランス、無職、会社員以外</td><td>前年の所得と世帯人数で計算</td></tr>
<tr><td>社会健康保険</td><td>会社員（正社員・派遣社員）</td><td>標準報酬月額に応じて計算。会社が半分負担</td></tr>
<tr><td>後期高齢者医療制度</td><td>75歳以上</td><td>年金から天引き</td></tr></table>
<h3>加入義務と罰則</h3>
<p>健康保険に加入しない場合、医療費が全額自己負担（10割）になります。また、市区町村から督促状が届き、最終的には財産差し押さえのリスクもあります。永住権申請時にも健康保険の加入状況がチェックされるため、必ず加入しましょう。</p>""",
    "保険料の計算方法": """
<h3>国民健康保険の場合</h3>
<p>以下の要素で計算されます：<br>
保険料 = 所得割（前年の所得に応じて）+ 均等割（加入者数に応じて）+ 平等割（世帯ごとに固定額）</p>
<h3>社会健康保険の場合</h3>
<p>標準報酬月額に保険料率をかけて計算。2026年の保険料率は約9〜10%（会社と折半のため実質負担は約5%）</p>
<h3>保険料を抑える方法</h3>
<ul>
<li>所得が低い場合は減免制度を申請する</li>
<li>社会健康保険は会社が半分負担するため、国民健康保険より負担が軽いことが多い</li>
<li>家族を扶養に入れると、扶養家族分の保険料は発生しない（社会健康保険の場合）</li>
</ul>""",
    "病院のかかり方と医療費": """
<h3>病院に行く流れ</h3>
<ol>
<li>保険証を持って医療機関を受診する</li>
<li>初診時に保険証と身分証明証を提示</li>
<li>診察を受ける</li>
<li>会計時に保険証があれば医療費の3割のみ支払い</li>
</ol>
<h3>医療費の負担割合</h3>
<ul>
<li>6歳未満：医療費の2割負担</li>
<li>6歳〜69歳：医療費の3割負担</li>
<li>70歳〜74歳：医療費の2割負担（現役並み所得者は3割）</li>
<li>75歳以上：医療費の1割負担</li>
</ul>
<h3>高額療養費制度</h3>
<p>1ヶ月の医療費が上限額を超えた場合、超えた分が後日払い戻される制度です。上限額は所得に応じて異なります。</p>""",
    "よくある質問（FAQ）": """
<h3>Q1. 健康保険に加入しないとどうなりますか？</h3><p>A. 医療費が全額自己負担になるほか、市区町村から督促、最終的に財産差し押さえのリスクがあります。</p>
<h3>Q2. 転職した場合、健康保険はどうなりますか？</h3><p>A. 退職後は国民健康保険に切り替える必要があります。新しい職場では再加入手続きをします。</p>
<h3>Q3. ベトナムに一時帰国する場合、健康保険はどうなりますか？</h3><p>A. 1年以上の海外在留でない限り、健康保険の資格は継続されます。</p>
<h3>Q4. 家族を扶養に入れると保険料は上がりますか？</h3><p>A. 社会健康保険の場合、扶養家族の保険料は追加でかかりません。</p>"""
})

# ===== 3. telecom-line-mobile - LINEモバイル =====
set_article("telecom-line-mobile",
    "LINEモバイルの契約・設定・使い方完全ガイド｜ベトナム人におすすめの理由",
    "LINEモバイルの料金プラン、申し込み方法、開通手続き、LINE通話無料のメリットを徹底解説。他社との比較、ベトナムとの連絡に最適な理由、よくあるトラブルと解決方法も紹介。",
    "LINEモバイル,格安SIM,LINE通話,月額料金,データ通信,ベトナム連絡",
    "telecom",
    {"LINEモバイルとは": """
<p>LINEモバイルは、LINE株式会社が提供する格安SIMサービスです。最大の特徴は<strong>LINEアプリの通信がデータ消費ゼロ</strong>なこと。在日ベトナム人がベトナムの家族や友人とLINEで連絡する際に非常に便利です。</p>
<h3>LINEモバイルの基本情報</h3>
<table><tr><th>項目</th><th>内容</th></tr>
<tr><td>回線</td><td>ドコモ回線</td></tr>
<tr><td>月額料金</td><td>990円〜（3GBプラン）</td></tr>
<tr><td>データ容量</td><td>3GB / 6GB / 15GB / 30GB</td></tr>
<tr><td>LINE通信</td><td>データ消費ゼロ（テキスト・通話・ビデオ）</td></tr>
<tr><td>契約期間</td><td>なし（いつでも解約可能）</td></tr></table>""",
    "料金プラン比較": """
<h3>料金プラン一覧</h3>
<table><tr><th>プラン</th><th>月額料金</th><th>データ容量</th><th>LINE利用</th></tr>
<tr><td>ベーシック3GB</td><td>990円</td><td>3GB</td><td>カウントフリー</td></tr>
<tr><td>ベーシック6GB</td><td>1,650円</td><td>6GB</td><td>カウントフリー</td></tr>
<tr><td>ベーシック15GB</td><td>2,090円</td><td>15GB</td><td>カウントフリー</td></tr>
<tr><td>ベーシック30GB</td><td>3,300円</td><td>30GB</td><td>カウントフリー</td></tr></table>
<h3>他社との比較</h3>
<p>楽天モバイル（3,278円/無制限）と比較するとデータ容量は少ないですが、LINEヘビーユーザーならLINEモバイルの方が実質的にお得です。</p>""",
    "申し込みから開通までの流れ": """
<h3>申し込み手順</h3>
<ol>
<li>LINEモバイル公式サイトから申し込む</li>
<li>本人確認書類（在留カード）をアップロード</li>
<li>SIMカードが自宅に届く（2〜5日）</li>
<li>自分でSIMカードを挿入し、APN設定を行う</li>
<li>開通完了（最短即日）</li>
</ol>
<h3>必要なもの</h3>
<ul>
<li>在留カード（両面の写真またはスキャン）</li>
<li>パスポート（本人確認用）</li>
<li>LINEアカウント</li>
<li>クレジットカードまたはキャリア決済</li>
</ul>""",
    "よくある質問（FAQ）": """
<h3>Q1. ベトナムから持ってきたスマホでも使えますか？</h3><p>A. SIMロックフリーの端末であれば使用可能です。ただし、対応バンドを確認してください。</p>
<h3>Q2. LINEモバイルから他社に乗り換える場合、解約金はかかりますか？</h3><p>A. 契約期間の縛りがないので解約金はかかりません。</p>
<h3>Q3. ベトナムへの国際電話はかけられますか？</h3><p>A. LINEアプリの通話機能を使えば無料です。通常の電話回線を使う場合は有料です。</p>"""
})

# ===== 4. life-nihongo - 日本語学習 =====
set_article("life-nihongo",
    "在日ベトナム人の日本語学習完全ガイド｜独学から日本語学校までのロードマップ",
    "在日ベトナム人のための日本語学習方法を段階別に解説。初心者向けおすすめアプリ、日本語学校の選び方、JLPT対策、ビジネス日本語習得法、学習計画の立て方まで完全網羅。",
    "日本語学習,日本語学校,JLPT,ベトナム人,独学,アプリ,Nihongo",
    "sinh-hoat",
    {"日本語学習の全体像": """
<p>日本で生活・仕事をするためには日本語力が不可欠です。日本語レベルによって学習アプローチを変えましょう。</p>
<h3>日本語レベル別の目標</h3>
<table><tr><th>レベル</th><th>目安</th><th>学習時間</th></tr>
<tr><td>初心者（N5相当）</td><td>簡単な挨拶、ひらがな・カタカナ</td><td>150〜300時間</td></tr>
<tr><td>初級（N4相当）</td><td>日常会話、簡単な読み書き</td><td>300〜600時間</td></tr>
<tr><td>中級（N3相当）</td><td>複雑な会話、一般的な文章</td><td>600〜900時間</td></tr>
<tr><td>中上級（N2相当）</td><td>ビジネス会話、新聞が読める</td><td>900〜1,200時間</td></tr>
<tr><td>上級（N1相当）</td><td>高度な日本語運用</td><td>1,200時間以上</td></tr></table>""",
    "おすすめ学習アプリとツール": """
<h3>1. Duolingo</h3><p>無料でゲーム感覚で学べる。ベトナム語から日本語を学べるコースあり。初心者に最適。</p>
<h3>2. みんなの日本語（アプリ版）</h3><p>日本語学校で使われる定番テキストのアプリ版。文法を体系的に学べる。</p>
<h3>3. Anki（暗記カードアプリ）</h3><p>単語帳アプリ。自分でカードを作成して効率的に語彙力アップ。</p>
<h3>4. リアルな日本語に触れる</h3>
<ul>
<li>YouTube：日本語学習チャンネルを活用</li>
<li>Netflix：日本語字幕で日本のドラマ・アニメを見る</li>
<li>Podcast：通勤中に日本語の音声を聞く</li>
</ul>""",
    "日本語学校の選び方": """
<h3>日本語学校を選ぶポイント</h3>
<ul>
<li><strong>立地</strong>：自宅から通いやすい場所にあるか</li>
<li><strong>時間</strong>：仕事と両立できる夜間コースがあるか</li>
<li><strong>サポート</strong>：ベトナム人スタッフがいるか</li>
<li><strong>カリキュラム</strong>：JLPT対策コースがあるか</li>
<li><strong>費用</strong>：入学金・授業料が予算内か（年間60〜80万円程度）</li>
</ul>
<h3>日本語学校に通うメリット</h3>
<ol>
<li>体系的なカリキュラムで効率的に学習できる</li>
<li>日本人教師から直接指導を受けられる</li>
<li>他の外国人学生との交流でモチベーション維持</li>
<li>JLPT受験のサポートが受けられる</li>
<li>ビザ取得・更新のサポート（留学ビザの場合）</li>
</ol>""",
    "JLPT対策": """
<h3>JLPT（日本語能力試験）の重要性</h3>
<p>JLPTは日本で最も認知度の高い日本語試験です。N2以上を取得すると以下のメリットがあります：</p>
<ul>
<li>ビザ更新・変更で有利に働く</li>
<li>転職・就職活動で評価される</li>
<li>大学・専門学校への入学資格を得られる</li>
<li>永住権申請時に日本語能力の証明になる</li>
</ul>
<h3>効率的な対策方法</h3>
<ol>
<li>公式問題集を繰り返し解く</li>
<li>聴解は毎日30分以上のリスニング</li>
<li>読解は日本語の記事や新聞を毎日読む</li>
<li>語彙はAnkiアプリで毎日100語ずつ暗記</li>
</ol>""",
    "よくある質問（FAQ）": """
<h3>Q1. 独学と日本語学校、どちらが効果的ですか？</h3><p>A. 独学は費用がかからない反面、モチベーション維持が難しいです。予算に余裕があれば日本語学校をおすすめします。</p>
<h3>Q2. JLPT N2に合格するにはどのくらい時間がかかりますか？</h3><p>A. ゼロから始めて約1年半〜2年（900〜1,200時間の学習）が目安です。</p>
<h3>Q3. 仕事をしながら日本語を学ぶコツは？</h3><p>A. 通勤時間の活用（30分×往復=1日1時間）と、職場での日本人との積極的な会話が効果的です。</p>
<h3>Q4. ベトナム語で日本語を教えてくれる学校はありますか？</h3><p>A. 一部の日本語学校にはベトナム人スタッフが在籍しています。新宿・大久保エリアに多いです。</p>"""
})

# ===== 5. life-kurashi - 生活費 =====
set_article("life-kurashi",
    "在日ベトナム人の生活費ガイド｜東京・大阪・地方の費用比較と節約術",
    "日本で生活するベトナム人が知っておくべき生活費の内訳を徹底解説。東京・大阪・地方都市の家賃・食費・光熱費の比較、月々の支出目安、効果的な節約方法、お金の管理術まで。",
    "生活費,家計,節約,光熱費,食費,家賃,支出,東京,大阪",
    "sinh-hoat",
    {"生活費の地域別比較": """
<p>日本での生活費は住む地域によって大きく異なります。</p>
<h3>月々の生活費目安（単身者）</h3>
<table><tr><th>項目</th><th>東京</th><th>大阪</th><th>地方都市</th></tr>
<tr><td>家賃</td><td>7〜12万円</td><td>5〜8万円</td><td>3〜5万円</td></tr>
<tr><td>食費</td><td>3〜5万円</td><td>3〜4万円</td><td>2.5〜3.5万円</td></tr>
<tr><td>光熱費</td><td>1〜2万円</td><td>1〜1.5万円</td><td>1〜1.5万円</td></tr>
<tr><td>通信費</td><td>0.5〜1万円</td><td>0.5〜1万円</td><td>0.5〜1万円</td></tr>
<tr><td>交通費</td><td>1〜2万円</td><td>0.5〜1.5万円</td><td>0.3〜1万円</td></tr>
<tr><td>保険料</td><td>1〜2万円</td><td>1〜2万円</td><td>1〜2万円</td></tr>
<tr><td><strong>合計</strong></td><td><strong>13.5〜24万円</strong></td><td><strong>11〜18万円</strong></td><td><strong>8.3〜14万円</strong></td></tr></table>""",
    "項目別節約術": """
<h3>家賃を抑える方法</h3>
<ul>
<li>駅から離れた物件を選ぶ（徒歩10分以上で家賃が1〜2万円安くなる）</li>
<li>シェアハウスを利用する（初期費用も安く、家具家電付き）</li>
<li>UR賃貸を利用する（保証人不要、更新料なし、仲介手数料なし）</li>
</ul>
<h3>食費を抑える方法</h3>
<ul>
<li>業務スーパーでまとめ買いする（一般的なスーパーより2〜3割安い）</li>
<li>自炊を基本とする（外食1食＝自炊3食分のコスト）</li>
<li>タイムセールを活用する（夕方以降の値引き品を狙う）</li>
</ul>
<h3>光熱費を抑える方法</h3>
<ul>
<li>格安電力会社に乗り換える（毎月500〜1,000円節約）</li>
<li>エアコンは設定温度を夏28度・冬20度に</li>
<li>LED電球に交換する</li>
</ul>""",
    "お金の管理術": """
<h3>効果的な家計管理方法</h3>
<ol>
<li><strong>収支を把握する</strong>：家計簿アプリ（マネーフォワードなど）で毎月の収支を記録</li>
<li><strong>固定費を見直す</strong>：保険、通信費、サブスクリプションを定期的に見直す</li>
<li><strong>予算を決める</strong>：収入の50%を生活費、20%を貯金、30%を趣味・交際費に配分</li>
<li><strong>自動積立を設定する</strong>：毎月の給料日に自動で貯金口座に振り替え</li>
</ol>""",
    "よくある質問（FAQ）": """
<h3>Q1. 東京と大阪、どちらが生活しやすいですか？</h3><p>A. 家賃・食費は大阪の方が安いですが、求人数は東京の方が多いです。</p>
<h3>Q2. 毎月どのくらい貯金できますか？</h3><p>A. 東京で月5〜10万円、地方で月10〜15万円が目安です。</p>
<h3>Q3. 生活費を抑えるためにシェアハウスはおすすめですか？</h3><p>A. 初期費用を抑えられ、日本人との交流もできるため、最初の住まいとしておすすめです。</p>"""
})

# ===== 6. haiguusha-raiyu-toroku - 配偶者呼び寄せ =====
set_article("haiguusha-raiyu-toroku",
    "配偶者（家族）を日本に呼び寄せる方法｜在留資格・手続き完全ガイド",
    "在日ベトナム人が配偶者や子供を日本に呼び寄せるための在留資格申請手続きを完全解説。家族滞在ビザの条件、必要書類、収入要件、審査期間、不許可リスクと対策まで詳しく説明。",
    "配偶者呼び寄せ,家族滞在,在留資格,扶養,年収要件,必要書類",
    "sinh-hoat",
    {"家族滞在ビザの基本条件": """
<h3>対象となる家族</h3>
<p>以下の家族を呼び寄せることができます：</p>
<ul>
<li><strong>配偶者</strong>：法律上の結婚関係にあるパートナー</li>
<li><strong>子</strong>：実子（養子含む場合あり）</li>
</ul>
<h3>在日側の在留資格</h3>
<p>家族を呼び寄せることができる在留資格は限られています：</p>
<ul>
<li>技術・人文知識・国際業務（技人国）</li>
<li>経営・管理ビザ</li>
<li>特定技能2号（1号では不可）</li>
<li>永住者ビザ</li>
<li>日本人の配偶者等ビザ</li>
</ul>
<h3>収入要件</h3>
<p>年収300万円以上（月収25万円以上）が一般的な目安。正社員での安定収入が最も有利で、アルバイト収入のみでは不許可リスクが高まります。</p>""",
    "必要書類と手続きの流れ": """
<h3>在日側の必要書類</h3>
<ul>
<li>在留資格変更許可申請書</li>
<li>パスポート（写し）・在留カード（写し）</li>
<li>源泉徴収票（直近2〜3年分）</li>
<li>課税証明書・納税証明書</li>
<li>住民票（世帯全員の記載があるもの）</li>
<li>雇用証明書・在職証明書</li>
</ul>
<h3>ベトナム側の必要書類</h3>
<ul>
<li>パスポート（原本と写し）</li>
<li>結婚証明書（日本語訳付き）</li>
<li>家族登録証明書</li>
<li>健康診断証明書</li>
</ul>
<h3>手続きの流れ</h3>
<ol>
<li>書類準備（約1ヶ月）</li>
<li>入国管理局に申請</li>
<li>審査（東京：1〜3ヶ月、地方：2週間〜1ヶ月）</li>
<li>許可後、在留カードを受領</li>
</ol>""",
    "審査通過のポイントと不許可対策": """
<h3>審査でチェックされるポイント</h3>
<ul>
<li>収入の安定性と扶養能力</li>
<li>結婚の真实性（偽装結婚でないこと）</li>
<li>住居の広さ（家族で暮らせる十分な広さか）</li>
<li>在日側の納税状況</li>
<li>過去の在留状況（オーバーステイ歴の有無）</li>
</ul>
<h3>不許可の場合の対策</h3>
<ul>
<li>不許可理由を確認し、改善する</li>
<li>収入不足の場合は預貯金の証明を追加</li>
<li>結婚の真实性を証明する資料（写真・交際経緯書）を充実させる</li>
<li>行政書士に相談して再申請する</li>
</ul>""",
    "よくある質問（FAQ）": """
<h3>Q1. 特定技能1号でも家族を呼び寄せられますか？</h3><p>A. 特定技能1号では家族の呼び寄せはできません。特定技能2号または技人国への変更が必要です。</p>
<h3>Q2. 配偶者が呼び寄せられた後、アルバイトはできますか？</h3><p>A. 資格外活動許可を申請すれば週28時間以内で就労可能です。</p>
<h3>Q3. 呼び寄せた家族は健康保険に入れますか？</h3><p>A. 扶養家族として在日側の健康保険に加入できます。</p>"""
})

# ===== 7. telecom-rakuten-mobile - 楽天モバイル =====
set_article("telecom-rakuten-mobile",
    "楽天モバイルの契約・設定・活用ガイド｜ベトナム人に最適な格安SIM",
    "楽天モバイルの料金プラン、申し込み方法、Rakuten Linkの使い方、データ無制限のメリットを徹底解説。他社との比較、よくあるトラブルと解決方法、ベトナム通話の活用術まで。",
    "楽天モバイル,Rakuten,格安SIM,データ無制限,月額料金,Rakuten Link",
    "telecom",
    {"楽天モバイルの魅力": """
<p>楽天モバイルは月額3,278円（税込）で<strong>データ通信が実質無制限</strong>になる画期的な格安SIMです。</p>
<h3>基本情報</h3>
<table><tr><th>項目</th><th>内容</th></tr>
<tr><td>月額料金</td><td>3,278円（税込）</td></tr>
<tr><td>データ容量</td><td>実質無制限（20GB超過後も最大1Mbps）</td></tr>
<tr><td>通話</td><td>Rakuten Linkアプリで国内通話無料</td></tr>
<tr><td>回線</td><td>楽天回線（一部エリアはパートナー回線）</td></tr>
<tr><td>契約期間</td><td>縛りなし</td></tr></table>""",
    "料金プランの詳細": """
<h3>データ容量と料金</h3>
<table><tr><th>データ容量</th><th>月額料金</th><th>超過後</th></tr>
<tr><td>3GBまで</td><td>0円（実質無料）</td><td>-</td></tr>
<tr><td>3GB超〜20GB</td><td>1,078円</td><td>1Mbpsに制限</td></tr>
<tr><td>20GB超</td><td>3,278円</td><td>最大1Mbpsに制限（実質無制限）</td></tr></table>
<h3>Rakuten Linkのメリット</h3>
<p>Rakuten Linkアプリを使うと、国内通話が無料になるだけでなく、ベトナムへの国際通話も格安で利用できます。</p>""",
    "申し込みから開通まで": """
<ol>
<li>楽天モバイル公式サイトまたは楽天市場で申し込み</li>
<li>本人確認書類（在留カード）を提出</li>
<li>SIMカードまたはeSIMを取得</li>
<li>スマホにSIMを挿入し、APN設定</li>
<li>Rakuten Linkアプリをインストール</li>
</ol>
<h3>eSIM対応</h3>
<p>楽天モバイルはeSIMに対応しているため、物理SIMが不要で即日開通も可能です。</p>""",
    "よくある質問（FAQ）": """
<h3>Q1. 楽天モバイルはベトナム人の外国人でも申し込めますか？</h3><p>A. 在留期間が3ヶ月以上残っていれば申し込み可能です。</p>
<h3>Q2. データ無制限と言っても制限はありますか？</h3><p>A. 20GB超過後は最大1Mbpsに制限されますが、LINE・SNS・音楽ストリーミング程度なら問題なく使えます。</p>
<h3>Q3. 楽天回線のエリアはどのくらいですか？</h3><p>A. 都市部はほぼカバーされています。地方ではパートナー回線（au）を使用します。</p>"""
})

# ===== 8. life-byoin - 病院のかかり方 =====
set_article("life-byoin",
    "日本の病院のかかり方完全ガイド｜ベトナム人向け医療ナビ",
    "日本で病院にかかる方法をベトナム人向けに徹底解説。健康保険の使い方、診療科の選び方、予約方法、症状別の受診目安、医療費の支払い、日本語ができなくても受診できる方法まで。",
    "病院,医療,健康保険,診療,ベトナム人,医療費,診察,受診方法",
    "sinh-hoat",
    {"病院に行く前に知っておくこと": """
<h3>日本の医療制度の特徴</h3>
<ul>
<li><strong>保険証が必須</strong>：健康保険証がないと医療費が全額自己負担（10割）になります</li>
<li><strong>診療所と病院の違い</strong>：軽い症状は診療所（クリニック）、重い症状は病院を受診するのが一般的</li>
<li><strong>予約制</strong>：多くの医療機関は予約制です。予約なしでも受診できますが、待ち時間が長くなります</li>
<li><strong>薬は院外処方</strong>：病院で処方箋をもらい、薬局で薬を受け取るシステム</li>
</ul>""",
    "症状別の診療科一覧": """
<table><tr><th>症状</th><th>受診する診療科</th></tr>
<tr><td>発熱・風邪・喉の痛み</td><td>内科</td></tr>
<tr><td>腹痛・胃腸の不調</td><td>内科（消化器内科）</td></tr>
<tr><td>頭痛・めまい</td><td>内科（脳神経内科）</td></tr>
<tr><td>ケガ・骨折・腰痛</td><td>整形外科</td></tr>
<tr><td>歯の痛み</td><td>歯科</td></tr>
<tr><td>皮膚のかゆみ・発疹</td><td>皮膚科</td></tr>
<tr><td>子供の病気</td><td>小児科</td></tr>
<tr><td>女性の健康相談</td><td>婦人科</td></tr>
<tr><td>目のトラブル</td><td>眼科</td></tr>
<tr><td>耳・鼻のトラブル</td><td>耳鼻咽喉科</td></tr></table>""",
    "日本語ができなくても受診する方法": """
<h3>多言語対応の医療機関を探す</h3>
<ul>
<li>AMDA国際医療情報センター：電話通訳サービスあり</li>
<li>東京都医療機関案内サービス：多言語対応の病院を検索可能</li>
<li>医療通訳派遣サービス：市区町村によっては無料で医療通訳を派遣</li>
</ul>
<h3>受診時のポイント</h3>
<ul>
<li>症状をメモして持参する（ベトナム語と日本語で）</li>
<li>スマホの翻訳アプリを活用する</li>
<li>保険証と在留カードを必ず持参する</li>
<li>薬のアレルギーがある場合は事前に伝える</li>
</ul>""",
    "医療費と高額療養費制度": """
<h3>医療費の負担</h3>
<p>保険証があれば医療費の3割負担（6歳未満は2割、70歳以上は1〜2割）。<br>
例：診察料が10,000円の場合、自己負担は3,000円</p>
<h3>高額療養費制度</h3>
<p>1ヶ月の医療費が上限額を超えた場合、超えた分が払い戻されます。上限額は所得によって異なり、一般的な所得で約80,000円程度です。事前に「限度額適用認定証」を取得すれば、窓口での支払いを上限額までに抑えられます。</p>""",
    "よくある質問（FAQ）": """
<h3>Q1. 休日や夜間に病院に行きたい場合は？</h3><p>A. 休日診療所や救急医療機関があります。市区町村の広報で確認できます。緊急の場合は119番で救急車を呼べます。</p>
<h3>Q2. 薬は日本の薬局でしか買えませんか？</h3><p>A. 医師の処方箋が必要な薬は病院でもらった処方箋を薬局に持っていきます。市販薬（風邪薬・頭痛薬など）はドラッグストアで購入できます。</p>
<h3>Q3. 健康診断はどこで受けられますか？</h3><p>A. 会社員は年に1回の健康診断を会社が手配します。自営業の方は市区町村の特定健診を受けることができます。</p>"""
})

NAV = {"/pages/jobs.html":"転職・求人", "/pages/vinh-tru.html":"永住・帰化", "/pages/visa.html":"ビザ・更新", "/pages/sinh-hoat.html":"生活・行政", "/pages/cong-viec.html":"仕事・金融", "/pages/telecom.html":"通信・SIM", "/pages/estate.html":"不動産・住まい", "/pages/chuyen-gia.html":"専門家相談"}

CTAS = {
    "sinh-hoat": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4de; 行政書士に相談しませんか？</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">初回無料相談対応の行政書士がサポートします。</p><a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">行政書士を探す &#x2192;</a></div>',
    "cong-viec": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4b3; クレジットカードを比較する</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">外国人でも作りやすいカードをご紹介。</p><a href="/pages/cong-viec.html" class="btn btn-accent btn-lg">カードを比較 &#x2192;</a></div>',
    "telecom": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4f1; 格安SIMを比較する</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">月額500円から使える格安SIM。今すぐ比較。</p><a href="/pages/telecom.html" class="btn btn-accent btn-lg">SIMを比較 &#x2192;</a></div>',
}

DIRS = {"sinh-hoat":"sinh-hoat", "cong-viec":"cong-viec", "telecom":"telecom"}

def gen(slug, d):
    today = datetime.now().strftime("%Y-%m-%d")
    t = d["title"]; hl = t.split("｜")[0]
    cat = d["cat"]; sec = d["sections"]; kw = d["kw"]; desc = d["desc"]
    # nav
    nlist = list(NAV.items())
    ai = 3 if cat == "sinh-hoat" else (4 if cat == "cong-viec" else 5 if cat == "telecom" else 0)
    nav_h = ""
    for i, (u, l) in enumerate(nlist):
        ac = " header__nav-link--active" if i == ai else ""
        nav_h += f'          <li><a href="{u}" class="header__nav-link{ac}">{l}</a></li>\n'
    toc = ""; sh = ""
    for i, (h, c) in enumerate(sec.items(), 1):
        hid = f"s{i}"
        toc += f'          <li><a href="#{hid}">{h}</a></li>\n'
        sh += f'      <h2 id="{hid}">{h}</h2>\n{c}\n'
    ou = f"https://vietnam-japan-guide.com/articles/{DIRS[cat]}/{slug}.html"
    
    # FAQ schema
    faq = ""
    if "よくある質問（FAQ）" in sec:
        qas = re.findall(r"<h3>Q\d+\.\s*([^<]+)</h3>\s*<p>A\.\s*([^<]+)</p>", sec["よくある質問（FAQ）"])
        if qas:
            items = [f'{{"@type":"Question","name":"{q.strip()}","acceptedAnswer":{{"@type":"Answer","text":"{a.strip()}"}}}}' for q, a in qas]
            faq = '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n' + ",\n".join(items) + "\n]}\n</script>"
    
    cat_n = NAV.get(f"/pages/{cat}.html","生活・行政")
    bc = '{"@type":"ListItem","position":3,"name":"' + hl + '","item":"' + ou + '"}'
    df = desc.split("。")[0] + "。"
    
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{t} | Vietnam Japan Guide</title>
  <meta name="description" content="{desc}"><meta name="keywords" content="{kw}">
  <meta name="robots" content="index,follow">
  <meta property="og:title" content="{t}"><meta property="og:description" content="{desc}">
  <meta property="og:type" content="article"><meta property="og:url" content="{ou}">
  <link rel="canonical" href="{ou}"><link rel="stylesheet" href="../../css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{hl}","description":"{df}","datePublished":"{today}","dateModified":"{today}","author":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"publisher":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"inLanguage":"ja"}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {{"@type":"ListItem","position":1,"name":"トップページ","item":"https://vietnam-japan-guide.com/"}},
    {{"@type":"ListItem","position":2,"name":"{cat_n}","item":"https://vietnam-japan-guide.com/pages/{cat}.html"}},
    {bc}
  ]}}</script>
  {faq}
</head>
<body>
  <header class="header"><div class="header__inner">
    <a href="/" class="header__logo"><span class="header__logo-icon">VN</span>Vietnam Japan Guide</a>
    <nav class="header__nav"><ul class="header__nav-list">
{nav_h}    </ul></nav>
    <button class="header__menu-toggle"><span></span><span></span><span></span></button>
  </div></header>
  <nav class="breadcrumb"><div class="container"><ol class="breadcrumb__list">
    <li class="breadcrumb__item"><a href="/">トップページ</a></li>
    <li class="breadcrumb__item"><a href="/pages/{cat}.html">{cat_n}</a></li>
    <li class="breadcrumb__item breadcrumb__item--current">{hl}</li>
  </ol></div></nav>
  <article class="article-content"><div class="container">
    <h1>{hl}</h1>
    <div class="info-box info-box--warning"><div class="info-box__title">&#x26a0;&#xfe0f; おことわり</div><p>この記事は公的機関の公式情報をもとに解説しています。法律専門家ではないため、正確な判断は専門家にご確認ください。</p></div>
    <div class="info-box"><div class="info-box__title">&#x1f4dd; この記事のポイント</div><p>{desc}</p></div>
    <div class="toc"><div class="toc__title">&#x1f4d1; 目次</div><ul class="toc__list">{toc}</ul></div>
    {sh}
    {CTAS.get(cat, CTAS["sinh-hoat"])}
  </div></article>
  <footer class="footer"><div class="footer__grid">
    <div><h4>当サイトについて</h4><p>在日ベトナム人の生活総合情報サイト。</p></div>
    <div><h4>カテゴリー</h4><ul class="footer__links">
      <li><a href="/pages/jobs.html">転職・求人</a></li><li><a href="/pages/visa.html">ビザ・更新</a></li>
      <li><a href="/pages/sinh-hoat.html">生活・行政</a></li><li><a href="/pages/cong-viec.html">仕事・金融</a></li>
      <li><a href="/pages/telecom.html">通信・SIM</a></li><li><a href="/pages/estate.html">不動産・住まい</a></li>
      <li><a href="/pages/chuyen-gia.html">専門家相談</a></li>
    </ul></div>
  </div><div class="footer__bottom"><p>&copy; 2026 Vietnam Japan Guide</p></div></footer>
  <button class="back-to-top">&uarr;</button>
  <script src="../../js/main.js" defer></script>
</body>
</html>'''

cnt = 0
for slug, d in ARTICLES.items():
    h = gen(slug, d)
    h = h.replace("{{","{").replace("}}","}")
    cat = d["cat"]
    fp = os.path.join(BASE, "articles", DIRS[cat], f"{slug}.html")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(h)
    cnt += 1
    wc = len(h.split("\n"))
    print(f"[{cnt}] {slug} -> {wc}行")

print(f"Done! {cnt} articles rewritten")