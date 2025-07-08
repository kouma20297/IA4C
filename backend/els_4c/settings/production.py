from .base import *
import os

DEBUG = False

# 静的ファイル設定（Render用）
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT", "5432"),
    }
}
