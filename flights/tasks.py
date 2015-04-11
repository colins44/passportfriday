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

template ="""{
  "request": {
    "slice": [
      {
        "origin": "{{ route.origin.code }}",
        "destination": "{{ route.destination.code }}",
        "date": "{{ route.departure_date|date:"c" }}",
        "maxStops": 0,
        "permittedDepartureTime": {
          "earliestTime": "18:00",
          "latestTime": "23:59"
        }
      },
      {
        "origin": "{{ route.destination.code }}",
        "destination": "{{ route.origin.code }}",
        "date": "{{ route.return_date|date:"c" }}",
        "maxStops": 0,
        "permittedDepartureTime": {
          "earliestTime": "15:00",
          "latestTime": "23:59"
        }
      }
    ],
    "passengers": {
      "adultCount": 1,
      "infantInLapCount": 0,
      "infantInSeatCount": 0,
      "childCount": 0,
      "seniorCount": 0
    },
    "solutions": 1,
    "refundable": false
  }
}"""

@shared_task
def get_flight_price(route):
    t = Template(template)
    rendered = t.render(Context({'route':route}))
    headers ={'Content-type': 'application/json'}
    url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s' %QPX_APIKEY
    r = requests.post(url, data=rendered, headers =headers)
    returned_data = json.loads(r.content)
    print returned_data
    slice = returned_data.get('trips').get('tripOption')
    print slice.get('saleTotal')
    for segment in slice.get('segment'):
        print segment.get('flight').get('carrier')
        print segment.get('flight').get('number')

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







