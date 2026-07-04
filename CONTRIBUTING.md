# 開発参加ガイド

このプロジェクトはチーム開発フロー学習を目的としています。

## 開発の進め方

### ステップ 1: ブランチ作成

```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

### ステップ 2: 実装・テスト

- コード実装
- ローカルテスト実行（pytest）
- Lint 確認（ruff check .）

### ステップ 3: コミット・プッシュ

```bash
git add .
git commit -m "feat: describe your change"
git push origin feature/your-feature-name
```

### ステップ 4: PR 作成・マージ

1. GitHub で PR を作成
2. PR テンプレートに従って説明を記入
3. CI が通ることを確認
4. `Merge pull request` でマージ
5. マージ後ブランチを削除

## コードスタイル

- Python: PEP 8 準拠
- Lint ツール: ruff
- テストフレームワーク: pytest

## テスト要件

すべての機能追加にはテストが必須です。

```bash
pytest
```

## コミットメッセージの規約

- `feat: 新機能名` - 新機能追加
- `fix: バグ概要` - バグ修正
- `chore: 内容` - 設定・メンテナンス
- `ci: 内容` - CI/CD 関連

## PR レビューポイント

- [ ] CI テストが全て通っている
- [ ] テストコードが追加されている
- [ ] ドキュメントが更新されている
- [ ] コミットメッセージが規約に従っている
