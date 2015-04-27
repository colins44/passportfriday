from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from datetime import timedelta


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'passportfridays.settings')

app = Celery('passportfridays')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

settings.CELERYBEAT_SCHEDULE = {
    #These items must happen in this order and need to be run once a week
    #first delete old flights
    # 'delete_old_flights': {
    #     'task': 'flights.tasks.delete_old_flights',
    #     'schedule': crontab(),
    #     'args': ()
    # },
    #second get the upcoming flights schedule from all london airports
    'get_upcoming_flights': {
        'task': 'flights.tasks.get_upcoming_flights',
        'schedule': crontab(53),
        'args': ()
    },
    # #Third find possible destinations
    'get_possible_destinations': {
        'task': 'flights.tasks.get_possible_destinations',
        'schedule': crontab(minute=57),
        'args': ()
    },
    # # # #Fourth get the flight prices for the possible destinations
    'get_flight_prices': {
        'task': 'flights.tasks.get_inital_flight_prices',
        'schedule': crontab(minute=05),
        'args': ()
    },
    # 'add-every-minute': {
    #     'task': 'flights.tasks.add',
    #     'schedule': crontab(),
    #     'args': ()
    # },
    #     'count-every-minute': {
    #     'task': 'flights.tasks.count',
    #     'schedule': crontab(),
    #     'args': ()
    # },
    #Once the above tasks have been run we can uses our qpx daily quota to look up flight prices on the other week days
    #this setting updates the 10 cheapest slices 5 times a day, except for the day we get intial prices
    # 'update_flight_prices': {
    #     'task': 'flights.tasks.update_flight_prices',
    #     'schedule': crontab(day_of_week='mon,tue,wed,fri,sat,sun',
    #                         hour='10,12,16,20,0',
    #                         minute=0),
    #     'args': (10)
    # },
    # 'update_flight_prices-every-min': {
    #     'task': 'flights.tasks.add',
    #     # 'schedule': crontab(day_of_week='mon,tue,wed,fri,sat,sun',
    #     #                     hour='16,17,18,19',
    #     #                     minute='9,10,11'),
    #     # 'schedule': crontab(day_of_week='mon,tue,wed,fri,sat,sun',hour="*/4", minute="*"),
    #     'schedule': crontab(),
    #     'args': (1)
    # },
    # 'add-every-30-seconds': {
    #     'task': 'flights.tasks.get_possible_destinations',
    #     'schedule': crontab(),
    #     'args': ()
    # }
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))