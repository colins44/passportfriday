# # Django settings for passportfridays project.
# import os
# from kombu import Exchange, Queue
# # from celery.scheduler import crontab
# from datetime import timedelta
# DEBUG = True
# TEMPLATE_DEBUG = DEBUG
#
# ADMINS = (
#     # ('Your Name', 'your_email@example.com'),
# )
#
# MANAGERS = ADMINS
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#
# #docker DB setup
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }
# #vagrant db setup
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
# #         'NAME': 'postgres',
# #         'USER': 'postgres',
# #         'PASSWORD': '',
# #         'HOST': '127.0.0.1',
# #         'PORT': '',
# #     }
# # }
#
# # import sys
# # if 'test' in sys.argv or 'test_coverage' in sys.argv:
# #     #we change the host to none for codeship
# #     DATABASES['default']['HOST'] = None
#
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'colin.pringle-wood@ostmodern.co.uk'
# EMAIL_HOST_PASSWORD = 'thisisthepassword'
# DEFAULT_FROM_EMAIL = 'colin.pringle-wood@ostmodern.co.uk'
# DEFAULT_TO_EMAIL = 'colin.pringle-wood@ostmodern.co.uk'
#
# DEFAULT_FROM_EMAIL = 'The Passport Fridays Team <noreply@passportfridays.com>'
# DEFAULT_FROM_NAME = 'The Passport Fridays Team'
#
# LOGIN_REDIRECT_URL = '/account/'
# LOGOUT_REDIRECT_URL = '/'
#
# # Redis
#
# REDIS_PORT = 6379
# REDIS_DB = 0
# REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')
#
# RABBIT_HOSTNAME = os.environ.get('RABBIT_PORT_5672_TCP', 'localhost:5672')
#
#
# # Hosts/domain names that are valid for this site; required if DEBUG is False
# # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = []
#
# # Local time zone for this installation. Choices can be found here:
# # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# # although not all choices may be available on all operating systems.
# # In a Windows environment this must be set to your system time zone.
# TIME_ZONE = 'UTC'
#
# # Language code for this installation. All choices can be found here:
# # http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en-us'
#
# SITE_ID = 1
#
# # If you set this to False, Django will make some optimizations so as not
# # to load the internationalization machinery.
# USE_I18N = True
#
# # If you set this to False, Django will not format dates, numbers and
# # calendars according to the current locale.
# USE_L10N = True
#
# # If you set this to False, Django will not use timezone-aware datetimes.
# USE_TZ = True
#
# # Absolute filesystem path to the directory that will hold user-uploaded files.
# # Example: "/var/www/example.com/media/"
# MEDIA_ROOT = ''
#
# # URL that handles the media served from MEDIA_ROOT. Make sure to use a
# # trailing slash.
# # Examples: "http://example.com/media/", "http://media.example.com/"
# MEDIA_URL = '/static/media/'
#
# # Absolute path to the directory static files should be collected to.
# # Don't put anything in this directory yourself; store your static files
# # in apps' "static/" subdirectories and in STATICFILES_DIRS.
# # Example: "/var/www/example.com/static/"
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# # URL prefix for static files.
# # Example: "http://example.com/static/", "http://static.example.com/"
# STATIC_URL = '/static/'
#
# # Additional locations of static files
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "project_static"),
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# )
#
# # List of finder classes that know how to find static files in
# # various locations.
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )
#
# # Make this unique, and don't share it with anybody.
# SECRET_KEY = 'e9_mqi1#wwr6b0$1prc^)_aolc7q!oex(7m)^duq&do79q-71%'
#
# # List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# #     'django.template.loaders.eggs.Loader',
# )
#
# MIDDLEWARE_CLASSES = (
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     # Uncomment the next line for simple clickjacking protection:
#     # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )
#
# AUTHENTICATION_BACKENDS = (
#         # 'email_user.backends.EmailUserAuth',
#         'django.contrib.auth.backends.ModelBackend',
#     )
#
# ROOT_URLCONF = 'passportfridays.urls'
#
# LOGIN_URL = '/signin'
# LOGOUT_REDIRECT_URL = '/'
#
# AUTH_USER_MODEL = 'email_user.EmailUser'
#
# EAN_HOTEL_API  ={
#     'application' : 'testing app',
#     'key': '3rdyahz9hnfnba6nuqu8gedp',
#     'shared_secret': 'UzhYX7kX',
# }
#
# #read this for google flights
# #http://www.nohup.in/blog/using-json-google-flights
#
# # Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'passportfridays.wsgi.application'
#
# import os
# TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)
#
# INSTALLED_APPS = (
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.sites',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     # Uncomment the next line to enable the admin:
#     'django.contrib.admin',
#     # Uncomment the next line to enable admin documentation:
#     # 'django.contrib.admindocs',
#     'flights',
#     'email_user',
#     'weekend',
#     'django_extensions',
#     'location',
#     'accommodation',
#     'genericadmin',
# )
#
# FLIGHTSTATS_APPID = '92c5179a'
# FLIGHTSTATS_APPKEY = 'c4d1675d8482e35d11d7af0000618e78'
# QPX_APIKEY ='AIzaSyCyEO6Vp6MxuKYnEOlvVJV-TyaAgXyZJZc'
#
# CELERY_ALWAYS_EAGER = True
#
# # A sample logging configuration. The only tangible logging
# # performed by this configuration is to send an email to
# # the site admins on every HTTP 500 error when DEBUG=False.
# # See http://docs.djangoproject.com/en/dev/topics/logging for
# # more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }
# # Redis
#
# REDIS_PORT = 6379
# REDIS_DB = 0
# REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')
#
# RABBIT_HOSTNAME = os.environ.get('RABBIT_PORT_5672_TCP', 'localhost:5672')
#
#
# if RABBIT_HOSTNAME.startswith('tcp://'):
#     RABBIT_HOSTNAME = RABBIT_HOSTNAME.split('//')[1]
#
# BROKER_URL = os.environ.get('BROKER_URL',
#                             '')
# if not BROKER_URL:
#     BROKER_URL = 'amqp://{user}:{password}@{hostname}/{vhost}/'.format(
#         user=os.environ.get('RABBIT_ENV_USER', 'admin'),
#         password=os.environ.get('RABBIT_ENV_RABBITMQ_PASS', 'mypass'),
#         hostname=RABBIT_HOSTNAME,
#         vhost=os.environ.get('RABBIT_ENV_VHOST', ''))
#
#
#
#
# BROKER_HEARTBEAT = '?heartbeat=30'
# if not BROKER_URL.endswith(BROKER_HEARTBEAT):
#     BROKER_URL += BROKER_HEARTBEAT
#
# BROKER_POOL_LIMIT = 1
# BROKER_CONNECTION_TIMEOUT = 10
#
# # Celery configuration
#
# # configure queues, currently we have only one
# CELERY_DEFAULT_QUEUE = 'default'
# CELERY_QUEUES = (
#     Queue('default', Exchange('default'), routing_key='default'),
# )
#
# # Sensible settings for celery
# CELERY_ALWAYS_EAGER = False
# CELERY_ACKS_LATE = True
# CELERY_TASK_PUBLISH_RETRY = True
# CELERY_DISABLE_RATE_LIMITS = False
#
# # By default we will ignore result
# # If you want to see results and try out tasks interactively, change it to False
# # Or change this setting on tasks level
# CELERY_IGNORE_RESULT = True
# CELERY_SEND_TASK_ERROR_EMAILS = False
# CELERY_TASK_RESULT_EXPIRES = 600
#
# # Set redis as celery result backend
# CELERY_RESULT_BACKEND = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)
# CELERY_REDIS_MAX_CONNECTIONS = 1
#
# # Don't use pickle as serializer, json is much safer
# CELERY_TASK_SERIALIZER = "json"
# CELERY_ACCEPT_CONTENT = ['application/json']
#
# CELERYD_HIJACK_ROOT_LOGGER = False
# CELERYD_PREFETCH_MULTIPLIER = 1
# CELERYD_MAX_TASKS_PER_CHILD = 1000
#
# # CELERYBEAT_SCHEDULE = {
# #     'add-every-30-seconds': {
# #         'task': 'flights.tasks.add',
# #         'schedule': timedelta(seconds=3),
# #         'args': ()
# #     },
# # }
# #
# # CELERYBEAT_SCHEDULE = {
# #     'add-every-min': {
# #         'task': 'flights.tasks.add',
# #         'schedule': crontab(),
# #         'args': ()
# #     },
# # }


