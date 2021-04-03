from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'POER': '3306',
        'NAME': 'typeidea_db',
        'USER': 'xxx',
        'PASSWORD': 'xxx',
    }
}
