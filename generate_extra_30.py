#!/usr/bin/env python3
"""追加30記事を生成"""
import os
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

NEW = []

def add(slug, title, desc, kw, cat, cta, sections):
    NEW.append((slug, {"title": title, "desc": desc, "kw": kw, "cat": cat, "cta": cta, "sections": sections}))

add("life-idp-unten", "国際運転免許証（IDP）の取得方法｜ベトナム人ガイド", "ベトナム人が日本で運転するための国際運転免許証の取得方法を解説。ベトナム免許からの切り替え、運転免許試験、必要書類まで。", "国際運転免許,IDP,運転免許,ベトナム人,車,運転,免許切り替え", "life", "generic", {"国際運転免許証の基礎知識": "<p>日本で外国人が運転するには国際運転免許証（IDP）が必要です。</p>", "取得手順": "<ol><li>運転免許センターで申請</li><li>適性検査</li><li>筆記試験</li><li>実技試験</li></ol>", "よくある質問（FAQ）": "<h3>Q1. ベトナムの免許は使えますか？</h3><p>A. 切り替えが必要です。</p>"})
add("life-byoin", "日本の病院のかかり方｜ベトナム人向け医療ガイド", "日本で病院にかかる方法をベトナム人向けに解説。健康保険の使い方、病院の選び方、予約方法、症状別の診療科。", "病院,医療,健康保険,診療,ベトナム人,医療費", "life", "hoken", {"病院のかかり方": "<p>健康保険証を持って病院に行きます。</p>", "診療科の選び方": "<table><tr><th>症状</th><th>診療科</th></tr><tr><td>発熱</td><td>内科</td></tr><tr><td>ケガ</td><td>整形外科</td></tr><tr><td>歯</td><td>歯科</td></tr></table>"})
add("life-nihongo", "在日ベトナム人のための日本語学習法｜おすすめアプリ・学校", "日本に住むベトナム人のための効果的な日本語学習方法を紹介。おすすめアプリ、日本語学校、独学方法、JLPT対策。", "日本語学習,日本語学校,JLPT,ベトナム人,勉強,アプリ", "life", "generic", {"おすすめ学習アプリ": "<p>Duolingo、みんなの日本語連動アプリが効果的。</p>", "日本語学校の選び方": "<p>夜間コースがある学校を選びましょう。</p>"})
add("life-taxi-ride", "日本でのタクシーの乗り方｜ベトナム人ガイド", "日本でのタクシーの正しい乗り方、料金システム、予約方法、配車アプリの使い方を解説。", "タクシー,Uber,配車アプリ,移動,交通,ベトナム人", "life", "generic", {"タクシーの乗り方": "<p>後ろのドアが自動で開きます。行き先を伝えましょう。</p>", "配車アプリ": "<p>Uber、GO、DiDiが便利。</p>"})
add("life-kurashi", "日本での生活費の内訳｜在日ベトナム人の家計管理術", "東京・大阪など主要都市の生活費の内訳を解説。家賃、食費、光熱費、通信費の目安と節約のコツ。", "生活費,家計,節約,光熱費,食費,家賃,支出", "life", "generic", {"月の生活費目安": "<p>東京単身：約15〜20万円/月、大阪：約12〜17万円/月</p>", "節約のコツ": "<p>格安SIM、自炊、業務スーパーの活用。</p>"})
add("life-konbini", "コンビニの便利な使い方｜ベトナム人ガイド", "日本のコンビニの便利な使い方を解説。公共料金支払い、ATM、コピー機、発送サービスまで。", "コンビニ,セブンイレブン,ファミマ,ローソン,公共料金", "life", "generic", {"コンビニのサービス": "<ul><li>公共料金支払い</li><li>ATM</li><li>コピー・FAX</li><li>宅配便発送</li></ul>"})
add("life-pet", "日本でのペットの飼い方｜ベトナム人ガイド", "日本で犬や猫を飼う際のルール、登録方法、ワクチン、費用、賃貸物件での注意点を解説。", "ペット,犬,猫,飼い方,賃貸,動物病院", "life", "generic", {"ペットを飼う前に": "<p>賃貸物件の多くはペット禁止。ペット可物件を探しましょう。</p>"})
add("life-recycle", "日本のゴミ出しルール完全ガイド｜ベトナム人向け", "日本のゴミの分別方法、出し方のルール、収集スケジュールの確認方法を解説。", "ゴミ,分別,リサイクル,燃えるゴミ,燃えないゴミ,収集日", "life", "generic", {"ゴミの分別方法": "<p>市区町村によってルールが異なります。役所で分別表をもらいましょう。</p>"})
add("life-nekkyo", "日本の暑さ対策・寒さ対策｜ベトナム人生活ガイド", "日本の夏の暑さ・冬の寒さ対策を解説。エアコンの使い方、節電方法、熱中症対策。", "暑さ対策,寒さ対策,熱中症,エアコン,節電,服装", "life", "generic", {"夏の対策": "<p>熱中症に注意。エアコンを適切に使いましょう。</p>", "冬の対策": "<p>室内の乾燥に注意。加湿器を使いましょう。</p>"})
add("life-kojin", "個人情報保護と在留カード管理｜ベトナム人向け", "在留カードの適切な管理方法、個人情報漏洩防止、紛失時の対応を解説。", "個人情報,在留カード,管理,紛失,セキュリティ", "life", "generic", {"在留カードの管理": "<p>常に携帯する義務があります。コピーを保管しておきましょう。</p>"})
add("car-shaken", "車検（Shaken）の基礎知識｜ベトナム人車オーナー向け", "日本で車を所有する際の車検制度を解説。費用の目安、頻度、整備工場の選び方。", "車検,Shaken,自動車,整備,車両点検,費用", "life", "generic", {"車検とは": "<p>新車初回3年、以降2年ごと。費用は10〜20万円程度。</p>"})
add("car-loan", "自動車ローンの組み方｜在日ベトナム人ガイド", "日本で自動車ローンを組む方法を解説。ローンの種類、金利、審査基準、必要書類。", "自動車ローン,車ローン,ローン審査,金利,分割払い", "money", "generic", {"自動車ローンの種類": "<p>ディーラーローン（金利2〜5%）、銀行ローン（金利1〜4%）</p>"})
add("edu-youchien", "日本の幼稚園・保育園の申し込み方法｜ベトナム人家族向け", "幼稚園・保育園・こども園の違い、申し込み方法、費用、保育料無償化制度を解説。", "幼稚園,保育園,こども園,保育,教育,子育て,無償化", "life", "generic", {"幼稚園と保育園の違い": "<p>幼稚園（3〜5歳、教育機関）、保育園（0〜5歳、保育施設）</p>"})
add("edu-daigaku", "ベトナム人留学生のための日本の大学進学ガイド", "日本の大学への進学方法を解説。留学生試験（EJU）、日本語能力試験、出願書類、奨学金。", "大学進学,留学生,EJU,奨学金,日本語学校,高等教育", "life", "generic", {"大学進学の流れ": "<p>日本語学校（1〜2年）→EJU受験→大学出願→入学</p>"})
add("money-nenkin", "日本の年金制度完全ガイド｜在日ベトナム人向け", "日本の年金制度の仕組み、加入方法、保険料、将来の受給額を解説。", "年金,国民年金,厚生年金,年金制度,保険料", "money", "hoken", {"年金制度の仕組み": "<p>20歳以上は国民年金に加入。会社員は厚生年金にも加入。</p>"})
add("money-zeikimushi", "税金の還付（還付申告）のやり方｜ベトナム人向け", "源泉徴収された税金の還付を受ける方法を解説。医療費控除、ふるさと納税、住宅ローン控除。", "還付申告,税金,医療費控除,ふるさと納税,確定申告", "money", "generic", {"還付を受けられるケース": "<p>医療費が10万円超、ふるさと納税、住宅ローンなど。</p>"})
add("money-furusato", "ふるさと納税のやり方｜在日ベトナム人も使える節税制度", "ふるさと納税の仕組み、申し込み方法、おすすめ返礼品、控除上限額の計算方法。", "ふるさと納税,節税,返礼品,ワンストップ特例,確定申告", "money", "generic", {"ふるさと納税とは": "<p>自治体に寄付すると住民税が控除され返礼品がもらえる制度。</p>"})
add("telecom-line-mobile", "LINEモバイルの契約方法と使い方｜ベトナム人ガイド", "LINEモバイルの料金プラン、申し込み方法、LINE通話無料のメリット、他社との比較。", "LINEモバイル,格安SIM,LINE通話,月額料金,データ通信", "telecom", "mobile", {"LINEモバイルの特徴": "<p>LINE通話がデータ消費ゼロ。ベトナムとの連絡に最適。</p>"})
add("telecom-net-bank", "ネット銀行の口座開設と使い方｜ベトナム人向け", "楽天銀行・SBI新生銀行などネット銀行の口座開設方法、メリット、海外送金機能。", "ネット銀行,楽天銀行,SBI新生銀行,口座開設,海外送金", "money", "sokin", {"ネット銀行のメリット": "<p>手数料が安い、24時間取引可能、ベトナム送金も簡単。</p>"})
add("telecom-wifi-free", "日本のWi-Fiスポットの探し方｜無料Wi-Fi完全ガイド", "日本で使える無料Wi-Fiスポットの探し方、接続方法、セキュリティ注意点を解説。", "WiFi,無料WiFi,WiFiスポット,インターネット,接続", "telecom", "mobile", {"無料Wi-Fiスポット": "<p>コンビニ、カフェ、駅、空港、公共施設で利用可能。</p>"})
add("estate-sharehouse", "シェアハウスの選び方｜ベトナム人におすすめの住まい", "初期費用を抑えたい人におすすめのシェアハウスの選び方、メリット・デメリット、運営会社。", "シェアハウス,シェアルーム,格安,初期費用,一人暮らし", "estate", "estate", {"シェアハウスのメリット": "<p>初期費用が安い（3〜5万円）、家具家電付き。</p>"})
add("estate-ur", "UR賃貸住宅の入居方法｜保証人不要で安心", "UR賃貸住宅の入居条件、申し込み方法、家賃相場、外国人入居の可否を解説。", "UR賃貸,都市再生機構,保証人不要,団地,賃貸,外国人入居", "estate", "estate", {"UR賃貸の特徴": "<p>保証人不必要、更新料なし、仲介手数料なし。</p>"})
add("life-gaikokujin-toroku", "外国人登録の基礎知識｜ベトナム人向けガイド", "日本での外国人登録手続きの基本を解説。市区町村での届出、在留カード管理、住所変更手続き。", "外国人登録,市区町村,届出,在留カード,住所変更", "life", "generic", {"外国人登録とは": "<p>日本に住む外国人は市区町村に住民登録する義務があります。</p>"})
add("life-kyouiku", "在日ベトナム人の子供の教育ガイド｜学校選びと進路", "ベトナム人の子供の教育について解説。日本の学校、インターナショナルスクール、母国語教育の選択肢。", "教育,子供,学校,進路,インターナショナルスクール,ベトナム語", "life", "generic", {"教育の選択肢": "<p>日本の公立学校、外国人学校、インターナショナルスクールなど。</p>"})
add("money-toushi", "在日ベトナム人のための投資入門｜NISA・iDeCo解説", "日本での投資の始め方を解説。NISA、iDeCo、株式投資、投資信託の基本。", "投資,NISA,iDeCo,株式,投資信託,資産運用", "money", "generic", {"投資の始め方": "<p>まずはNISA口座を開設。少額から積立投資を始めましょう。</p>"})
add("money-kaigai-sokin", "海外送金の税金と申告義務｜ベトナム送金時の注意点", "日本からベトナムへの海外送金における税金と申告義務について解説。贈与税、所得税の課税関係。", "海外送金,税金,贈与税,申告,ベトナム送金,税務署", "money", "sokin", {"海外送金の税金": "<p>年間110万円以上の送金は贈与税の申告が必要な場合があります。</p>"})
add("telecom-rakuten-mobile", "楽天モバイルの契約方法と使い方｜ベトナム人ガイド", "楽天モバイルの料金プラン、申し込み方法、データ無制限のメリット、注意点を解説。", "楽天モバイル,Rakuten,格安SIM,データ無制限,月額料金", "telecom", "mobile", {"楽天モバイルの特徴": "<p>月額3,278円でデータ無制限。Rakuten Linkで国内通話無料。</p>"})
add("life-shukatsu", "在日ベトナム人学生の就職活動（Shukatsu）ガイド", "日本の就職活動の流れをベトナム人学生向けに解説。インターンシップ、エントリーシート、面接対策。", "就職活動,Shukatsu,インターン,内定,新卒採用,エントリーシート", "life", "jobs", {"就職活動の流れ": "<p>3年生から準備開始。インターン参加→本選考→内定</p>"})
add("life-kyufukin", "日本でもらえる給付金・助成金一覧｜在日ベトナム人向け", "在日ベトナム人が受け取れる給付金・助成金を一覧で紹介。出産育児一時金、児童手当、医療費助成など。", "給付金,助成金,出産一時金,児童手当,医療費助成", "life", "generic", {"主な給付金": "<table><tr><th>名称</th><th>金額</th></tr><tr><td>出産育児一時金</td><td>50万円</td></tr><tr><td>児童手当</td><td>月1〜1.5万円</td></tr></table>"})
add("life-kyuujin-site", "Indeedとタウンワークの使い方｜ベトナム人求職者ガイド", "Indeedとタウンワークの効率的な使い方を比較。検索のコツ、応募方法、履歴書の送り方まで。", "Indeed,タウンワーク,求人,応募,検索,仕事探し", "life", "jobs", {"Indeedの使い方": "<p>キーワードと場所で検索。日本語と英語両方で検索可能。</p>"})

