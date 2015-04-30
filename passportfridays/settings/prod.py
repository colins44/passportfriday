from passportfridays.settings.common import *

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "passportfridays"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_UR

DATABASES = {
    'default':
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'passportfridays',
        'USER' : 'devuser',
        'PASSWORD' : 'clownshoes',
        'HOST' : 'passportfridays.cgh8jbmyus8x.eu-west-1.rds.amazonaws.com',
        'PORT' : '5432',
    }
}