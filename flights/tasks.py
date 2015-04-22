from __future__ import absolute_import
from datetime import timedelta
from flights.models import Flight, Slice
from flights.utils import TemplateEmailer, get_flight_prices
from celery import shared_task
from flights.utils import get_flight_data
from django.utils import timezone
from location.models import City, Destinations
from weekend.models import Dates


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

def get_dates(days):
    future_date = timezone.now()+timedelta(days=days)
    return Dates.objects.filter(departure_date__gte=future_date)[:1][0]

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
def get_upcoming_flights(days=120, airports = ['LHR', 'LGW'], hours = [18, 19, 20, 21, 22, 23]):
    """get the inbound and outbound flight times for airports
    this task should be run every week
    first the function that gets the dates for that weekend should be called
    Then this function can be called"""

    dates = get_dates(days)
    for airport in airports:
        for hour in hours:
            get_flight_data(airport, dates, hour)


@shared_task
def get_possible_destinations(days=120, city=None):
    '''pass a city code to this function to find and save a list of possible destinations
    this task should be run once a week on wednesdays to take into account for public holidays
    after this task the get flight prices should run to get prices for all these destinations

    This function should only be run once flight data for this weekend has been populated
    So first run the task get_airport flight for that weekend, then run this task'''
    dates = get_dates(days)
    if city is None:
        city = City.objects.get(name='London', country__name='United Kingdom')
    else:
        pass
    city.possible_destinations(dates)


@shared_task
def get_inital_flight_prices(days=120):
    dates = get_dates(days)
    destinations = Destinations.objects.get(dates=dates)
    cites = destinations.destinations.all()
    for city in cites:
        get_flight_prices(destinations.origin, city, dates)

@shared_task
def update_flight_prices(limit):
    slices = Slice.objects.all().order_by('price')[:limit]
    for slice in slices:
        get_flight_prices(slice.origin, slice.destination, slice.dates)














