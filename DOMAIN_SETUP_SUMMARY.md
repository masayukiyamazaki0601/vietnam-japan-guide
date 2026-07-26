# japan-residence.com セットアップ状況

## 完了したこと ✅
1. Netlifyサイト「japan-residence」作成・デプロイ完了
   - https://japan-residence.netlify.app/ja/ （日本語）
   - https://japan-residence.netlify.app/vi/ （ベトナム語）
2. カスタムドメイン `japan-residence.com` をNetlifyに追加
3. Netlify DNSを有効化（ネームサーバー発行済み）

## 未完了 ❌
お名前.comでネームサーバーをNetlifyのものに変更する必要がある。

## お名前.com ログイン情報
- URL: https://www.onamae.com
- ID: `51159016`
- パスワード: `sxm23545`

## 設定方法（2択）

### 方法A: ネームサーバー変更（推奨）
1. https://www.onamae.com/domain/nameserver/ にアクセス
2. `japan-residence.com` にチェック
3. 「その他のサービス」を選択
4. 以下4つを入力：
   - `dns1.p04.nsone.net`
   - `dns2.p04.nsone.net`
   - `dns3.p04.nsone.net`
   - `dns4.p04.nsone.net`
5. 「確認」→「保存」

### 方法B: Aレコード修正（より簡単）
1. https://www.onamae.com/domain/dns/ にアクセス
2. `japan-residence.com` のAレコードを編集
3. 値 `157.120.209.48` → `75.2.60.5` に変更
4. 保存

## 反映について
- DNS変更後、数分〜24時間で `https://japan-residence.com` にアクセス可能になる
- Netlify側の設定は全て完了済みのため、お名前.comの設定だけで動作する