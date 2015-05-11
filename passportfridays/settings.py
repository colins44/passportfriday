"""
django settings for pf2 project.

for more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

for the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# build paths inside the project like this: os.path.join(base_dir, ...)
import os
<<<<<<< HEAD
from unipath import Path
BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
print BASE_DIR
# from kombu import exchange, queue
=======
base_dir = os.path.dirname(os.path.dirname(__file__))
#from kombu import exchange, queue
>>>>>>> a77c6c3a20a93d5fee5c78323bebf6e364c951bc


# quick-start development settings - unsuitable for production
# see https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# security warning: keep the secret key used in production secret!
SECRET_KEY = 'cmhz2hig9o-^va1y=8oeg-_xf54(40=6x+3%qnf0ttd+mgeoxh'

# security warning: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'email_user',
    'flights',
    'weekend',
    'django_extensions',
    'location',
    'accommodation',
    'genericadmin',
    'djcelery',
    'kombu.transport.django',
    'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS= (
        'email_user.backends.EmailUserAuth',
)

ROOT_URLCONF = 'passportfridays.urls'

WSGI_APPLICATION = 'passportfridays.wsgi.application'

# auth_user_model = 'email_user.emailuser'

# import djcelery
# djcelery.setup_loader()
# broker_url = 'django://'

AUTH_USER_MODEL = 'email_user.EmailUser'

#vagrant db setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'passportfridays',
        'USER': 'dirtypunit',
        'PASSWORD': 'downsouth69',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#covers regular testing and django-coverage
import sys
if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default']['engine'] = 'sqlite3'

# internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
ROOT_URLCONF = 'passportfridays.urls'
# email_backend = 'django.core.mail.backends.smtp.emailbackend'
email_backend = 'django.core.mail.backends.console.emailbackend'
email_use_tls = True
email_host = 'smtp.gmail.com'
email_port = 587
email_host_user = 'colin.pringle-wood@ostmodern.co.uk'
email_host_password = 'thisisthepassword'
default_from_email = 'colin.pringle-wood@ostmodern.co.uk'
default_to_email = 'colin.pringle-wood@ostmodern.co.uk'

default_from_email = 'the passport fridays team <noreply@passportfridays.com>'
default_from_name = 'the passport fridays team'

login_redirect_url = '/account/'
logout_redirect_url = '/'

# redis

redis_port = 6379
redis_db = 0
redis_host = os.environ.get('redis_port_6379_tcp_addr', '127.0.0.1')

rabbit_hostname = os.environ.get('rabbit_port_5672_tcp', 'localhost:5672')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# static files (css, javascript, images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = Path(BASE_DIR, 'static')

# absolute filesystem path to the directory that will hold user-uploaded files.
# example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# url that handles the media served from media_root. make sure to use a
# trailing slash.
# examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/static/media/'

STATICFILE_DIRS = (
<<<<<<< HEAD
    Path(BASE_DIR, "project_static"),
=======
    os.path.join(base_dir, "passportfridays/static"),
>>>>>>> a77c6c3a20a93d5fee5c78323bebf6e364c951bc
    # put strings here, like "/home/html/static" or "c:/www/django/static".
    # always use forward slashes, even on windows.
    # don't forget to use absolute paths, not relative paths.
)
print STATICFILE_DIRS

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

TEMPLATE_DIRS = (
    Path(BASE_DIR.parent, "templates"),
)

flightstats_appid = '92c5179a'
flightstats_appkey = 'c4d1675d8482e35d11d7af0000618e78'
qpx_apikey ='aizasycyeo6vp6mxukyneolvvjv-tyaagxyzjzc'

celery_always_eager = True

# a sample logging configuration. the only tangible logging
# performed by this configuration is to send an email to
# the site admins on every http 500 error when debug=false.
# see http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
logging = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.requiredebugfalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'error',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.adminemailhandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'error',
            'propagate': True,
        },
    }
}



# sensible settings for celery
celery_always_eager = False
celery_acks_late = True
celery_task_publish_retry = True
celery_disable_rate_limits = False

# by default we will ignore result
# if you want to see results and try out tasks interactively, change it to false
# or change this setting on tasks level
celery_ignore_result = True
celery_send_task_error_emails = False
celery_task_result_expires = 600

# set redis as celery result backend
celery_result_backend = 'redis://%s:%d/%d' % (redis_host, redis_port, redis_db)
celery_redis_max_connections = 1

# don't use pickle as serializer, json is much safer
celery_task_serializer = "json"
celery_accept_content = ['application/json']

celeryd_hijack_root_logger = False
celeryd_prefetch_multiplier = 1
celeryd_max_tasks_per_child = 1000


