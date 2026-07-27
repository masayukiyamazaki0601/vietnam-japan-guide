# Deploy Migration Record

## 移行サマリー

| 項目 | 変更前 | 変更後 |
|------|--------|--------|
| **ホスティング** | Netlify | GitHub Pages |
| **料金** | $0（クレジット超過で停止） | $0（完全無料・無制限） |
| **デプロイ方法** | GitHub Actions + Netlify CLI | GitHub Actions + peaceiris/actions-gh-pages |
| **リポジトリ** | PRIVATE | PUBLIC |
| **ブランチ** | main | main → gh-pages（自動デプロイ） |
| **URL** | https://japan-residence.com | https://masayukiyamazaki0601.github.io/vietnam-japan-guide/ |
| **移行日** | 2026-07-26 以前 | 2026-07-27 |

## 移行理由

Netlifyの無料枠クレジットが上限に達し、新規デプロイがブロックされた。
```
Error: "Account credit usage exceeded - new deploys are blocked until credits are added"
```
Netlify Pro（$19/月）はエックスサーバー（年1万円程度）より割高なため、完全無料のGitHub Pagesに移行。

## 移行手順

1. `.github/workflows/deploy.yml` を Netlify 用から GitHub Pages 用に書き換え
2. `gh repo edit --visibility public` でリポジトリをPUBLICに変更
3. `gh api .../pages` でGitHub Pagesのソースブランチを `gh-pages` に設定
4. プッシュ後、自動的にGitHub Pagesにデプロイ

## 現在のデプロイフロー

```
git push origin main
  → GitHub Actions（.github/workflows/deploy.yml）
    → peaceiris/actions-gh-pages@v4
      → gh-pages ブランチにデプロイ
        → https://masayukiyamazaki0601.github.io/vietnam-japan-guide/
```

## 翻訳済み記事一覧（2026-07-27）

| 記事 | 日本語版 | ベトナム語版 | GitHub Pages URL |
|------|---------|------------|-----------------|
| 子供を育てる在留資格 | `ja/articles/visa/kodomo-sodateru-zairyu.html` | `vi/articles/visa/kodomo-sodateru-zairyu.html` | `/vi/articles/visa/kodomo-sodateru-zairyu.html` |
| 婚約・短期間での結婚と配偶者ビザ | `ja/articles/visa/konyaku-tanki-kekkon.html` | `vi/articles/visa/konyaku-tanki-kekkon.html` | `/vi/articles/visa/konyaku-tanki-kekkon.html` |
| 日本語能力（N1・N2）がビザ・永住権に与える影響 | `ja/articles/visa/nihongo-n1n2-eikyo.html` | `vi/articles/visa/nihongo-n1n2-eikyo.html` | `/vi/articles/visa/nihongo-n1n2-eikyo.html` |
| 国際運転免許の利用 | `ja/articles/sinh-hoat/life-idp-riyou.html` | `vi/articles/sinh-hoat/life-idp-riyou.html` | `/vi/articles/sinh-hoat/life-idp-riyou.html` |

## GitHub Secrets

| Secret名 | 値 | 用途 |
|----------|----|------|
| `NETLIFY_AUTH_TOKEN` | nfp_Xf8bqFFqq4BBfi3Sz4eSXEJbPwB8YTJF2840 | （現在不使用）Netlify用 |
| `NETLIFY_SITE_ID` | 5dc61c6a-808b-4606-b436-126ca74de0d1 | （現在不使用）Netlify用 |
| `GITHUB_TOKEN` | 自動生成 | GitHub Pagesデプロイ用 |

## ローカル確認方法

```bash
cd _archive/projects/vietnam-japan-guide
python3 -m http.server 8001
# → http://localhost:8001/vi/
```
