
# IA4C - Interactive AI for Community

## 📝 プロジェクト概要
<!-- 
このプロジェクトの目的や背景を簡潔に書いてください。
例：「AIを活用してQ&A投稿を要約・教材化できるコミュニティプラットフォームです」 
-->
ここにプロジェクトの概要を書く

---

## 📦 主な機能
<!-- 
提供する機能のリストを箇条書きで。
将来的に追加予定の機能も書いてOK。
-->
- スレッド投稿・回答機能（Q&A形式）
- AIによる自動要約・教材化
- タグやカテゴリによる検索（予定）

---

## ⚙️ 使用技術（Tech Stack）
<!-- 
使用している言語、フレームワーク、ツールなど。
-->
- Python / Django REST Framework
- MSSQL（すでにあるものに統合する）
- Docker / docker-compose
- GitHub Actions（CI/CD）

---

## 🚀 セットアップ手順（ローカル開発用）
```bash
# 1. .envファイル作成
cp .env.template .env.dev

# 2. Docker起動
docker-compose up --build
