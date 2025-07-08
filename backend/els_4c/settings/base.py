import os
from pathlib import Path

# プロジェクトのベースディレクトリを定義
BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティキーとデバッグ設定（Renderでは環境変数で管理）
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = os.environ.get("DEBUG", "True") == "True"

# ホスト許可（スペース区切りで複数指定可能）
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split()

# アプリケーション定義
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # プロジェクトアプリ
    'els_4c',
    'users',
    'threads',
    'answers',

    # サードパーティ
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORSのために先頭に追加
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'els_4c.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'els_4c.wsgi.application'

# 認証ユーザーモデル
AUTH_USER_MODEL = 'users.User'

# 静的ファイル設定（開発/本番兼用）
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # 本番用collectstatic出力先

# デフォルトの主キーの型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework設定
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Auth0（使うなら）
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
AUTH0_API_IDENTIFIER = os.environ.get("AUTH0_API_IDENTIFIER")

# CORS設定（任意、必要に応じて）
CORS_ALLOW_ALL_ORIGINS = True

# 国際化設定
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True
USE_L10N = True  # ロケール形式（日本の数値や日付）を使う
USE_TZ = True

# ログ設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': { 'class': 'logging.StreamHandler' },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
