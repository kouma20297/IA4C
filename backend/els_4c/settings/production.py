from .base import *

DEBUG = False
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Renderでは必要に応じて変更
        'NAME': os.getenv("MYSQL_DATABASE"),
        'USER': os.getenv("MYSQL_USER"),
        'PASSWORD': os.getenv("MYSQL_PASSWORD"),
        'HOST': os.getenv("MYSQL_HOST", "db"),
        'PORT': '3306',
    }
}