CTAS = {
    "gyosei": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4de; 行政書士に相談しませんか？</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">初回無料相談対応の行政書士がサポートします。</p><a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">行政書士を探す &#x2192;</a></div>',
    "sokin": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4b0; ベトナムへの送金なら</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">Wise・SBI Remitなど手数料最安のサービスを比較。</p><a href="/pages/cong-viec.html" class="btn btn-accent btn-lg">送金サービスを比較 &#x2192;</a></div>',
    "hoken": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f3e5; 保険の見直しをしませんか？</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">毎月の保険料を最適化できます。</p><a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">保険を比較 &#x2192;</a></div>',
    "mobile": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4f1; 格安SIMを比較する</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">月額500円から使える格安SIM。</p><a href="/pages/telecom.html" class="btn btn-accent btn-lg">SIMを比較 &#x2192;</a></div>',
    "estate": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f3e0; 不動産会社を探す</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">保証人不要の物件を紹介。</p><a href="/pages/estate.html" class="btn btn-accent btn-lg">物件を探す &#x2192;</a></div>',
    "generic": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4ac; お困りごとはありませんか？</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">専門家による無料相談をご利用ください。</p><a href="/pages/chuyen-gia.html" class="btn btn-accent btn-lg">無料相談 &#x2192;</a></div>',
    "jobs": '<div class="cta-section" style="background:linear-gradient(135deg,var(--color-primary) 0%,var(--color-primary-dark) 100%);padding:var(--space-xl);border-radius:var(--radius-lg);text-align:center;margin-top:var(--space-2xl);"><h3 style="color:white;margin-bottom:var(--space-md);">&#x1f4bc; 求人を探す</h3><p style="color:rgba(255,255,255,0.9);margin-bottom:var(--space-lg);">ベトナム人向け求人情報。</p><a href="/pages/jobs.html" class="btn btn-accent btn-lg">求人を探す &#x2192;</a></div>',
}