"""
Django settings for pf2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from kombu import Exchange, Queue


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cmhz2hig9o-^va1y=8oeg-_xf54(40=6x+3%qnf0ttd+mgeoxh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'flights',
    'email_user',
    'weekend',
    'django_extensions',
    'location',
    'accommodation',
    'genericadmin',
    'djcelery',
    'kombu.transport.django',
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

AUTHENTICATION_BACKENDS = (
        # 'email_user.backends.EmailUserAuth',
        'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'passportfridays.urls'

WSGI_APPLICATION = 'passportfridays.wsgi.application'

AUTH_USER_MODEL = 'email_user.EmailUser'

import djcelery
djcelery.setup_loader()
BROKER_URL = 'django://'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# #docker DB setup
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }
#vagrant DB setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'passportfridays',
        'USER': 'devuser',
        'PASSWORD': 'clownshoes',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'colin.pringle-wood@ostmodern.co.uk'
EMAIL_HOST_PASSWORD = 'thisisthepassword'
DEFAULT_FROM_EMAIL = 'colin.pringle-wood@ostmodern.co.uk'
DEFAULT_TO_EMAIL = 'colin.pringle-wood@ostmodern.co.uk'

DEFAULT_FROM_EMAIL = 'The Passport Fridays Team <noreply@passportfridays.com>'
DEFAULT_FROM_NAME = 'The Passport Fridays Team'

LOGIN_REDIRECT_URL = '/account/'
LOGOUT_REDIRECT_URL = '/'

# Redis

REDIS_PORT = 6379
REDIS_DB = 0
REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')

RABBIT_HOSTNAME = os.environ.get('RABBIT_PORT_5672_TCP', 'localhost:5672')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/static/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "project_static"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

FLIGHTSTATS_APPID = '92c5179a'
FLIGHTSTATS_APPKEY = 'c4d1675d8482e35d11d7af0000618e78'
QPX_APIKEY ='AIzaSyCyEO6Vp6MxuKYnEOlvVJV-TyaAgXyZJZc'

CELERY_ALWAYS_EAGER = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Redis

# REDIS_PORT = 6379
# REDIS_DB = 0
# REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')
#
# RABBIT_HOSTNAME = os.environ.get('RABBIT_PORT_5672_TCP', 'localhost:5672')
#
#
# if RABBIT_HOSTNAME.startswith('tcp://'):
#     RABBIT_HOSTNAME = RABBIT_HOSTNAME.split('//')[1]
#
# BROKER_URL = os.environ.get('BROKER_URL',
#                             '')
# if not BROKER_URL:
#     BROKER_URL = 'amqp://{user}:{password}@{hostname}/{vhost}/'.format(
#         user=os.environ.get('RABBIT_ENV_USER', 'admin'),
#         password=os.environ.get('RABBIT_ENV_RABBITMQ_PASS', 'mypass'),
#         hostname=RABBIT_HOSTNAME,
#         vhost=os.environ.get('RABBIT_ENV_VHOST', ''))


#
#
# BROKER_HEARTBEAT = '?heartbeat=30'
# if not BROKER_URL.endswith(BROKER_HEARTBEAT):
#     BROKER_URL += BROKER_HEARTBEAT
#
# BROKER_POOL_LIMIT = 1
# BROKER_CONNECTION_TIMEOUT = 10

# Celery configuration

# configure queues, currently we have only one
CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

# Sensible settings for celery
CELERY_ALWAYS_EAGER = False
CELERY_ACKS_LATE = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_DISABLE_RATE_LIMITS = False

# By default we will ignore result
# If you want to see results and try out tasks interactively, change it to False
# Or change this setting on tasks level
CELERY_IGNORE_RESULT = True
CELERY_SEND_TASK_ERROR_EMAILS = False
CELERY_TASK_RESULT_EXPIRES = 600

# Set redis as celery result backend
CELERY_RESULT_BACKEND = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)
CELERY_REDIS_MAX_CONNECTIONS = 1

# Don't use pickle as serializer, json is much safer
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['application/json']

CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 1000
