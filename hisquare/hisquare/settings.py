"""
Django settings for hisquare project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEV_HOSTS = ('Micahs-MacBook-Pro.local')
PROD_HOST = 'hsma01p'

if socket.gethostname() in DEV_HOSTS:
    from hisquare.settings_dev import *
elif socket.gethostname() == PROD_HOST:
    from hisquare.settings_prod import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/highlands-square.com.conf/secretkey') as f:
	    SECRET_KEY = f.read().strip()
	    
ALLOWED_HOSTS = ['highlands-square.com', '104.236.153.248']

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hisquare.urls'

WSGI_APPLICATION = 'hisquare.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATABASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
    os.path.join(STATIC_DIR),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

