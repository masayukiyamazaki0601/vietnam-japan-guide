# プロジェクト引継ぎ書 - Vietnam Japan Guide（2026/7/16 更新 - cong-viec全24件完了）

## プロジェクト概要
在日ベトナム人向けの生活総合情報サイト。ビザ、永住権、日常生活の手続きについて日本語で解説。静的HTMLサイト（フレームワーク不使用）。

## サイト全体の記事数：169記事

| カテゴリ | 記事数 | 状態 |
|---------|-------|------|
| vinh-tru（永住権） | 32 | ✅ 全件更新済み |
| visa（ビザ） | 56 | ✅ 全件更新済み |
| sinh-hoat（生活） | 38 | ✅ 37件更新済み（life-skeleton-10.html のみ未更新） |
| **cong-viec（仕事・金融）** | **24** | **✅ 全24件完了** |
| jobs（仕事・日本語） | 6 | ❌ 未着手 |
| telecom（通信） | 6 | ❌ 未着手 |
| estate（不動産） | 6 | ❌ 未着手 |
| chuyen-gia（専門家） | 1 | ❌ 未着手 |

## 今回完了した作業（2026/7/16 セッション：cong-viec 13記事一挙完了）

### 新規作り直し（ユーザー提供の記事本文を統一フォーマットに組み込み）
1. ✅ **money-furusato.html** — ふるさと納税のやり方
2. ✅ **money-kaigai-sokin.html** — 海外送金の税金と申告義務
3. ✅ **money-toushi.html** — 在日ベトナム人のための投資入門（NISA・iDeCo）
4. ✅ **money-zeikimushi.html** — 税金の還付（還付申告）のやり方

### 「=== 執筆中 ===」から完全記事に書き換え
5. ✅ **nenkin-dattai-ikiru-eikyo.html** — 年金脱退一時金申請後の将来の年金への影響
6. ✅ **roudou-keiyakusho-point.html** — 日本の労働契約書で確認すべき重要ポイント
7. ✅ **shihonkin-junbi-note.html** — 会社設立時の資本金準備の注意点
8. ✅ **souzoku-zozei-kiso.html** — 日本での相続税・贈与税の基礎知識
9. ✅ **taishoku-go-juminzei.html** — 会社を辞めた後の住民税の支払い方法
10. ✅ **tokutei-ginou-kyuujin.html** — 特定技能の求人探しとおすすめ転職サイト
11. ✅ **vietnam-engineer-it.html** — ベトナム人エンジニアのための日本のIT業界解説
12. ✅ **money-nenkin.html** — 年金制度の基礎知識

### 既存記事を統一フォーマットで書き換え
13. ✅ **telecom-net-bank.html** — ネット銀行の口座開設と使い方

### 修正・統一した点
- CSSパス: `../..../../css/style.css` → `../../css/style.css`（nenkin-dattai-ikiru-eikyo, roudou-keiyakusho-point, shihonkin-junbi-note, souzoku-zozei-kiso, taishoku-go-juminzei, tokutei-ginou-kyuujin, vietnam-engineer-it）
- JSパス: `../..../../js/main.js` → `../../js/main.js`
- ヘッダーナビ: 8項目→5項目に統一（telecom-net-bank, money-furusato, money-kaigai-sokin, money-toushi, money-zeikimushi, money-nenkin）
- フッターリンク: 8項目→5項目に統一
- 語尾: 「でございます」「いたします」「おります」不使用
- おことわり文面統一
- パンくずリストの完全化

## 未完了タスク / 注意点
1. **🔲 sinh-hoat 未更新1件** — life-skeleton-10.html
2. **🔲 残りカテゴリ（jobs/telecom/estate/chuyen-gia）** — 全19件未着手
3. **🔲 sitemap.xml の更新** — 新規記事追加時
4. **🔲 `articles/singh-hoat/`**（タイポの空ディレクトリ）— 削除候補

## 技術情報
- 静的HTMLサイト（フレームワーク不使用）
- CSS: `/css/style.css`（ディープネイビー×カッパーゴールド配色）
- JS: `/js/main.js`
- サーバー: `python3 -m http.server 8087`（プロジェクトルートから起動）
- Git管理: `origin: https://github.com/masayukiyamazaki0601/mit-6.100l-curriculum.git`

## 作業の進め方（ルール）
- **テーマは1つずつ作成し、「次へ」の指示があるまで次のテーマは作成しない**
- 各記事は上記「統一フォーマット」に従う
- 事実関係の正確性を最優先（特に税金・ビザ・社会保険）
- 断定表現を避け「原則」「場合があります」「傾向があります」を使用
- 古い制度と現在の制度を混同しない
- 語尾は「です」「ます」で統一（「いたします」「おります」「ございます」不使用）

## ファイル構成
```
vietnam-japan-guide/
├── index.html
├── css/style.css
├── js/main.js
├── pages/（カテゴリ一覧ページ）
├── articles/
│   ├── vinh-tru/（32記事 - ✅ 完了）
│   ├── visa/（56記事 - ✅ 完了）
│   ├── sinh-hoat/（38記事 - ✅ 37/38完了）
│   ├── cong-viec/（24記事 - ✅ 全24件完了）
│   ├── jobs/（6記事 - ❌）
│   ├── telecom/（6記事 - ❌）
│   ├── estate/（6記事 - ❌）
│   ├── chuyen-gia/（1記事 - ❌）
│   └── singh-hoat/（空 - 削除候補）
└── sitemap.xml