CATS = {
    "life": {"name": "生活・行政手続き", "url": "/pages/sinh-hoat.html", "dir": "sinh-hoat"},
    "money": {"name": "仕事・金融", "url": "/pages/cong-viec.html", "dir": "cong-viec"},
    "telecom": {"name": "通信・SIM", "url": "/pages/telecom.html", "dir": "telecom"},
    "estate": {"name": "不動産・住まい", "url": "/pages/estate.html", "dir": "estate"},
}

NAV_LINKS = [("/pages/jobs.html", "転職・求人"), ("/pages/vinh-tru.html", "永住・帰化"), ("/pages/visa.html", "ビザ・更新"), ("/pages/sinh-hoat.html", "生活・行政"), ("/pages/cong-viec.html", "仕事・金融"), ("/pages/telecom.html", "通信・SIM"), ("/pages/estate.html", "不動産・住まい"), ("/pages/chuyen-gia.html", "専門家相談")]
NAV_MAP = {"life": 3, "money": 4, "telecom": 5, "estate": 6}

def gen(slug, data):
    today = datetime.now().strftime("%Y-%m-%d")
    t = data["title"]
    hl = t.split("｜")[0]
    cat = CATS[data["cat"]]
    cta = CTAS[data["cta"]]
    sec = data["sections"]
    ai = NAV_MAP.get(data["cat"], 0)
    nav = ""
    for i, (u, l) in enumerate(NAV_LINKS):
        ac = " header__nav-link--active" if i == ai else ""
        nav += f'          <li><a href="{u}" class="header__nav-link{ac}">{l}</a></li>\n'
    toc = ""
    sh = ""
    for i, (h, c) in enumerate(sec.items(), 1):
        hid = f"s{i}"
        toc += f'          <li><a href="#{hid}">{h}</a></li>\n'
        sh += f'      <h2 id="{hid}">{h}</h2>\n{c}\n'
    ou = f"https://vietnam-japan-guide.com/articles/{cat['dir']}/{slug}.html"
    cat_name = cat["name"]
    cat_url = cat["url"]
    breadcrumb_json = '{"@type":"ListItem","position":3,"name":"' + hl + '","item":"' + ou + '"}'
    
    # Pre-compute desc_first
    desc_first = data["desc"].split("。")[0] + "。"
    
    # Build FAQ schema
    faq = ""
    if "よくある質問（FAQ）" in sec:
        qas = __import__("re").findall(r"<h3>Q\d+\.\s*([^<]+)</h3>\s*<p>A\.\s*([^<]+)</p>", sec["よくある質問（FAQ）"])
        if qas:
            items = [f'{{"@type":"Question","name":"{q.strip()}","acceptedAnswer":{{"@type":"Answer","text":"{a.strip()}"}}}}' for q, a in qas]
            faq = '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n' + ",\n".join(items) + "\n]}\n</script>"

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
  <meta property="og:url" content="{ou}">
  <link rel="canonical" href="{ou}">
  <link rel="stylesheet" href="../../css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{hl}","description":"{desc_first}","datePublished":"{today}","dateModified":"{today}","author":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"publisher":{{"@type":"Organization","name":"Vietnam Japan Guide"}},"inLanguage":"ja"}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {{"@type":"ListItem","position":1,"name":"トップページ","item":"https://vietnam-japan-guide.com/"}},
    {{"@type":"ListItem","position":2,"name":"{cat_name}","item":"https://vietnam-japan-guide.com{cat_url}"}},
    {breadcrumb_json}
  ]}}</script>
  {faq}
