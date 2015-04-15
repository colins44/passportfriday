"""
Django settings to allow independent testing of the skylark library.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os

from celery import Celery

from skylark.core import get_apps, get_auth_backends
from skylark.core.default_settings import *

AUTH_USER_MODEL = 'skylark_auth.BasicEmailUser'

TEST_RUNNER = 'skylark.utils.testrunner.EagerLoadingTestRunner'

# TODO: Which of these should be in default_settings?
ACCOUNT_ACTIVATION_DAYS = 30
ROOT_URLCONF = 'skylark.core.urls'
STRIPE_SECRET = None
EMAIL_WELCOME_MESSAGE = 'Your Account'
DEFAULT_FROM_NAME = 'Skylark'
EMAIL_ACTIVATION = False
WEBSITE_BASE_URL = 'https://example.com/'
WEBSITE_STATIC_IMAGES_SERVER = WEBSITE_BASE_URL
BOX_OFFICE_CUSTOMER_MODEL = 'box_office.Customer'

REINDEX_ON_SAVE = False
RECACHE_ON_SAVE = False

OOYALA_SECRETS = {
    'standard': 'dummy_secret',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'skylark',
    }
}

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '%ws4LA/L."99SaCxn6quz\G+S/6>c8edj}aRLO})#jn{%Eg!c*.[tPj2J~~<uSd'

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    'django_nose',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + get_apps()


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
] + get_auth_backends()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'skylark_auth.middleware.TokenMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Celery
CELERY_ALWAYS_EAGER = True
app = Celery()

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: INSTALLED_APPS)
