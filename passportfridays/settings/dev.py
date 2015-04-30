from passportfridays.settings.common import *

#vagrant db setup
databases = {
    'default': {
        'engine': 'django.db.backends.postgresql_psycopg2',
        'name': 'passportfridays',
        'user': 'devuser',
        'password': 'clownshoes',
        'host': 'localhost',
        'port': 5432,
    }
