# niche-news-notifier

## 📌 プロジェクト概要

`niche-news-notifier` は、RSS フィードの新着記事を定期的に確認し、更新があればメール通知する Python ツールです。

このプロジェクトの主目的は、単に通知ツールを作ることではなく、チーム開発フローを体験学習することにあります。Git によるブランチ運用、Pull Request を前提とした開発、CI による自動テスト、GitHub Actions による定期実行までを小さなアプリで一通り経験できるように設計しています。

実行基盤は GitHub Actions のみで、専用サーバーを用意せずに運用できる完全無料・サーバーレス構成です。

## 🎯 なぜこのプロジェクトか

- チーム開発での実践的なワークフローを小さく体験できる
- `main` と `feature/*` を使った Git ブランチ戦略を練習できる
- CI/CD パイプラインを自分で組み立てて理解できる
- GitHub Actions による定期実行と通知の仕組みを学べる
- 学習対象を絞ることで、インフラ構築より開発プロセスに集中できる

## 🛠 技術スタック

- Python 3.11+
- feedparser（RSS 解析）
- pytest（テスト）
- ruff（Lint）
- GitHub Actions（CI/CD、定期実行）
- Gmail SMTP（メール通知）

## 📋 セットアップ手順

### 前提条件

- Python 3.11 以上
- Git
- GitHub アカウント
- Gmail アカウント
- Gmail の 2 段階認証とアプリパスワードの発行

### リポジトリクローン

```bash
git clone <your-repository-url>
cd niche-news-notifier
```

