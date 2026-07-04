# niche-news-notifie
0. プロジェクト概要

何を作るか

特定のRSSフィード（技術ブログ等）を定期的にチェックし、新着記事があればメールで通知するツール。

なぜこの構成か


サーバー不要・完全無料：GitHub Actions の schedule（cron）機能で定期実行
デプロイの複雑さを排除：Vercel/Renderなどの外部サービス管理が不要
Git/CICD 体験に集中できる：アプリの複雑さよりも「開発フロー」に重点


技術スタック

要素技術言語Python情報収集feedparser（RSS解析）通知smtplib（メール送信）実行環境GitHub Actions（cron）データ保存リポジトリ内 JSON（既読管理）テストpytestLintruff または flake8

全体の進め方

Phase 0: 環境準備
Phase 1: リポジトリ初期設定 & ブランチルール
Phase 2: 最小機能実装（Git フロー実践その1）
Phase 3: CI導入（テスト・Lint自動化）
Phase 4: CD導入（定期実行 + メール通知）
Phase 5: 機能追加サイクル（Git フロー実践その2以降）
Phase 6: AI統合（将来フェーズ）

重要な心構え：最初から完璧な機能を目指さない。各Phaseで「小さく作って、PRを出して、マージする」というサイクルを繰り返し体験することが目的。

1-3. ブランチ運用ルールを決める（今回のシンプル版）

今回はチーム規模が小さい想定なので、シンプルな運用にします：

main          … 常に動く状態を保つ（本番相当）
feature/xxx   … 機能追加・修正用の作業ブランチ

develop ブランチは、今回はまず入れずに main + feature/* のみで体験する（慣れてきたら develop を追加するのも良い学習になる）。