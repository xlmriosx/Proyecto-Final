from .settings import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}