from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv("MYSQL_DATABASE", "ia4c_dev"),
#         'USER': os.getenv("MYSQL_USER", "ia4c_user"),
#         'PASSWORD': os.getenv("MYSQL_PASSWORD", "securepass"),
#         'HOST': 'db',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("MYSQL_DATABASE", "ia4c_dev"),
        'USER': os.getenv("MYSQL_USER", "ia4c_user"),
        'PASSWORD': os.getenv("MYSQL_PASSWORD", "securepass"),
        'HOST': os.getenv("MYSQL_HOST"),
        'PORT': '3306',
    }
}