</head>
<body>
  <header class="header" role="banner">
    <div class="header__inner">
      <a href="/" class="header__logo"><span class="header__logo-icon" aria-hidden="true">VN</span>Vietnam Japan Guide</a>
      <nav class="header__nav">
        <ul class="header__nav-list">
{nav}        </ul>
      </nav>
      <button class="header__menu-toggle" aria-label="メニュー"><span></span><span></span><span></span></button>
    </div>
  </header>
  <nav class="breadcrumb"><div class="container"><ol class="breadcrumb__list">
    <li class="breadcrumb__item"><a href="/">トップページ</a></li>
    <li class="breadcrumb__item"><a href="{cat['url']}">{cat['name']}</a></li>
    <li class="breadcrumb__item breadcrumb__item--current">{hl}</li>
  </ol></div></nav>
  <article class="article-content"><div class="container">
    <h1>{hl}</h1>
    <div class="info-box info-box--warning"><div class="info-box__title">&#x26a0;&#xfe0f; おことわり</div><p>この記事は公的機関の公式情報をもとに解説しています。法律専門家ではないため、正確な判断は専門家にご確認ください。</p></div>
    <div class="info-box"><div class="info-box__title"><span class="icon">&#x1f4dd;</span> この記事のポイント</div><p>{data['desc']}</p></div>
    <div class="toc"><div class="toc__title">&#x1f4d1; 目次</div><ul class="toc__list">
{toc}        </ul></div>
{sh}    {cta}
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

cnt = 0
for slug, data in NEW:
    d = os.path.join(BASE, "articles", CATS[data["cat"]]["dir"])
    os.makedirs(d, exist_ok=True)
    h = gen(slug, data)
    h = h.replace("{{", "{").replace("}}", "}")
    with open(os.path.join(d, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(h)
    cnt += 1
    print(f"[{cnt}/30] {slug}")

print(f"Done! {cnt} articles")