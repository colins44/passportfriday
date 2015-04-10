from __future__ import absolute_import
from django.conf import settings
import datetime
from time import sleep
from flights.models import Airport, Flight
from location.models import City
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from flights.utils import TemplateEmailer
from celery import shared_task
import requests
from django.template import Context, Template
from passportfridays.settings import QPX_APIKEY
import json

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
def get_flight_data(airports, dates):
    leaving_hours =(18, 19, 20, 21, 22, 23)
    for airport in airports:
            for hour in leaving_hours:
                url = "https://api.flightstats.com/flex/schedules/rest/v1/json/from/%s/departing/%s/%s/%s/%d?appId=%s&appKey=%s" % (airport,
                                                                                                                                    dates.departure_date.year,
                                                                                                                                    dates.departure_date.month,
                                                                                                                                    dates.departure_date.day,
                                                                                                                                    hour,
                                                                                                                                    settings.FLIGHTSTATS_APPID,
                                                                                                                                    settings.FLIGHTSTATS_APPKEY)
                print url
                r = requests.get(url)
                outbound_flights = json.loads(r.content)
                sleep(2)

                for flight in outbound_flights['scheduledFlights']:
                    if flight["isCodeshare"] is False:

                        Airport.objects.get_or_create(iata=flight['departureAirportFsCode'])
                        Airport.objects.get_or_create(iata=flight['arrivalAirportFsCode'])

                        departure_date = datetime.datetime.strptime(flight['departureTime'], '%Y-%m-%dT%H:%M:%S.000')
                        arrival_date = datetime.datetime.strptime(flight['arrivalTime'], '%Y-%m-%dT%H:%M:%S.000')
                        departure_airport = Airport.objects.get(iata=flight['departureAirportFsCode'])
                        arrival_airport = Airport.objects.get(iata=flight['arrivalAirportFsCode'])
                        Flight.objects.create(departure_airport=departure_airport,
                                              arrival_airport=arrival_airport,
                                              departure_time=departure_date,
                                              flight_no= flight['flightNumber'],
                                              carrier_code= flight['carrierFsCode'],
                                              arrival_time= arrival_date,
                                              stops= flight['stops'],)

                for ap in outbound_flights['appendix']['airports']:
                    try:
                        city = City.objects.get(name__icontains=ap.get('city'), country__code=ap.get('countryCode'))
                    except ObjectDoesNotExist:
                        pass
                    except MultipleObjectsReturned:
                        pass
                    else:
                        city.code = ap.get('cityCode')
                        city.save()

            for hour in leaving_hours:
                url = "https://api.flightstats.com/flex/schedules/rest/v1/json/to/%s/arriving/%s/%s/%s/%d?appId=%s&appKey=%s" % (airport,
                                                                                                                                dates.departure_date.year,
                                                                                                                                dates.departure_date.month,
                                                                                                                                dates.departure_date.day,
                                                                                                                                hour,
                                                                                                                                settings.FLIGHTSTATS_APPID,
                                                                                                                                settings.FLIGHTSTATS_APPKEY)
                print url
                r = requests.get(url)
                inbound_flights = json.loads(r.content)
                sleep(2)

                for flight in inbound_flights['scheduledFlights']:
                    if flight["isCodeshare"] is False:

                        Airport.objects.get_or_create(iata=flight['departureAirportFsCode'])
                        Airport.objects.get_or_create(iata=flight['arrivalAirportFsCode'])

                        departure_date = datetime.datetime.strptime(flight['departureTime'], '%Y-%m-%dT%H:%M:%S.000')
                        arrival_date = datetime.datetime.strptime(flight['arrivalTime'], '%Y-%m-%dT%H:%M:%S.000')
                        departure_airport = Airport.objects.get(iata=flight['departureAirportFsCode'])
                        arrival_airport = Airport.objects.get(iata=flight['arrivalAirportFsCode'])
                        Flight.objects.create(departure_airport=departure_airport,
                                              arrival_airport=arrival_airport,
                                              departure_time=departure_date,
                                              flight_no= flight['flightNumber'],
                                              carrier_code= flight['carrierFsCode'],
                                              arrival_time= arrival_date,
                                              stops= flight['stops'],)

                for ap in inbound_flights['appendix']['airports']:
                    try:
                        city = City.objects.get(name__icontains=ap.get('city'), country__code=ap.get('countryCode'))
                    except ObjectDoesNotExist:
                        pass
                    except MultipleObjectsReturned:
                        pass
                    else:
                        city.code = ap.get('cityCode')
                        city.save()

@shared_task
def delete_old_flights():
    now = datetime.datetime.now()
    one_week_ago = now - datetime.timedelta(days=7)
    flights = Flight.objects.filter(departure_time__lte=one_week_ago)
    for flight in flights:
        flight.delete()