### 仮想環境構築（venv）

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source venv/bin/activate
```

### 依存関係インストール

```bash
pip install -r requirements.txt
```

### GitHub Secrets 設定

GitHub リポジトリの `Settings` → `Secrets and variables` → `Actions` で次の Secrets を設定します。

- `EMAIL_ADDRESS`
- `EMAIL_APP_PASSWORD`
- `EMAIL_TO`

### ブランチ保護ルール設定

`main` ブランチに対して、少なくとも次を有効にする想定です。

- Pull Request 経由でのみ変更可能
- CI 成功をマージ条件にする
- 必要に応じて自己レビュー用のチェックを運用に組み込む

## 📦 プロジェクト構成

```text
niche-news-notifier/
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       ├── ci.yml               (Lint・テスト自動実行)
│       └── notify.yml           (定期実行・メール通知)
├── venv/                        (.gitignore に含める)
├── fetcher.py                   (RSS フィード取得)
├── notifier.py                  (メール送信)
├── main.py                      (実行エントリーポイント)
├── test_fetcher.py              (現行テスト)
├── requirements.txt             (依存関係)
├── .gitignore
├── README.md
├── CONTRIBUTING.md              (開発参加ガイド)
└── seen_articles.json           (初回通知後に生成、既読管理)
```

## 🔄 実装の進み方（Phase 別）

### Phase 0: 環境準備

- ローカル Python 環境確認
- GitHub リポジトリ作成
- メール送信用 Secrets 準備

### Phase 1: リポジトリ初期設定

- `.gitignore`、`requirements.txt`、`README.md` 作成
- ブランチ保護ルール設定
- PR テンプレート作成

### Phase 2: 最小機能実装

- `fetcher.py`: RSS フィード取得機能
- Git フロー実践（feature ブランチ → PR → マージ）

### Phase 3: CI 導入

- `.github/workflows/ci.yml` 作成
- Lint（ruff）・テスト（pytest）の自動実行
- PR マージ時に CI 通過を必須化

### Phase 4: CD 導入

- `notifier.py`: メール送信機能
- `main.py`: 既読管理 + メール通知ロジック
- `.github/workflows/notify.yml`: 定期実行設定
- GitHub Secrets に認証情報を登録

### Phase 5: 機能追加サイクル（継続的）

- 複数フィード対応
- エラー時の通知
- テスト拡充
- `docs/` フォルダで詳細ドキュメント化

### Phase 6: AI 統合（将来）

- Claude API による記事要約
- GitHub Copilot によるコード支援
- AI による自動コードレビュー

## 🚀 使い方

### 手動実行

```bash
source venv/bin/activate  # Windows: venv\Scripts\Activate.ps1
python main.py
```

### 定期実行（自動）

GitHub Actions により、毎日 UTC 23:00（JST 8:00）に自動実行されます。新着記事がある場合のみメール通知し、既読情報は `seen_articles.json` に保存されます。

### 手動トリガー（GitHub Web UI）

Actions タブから `Notify New Articles` を選び、`Run workflow` を実行します。

## 📚 詳細ドキュメント

以下は Phase 5 で `docs/` 配下に追加予定です。

- `docs/SETUP.md` - 詳細なセットアップ手順
- `docs/GIT_WORKFLOW.md` - ブランチ戦略・PR フロー
- `docs/PHASES.md` - 各 Phase の詳細説明
- `docs/TROUBLESHOOTING.md` - よくあるエラー対処
- `CONTRIBUTING.md` - チーム開発時のルール

## 🔐 環境変数（GitHub Secrets）

| 変数名 | 説明 | 例 |
| --- | --- | --- |
| `EMAIL_ADDRESS` | 送信元メールアドレス | `your-email@gmail.com` |
| `EMAIL_APP_PASSWORD` | Gmail アプリパスワード | `abcd efgh ijkl mnop` |
| `EMAIL_TO` | 通知受信メールアドレス | `your-email@gmail.com` |

Gmail で 2 段階認証を有効化したうえで、アプリパスワードを発行してください。

## 🔄 CI/CD パイプライン

### CI（Continuous Integration）

- トリガー: `main` 向け Pull Request 作成時
- 実行内容: `ruff check .` と `pytest`
- ブランチ保護: CI 成功を `main` へのマージ条件に設定する想定

### CD（Continuous Delivery）

- トリガー: スケジュール実行（毎日 UTC 23:00）または手動実行
- 実行内容: RSS フィード取得、新着記事判定、メール通知、既読情報更新
- 既読情報: `seen_articles.json` の更新がある場合は GitHub Actions からコミット

## 📖 Git ワークフロー

### ブランチ戦略

```text
main              … 本番相当・常に動く状態
└── feature/xxx   … 機能開発用
```

### PR フロー

1. `git checkout -b feature/xxx` で機能ブランチ作成
2. 実装とテストを行う
3. `git push origin feature/xxx` でリモートへ反映
4. GitHub で Pull Request を作成
5. CI テスト実行・確認
6. 自分でレビューするか、チームレビューを受ける
7. `Merge pull request` でマージ
8. 不要になったブランチを削除

### コミットメッセージ規約

- `feat:` 新機能
- `fix:` バグ修正
- `chore:` 設定・メンテナンス
- `ci:` CI/CD 関連

## 🧪 テスト

### テスト実行

```bash
pytest
```

### テスト範囲

- `fetcher.py` の RSS フィード取得
- `notifier.py` のメール送信ロジック（Phase 5 でスタブ化テスト追加予定）
- メイン処理のエラーハンドリング（Phase 5 で拡充予定）

## 🚧 既知の制限・今後の改善

### Phase 5 で検討予定

- [ ] 複数 RSS フィード対応
- [ ] フィード設定の外部化（`config/feeds.json`）
- [ ] エラーハンドリングの強化
- [ ] テストカバレッジの向上
- [ ] ロギング機能追加
- [ ] 本文抜粋機能
- [ ] `tests/` フォルダへのテスト整理
- [ ] `docs/` フォルダの追加と文書整備

### Phase 6（AI 統合）で検討予定

- [ ] Claude API による記事要約
- [ ] GitHub Copilot によるコード支援
- [ ] PR の自動コードレビュー
- [ ] Issue の自動トリアージ

## 📝 ライセンス

MIT

## 📧 お問い合わせ

質問や改善提案は GitHub Issues で報告してください。
