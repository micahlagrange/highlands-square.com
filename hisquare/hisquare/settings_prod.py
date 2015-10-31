__author__ = 'UTURNMI'

DEBUG = TEMPLATE_DEBUG = False


with open('/etc/highlands-square.com.conf/db_password') as f:
    PASSWORD = f.read().strip()

# db, media, static dirs
DATABASES = {
    'default': {
      'NAME': 'django_db',
      'ENGINE': 'mysql.connector.django',
      'USER': 'root',
      'PASSWORD': PASSWORD,
      'OPTIONS': {
        'autocommit': True,
      },
    }
}

MEDIA_ROOT = '/www/hisquare/media'
STATIC_ROOT = '/www/hisquare/static'
STATIC_DIR = 'www/hisquare/static'

# Static, media urls
STATIC_URL = '//hsmadev.highlands-square.com/static/'
MEDIA_URL = '//hsmadev.highlands-square.com/media/'


SERVER_EMAIL = 'hsmasite@gmail.com'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d-%b-%Y %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/www/hisquare/logging/hisquare.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
        'basic_logger': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
        },
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mod_wsgi.server',
    'home'
)
