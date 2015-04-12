from __future__ import absolute_import
from datetime import timedelta
from flights.models import Flight, Destinations
from flights.utils import TemplateEmailer
from celery import shared_task
import requests
from django.template import Context, Template
from passportfridays.settings import QPX_APIKEY
import json
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
def get_airport_flight(days_from_now=60):
    """get the inbound and outbound flight times for airports
    this task should be run every week
    maybe wednesday would be best
    take into account public holidays"""
    airports =['LHR',]
    hours = [18, ]
    now = timezone.now()
    lookup= now + timedelta(days=days_from_now)
    end_lookup = now + timedelta(days=days_from_now+6)
    dates = Dates.objects.get(departure_date__gte=lookup, departure_date__lte=end_lookup)
    for airport in airports:
        for hour in hours:
            get_flight_data(airport, dates, hour)

@shared_task
def delete_old_flights():
    """delete old flights to save DB space"""
    now = timezone.now
    one_week_ago = now - timedelta(days=7)
    flights = Flight.objects.filter(departure_time__lte=one_week_ago)
    for flight in flights:
        flight.delete()

@shared_task
def get_possible_destinations(dates, city=None):
    '''pass a city code to this function to find and save a list of possible destinations
    this task should be run once a week on wednesdays to take into account for public holidays
    after this task the get flight prices should run to get prices for all these destinations'''
    if city is None:
        city = City.object.get(name='London', country='United Kingdom')
    else:
        pass
    destinations, dates = city.destinations(dates)
    destination, _ = Destinations.objects.get_or_create(origin=city, dates=dates)
    destination.destinations = destinations
    destination.save()

@shared_task
def flight_prices_lookup_logic():
    #maybe here goes the logic as to how to lookup the flight and what is important to us
    pass


@shared_task
def get_flight_prices(slice):
    '''call the get flight prices function call here and update the slice prices'''
    return None








