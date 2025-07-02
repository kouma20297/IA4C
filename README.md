# IA4C 拡張機能APIシステム

本システムは、スレッド投稿・回答・AI要約・教材化といった機能を提供する。 
認証やセキュリティは一切考慮しておらず、短期間で機能開発・動作確認することを目的としています。

---

## ✅ 概要

| 項目 | 内容 |
|------|------|
| プロジェクト名 | IA4C 拡張機能API |
| 使用技術 | Python / Django REST Framework |
| DB（開発用） | MySQL（Docker） |
| DB（本番用） | PostgreSQL（Render） |
| 認証DB（外部） | MSSQL（使えれば利用、接続不可でもOK） |
| 認証処理 | 一切なし（ログインやトークン認証なし） |
| 投稿者識別 | 仮のユーザーID（例："guest_user"）を自動付与 |

---

## 📦 提供API一覧

| カテゴリ | メソッド | エンドポイント | 説明 |
|----------|----------|----------------|------|
| スレッド投稿 | `POST` | `/api/threads/` | スレッドと質問を同時に作成 |
| スレッド一覧 | `GET` | `/api/threads/` | スレッドの一覧取得 |
| スレッド詳細 | `GET` | `/api/threads/:id/` | スレッド＋回答の詳細取得 |
| 回答投稿 | `POST` | `/api/threads/:id/answers/` | スレッドに対して回答を追加 |
| AI要約作成 | `POST` | `/api/threads/:id/summary/` | 質問と回答のAI要約を生成 |
| 教材化 | `POST` | `/api/materials/` | 要約から教材を作成 |
| 教材一覧取得 | `GET` | `/api/materials/` | 教材一覧を取得 |

---

## ⚙️ 開発環境構築手順（Docker）

```bash
# 1. リポジトリをクローン
git clone https://github.com/your-org/ia4c-backend.git
cd ia4c-backend


# 3. コンテナ起動
docker-compose up --build

# 4. マイグレーションと管理ユーザー作成（初回のみ）
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
