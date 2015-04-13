# Django settings for passportfridays project.
import os
# from celery.schedules import crontab
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# import sys
# if 'test' in sys.argv or 'test_coverage' in sys.argv:
#     #we change the host to none for codeship
#     DATABASES['default']['HOST'] = None

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
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


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/static/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "project_static"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e9_mqi1#wwr6b0$1prc^)_aolc7q!oex(7m)^duq&do79q-71%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
        # 'email_user.backends.EmailUserAuth',
        'django.contrib.auth.backends.ModelBackend',
    )

ROOT_URLCONF = 'passportfridays.urls'

LOGIN_URL = '/signin'
LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'email_user.EmailUser'

EAN_HOTEL_API  ={
    'application' : 'testing app',
    'key': '3rdyahz9hnfnba6nuqu8gedp',
    'shared_secret': 'UzhYX7kX',
}

#read this for google flights
#http://www.nohup.in/blog/using-json-google-flights

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'passportfridays.wsgi.application'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'flights',
    'email_user',
    'weekend',
    'django_extensions',
    'location',
    'accommodation',
    'genericadmin',
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
#
# CELERYBEAT_SCHEDULE = {
#     # Executes every Wednesday morning at 7:30 A.M
#     'add-every-monday-morning': {
#         'task': 'flights.tasks.get_airport_flight',
#         'schedule': crontab(hour=7, minute=30, day_of_week=3),
#         'args': (),
#     },
# }
#
# CELERYBEAT_SCHEDULE = {
#     # Executes every Wednesday morning at 7:30 A.M
#     'add-every-monday-morning': {
#         'task': 'flights.tasks.get_flight_prices',
#         'schedule': crontab(minute='*'),
#         'args': (),
#     },
# }