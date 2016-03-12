import os
from hisquare.settings import BASE_DIR


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Database
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

MEDIA_ROOT = os.path.join(BASE_DIR, "home", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "home", "static")

# Static, media urls
STATIC_URL = '//dev.highlands-square.com/static/'
MEDIA_URL = '//dev.highlands-square.com/media/'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home'
)

STATIC_DIR = os.path.join(BASE_DIR, "home", "static")

# FIXTURE_DIRS = (
#     os.path.join(BASE_DIR, 'hisquare', 'fixtures')
# )
