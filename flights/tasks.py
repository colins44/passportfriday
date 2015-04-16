from __future__ import absolute_import
from datetime import timedelta
from flights.models import Flight
from flights.utils import TemplateEmailer
from celery import shared_task
from flights.utils import get_flight_data
from django.utils import timezone
from weekend.models import Dates
from location.models import City


@shared_task
def send_email(template, context,  to, subject):
    email = TemplateEmailer(
                template=template,
                context=context,
                subject=subject,
                to=to,
            )
    email.send()

@shared_task
def test_email():
    templates = ['flights/emails/set_up_notifications.html',]
    for template in templates:
        email = TemplateEmailer(
                    template=template,
                    context={},
                    subject='testing',
                    to=['colin.pringlewood@gmail.com',],
                )
        email.send()


@shared_task
def get_weekend_dates(days_from_now=120):
    #TODO thes has to be better logic for this
    now = timezone.now()
    future = now + timedelta(days=days_from_now)
    cut_off = now + timedelta(days=(days_from_now+4))
    future_weekend = Dates.objects.get(departure_date__gte=future, departure_date__lte=cut_off)
    return future_weekend


@shared_task
def get_airport_flight(airports = ['LHR', 'LGW'], hours = [18, 19, 20, 21, 22, 23], dates=None):
    """get the inbound and outbound flight times for airports
    this task should be run every week
    first the function that gets the dates for that weekend should be called
    Then this function can be called"""
    if not dates:
        #we will get the flights 120 days from now
        future = (timezone.now())+timedelta(days=120)
        dates = Dates.objects.filter(departure_date__gte=future)[:1][0]
    for airport in airports:
        for hour in hours:
            get_flight_data(airport, dates, hour)

@shared_task
def delete_old_flights():
    """delete old flights to save DB space"""
    #TODO set up con job to run this every week
    now = timezone.now
    one_week_ago = now - timedelta(days=7)
    flights = Flight.objects.filter(departure_time__lte=one_week_ago)
    for flight in flights:
        flight.delete()

@shared_task
def get_possible_destinations(dates, city=None):
    '''pass a city code to this function to find and save a list of possible destinations
    this task should be run once a week on wednesdays to take into account for public holidays
    after this task the get flight prices should run to get prices for all these destinations

    This function should only be run once flight data for this weekend has been populated
    So first run the task get_airport flight for that weekend, then runn this task'''
    if city is None:
        city = City.objects.get(name='London', country__name='United Kingdom')
    else:
        pass
    city.possible_destinations(dates)


@shared_task
def flight_prices_lookup_logic():
    #maybe here goes the logic as to how to lookup the flight and what is important to us
    pass


@shared_task
def get_flight_prices(slice):
    '''call the get flight prices function call here and update the slice prices'''
    print 'colin'


@shared_task
def add():
    print 'colin'
    print '$$$$$$$$$$$$$$$$'
    print '$$$$$$$$$$$$$$$$'
    print '$$$$$$$$$$$$$$$$'













