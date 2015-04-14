from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.views.generic.base import TemplateResponseMixin
import requests
import json
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from location.models import City
from flights.models import Airport, Flight
from datetime import datetime
from time import sleep
from django.template import Context, Template, loader
from passportfridays.settings import QPX_APIKEY

template ="""{
  "request": {
    "slice": [
      {
        "origin": "{{ origin.code }}",
        "destination": "{{ destination.code }}",
        "date": "{{ dates.departure_date|date:"c" }}",
        "maxStops": 0,
        "permittedDepartureTime": {
          "earliestTime": "18:00",
          "latestTime": "23:59"
        }
      },
      {
        "origin": "{{ destination.code }}",
        "destination": "{{ rorigin.code }}",
        "date": "{{ dates.return_date|date:"c" }}",
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
    "solutions": 20,
    "refundable": false
  }
}"""

def process_qpx(data):
    '''this function takes the dict that is returned from qpx breaks it down itnot the slice and saves it
    by doing this we can get the data through an api call or any other function'''
    if type(data) is str:
        returned_data = json.loads(data)
    else:
        returned_data = data
    trips = returned_data.get('trips').get('tripOption')
    for trip in trips:
        print trip.get('saleTotal')
        slices = trip.get('slice')
        print slices
        outbound_flight = slices[0]
        inbound_flight = slices[1]
        inbound_date = datetime.strptime(inbound_flight.get('segment')[0].get('leg')[0].get('departureTime')[:16], '%Y-%m-%dT%H:%M')
        outbound_date = datetime.strptime(outbound_flight.get('segment')[0].get('leg')[0].get('departureTime')[:16], '%Y-%m-%dT%H:%M')
        outbound_flight = outbound_flight.get('segment')[0]
        print outbound_flight
        print outbound_date
        print '$$$$$$$$$$'
        inbound_flight = inbound_flight.get('segment')[0]
        print inbound_flight
        print inbound_date
        print outbound_flight.get('leg')[0].get('origin')
        # outbound_flight_departure_airport = Airport.objects.get(iata=outbound_flight.get('leg')[0].get('origin'))
        # outbound_flight_arrival_airport = Airport.objects.get(iata=outbound_flight.get('leg')[0].get('destination'))
        # inbound_flight_departure_airport = Airport.objects.get(iata=inbound_flight.get('leg')[0].get('origin'))
        # inbound_flight_arrival_airport = Airport.objects.get(iata=inbound_flight.get('leg')[0].get('destination'))
        # print outbound_flight_arrival_airport
        # print outbound_flight_departure_airport
        # outbound_flight = Flight.objects.get_or_create(departure_airport=outbound_flight_departure_airport,
        #                                                arrival_airport=outbound_flight_arrival_airport,
        #                                                departure_time__year=outbound_date.year,
        #                                                departure_time__month=outbound_date.month,
        #                                                departure_time__day=outbound_date.day)
        # inbound_flight = Flight.objects.get_or_create(departure_airport=inbound_flight_departure_airport,
        #                                                arrival_airport=inbound_flight_arrival_airport,
        #                                                departure_time__year=inbound_date.year,
        #                                                departure_time__month=inbound_date.month,
        #                                                departure_time__day=inbound_date.day)
        # print '$$$$$$$$$$$'
        # print outbound_flight
        # print '$$$$$$$$$$$'
        # print inbound_flight


def process_qpx(data):
    '''this function takes the dict that is returned from qpx breaks it down itnot the slice and saves it
    by doing this we can get the data through an api call or any other function'''
    if type(data) is str:
        returned_data = json.loads(data)
    else:
        returned_data = data

    trips = returned_data.get('trips')
    kind = returned_data.get('kind')
    for trip in trips:
        tripOption = trip.get('tripOption')
        kind = trip.get('kind')
        data = trip.get('data')
        requestId = trip.get('requestId')




class TemplateEmailer(EmailMultiAlternatives, TemplateResponseMixin):

    def get_template_names(self, template):
        return template

    def __init__(self, template, context={}, **kwargs):
        t = loader.get_template(self.get_template_names(template))
        context.update({
            'email_from_name': settings.DEFAULT_FROM_NAME,
        })
        c = Context(context)
        self.rendered_message = t.render(c)
        if not kwargs.get('subject', None):
            kwargs['subject'] = settings.DEFAULT_FROM_NAME
        if not kwargs.get('from_email', None):
            kwargs['from_email'] = settings.DEFAULT_FROM_EMAIL

        super(TemplateEmailer, self).__init__(**kwargs)
        self.attach_alternative(self.rendered_message, "text/html")

    def send(self, fail_silently=False):
        """Just changes the default to fail_silently=True"""
        return super(TemplateEmailer, self).send(fail_silently)


def get_flight_data(airport, dates, hour):
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

def get_flight_prices(origin, destination, dates):
    '''pass an origin city and a destination city plus the weekend dates object to this function in order to get prices
    a slice object is then made within the DB of the returned data'''
    t = Template(template)
    rendered = t.render(Context({'origin':origin, 'destination':destination, 'dates':dates}))
    headers ={'Content-type': 'application/json'}
    url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s' % QPX_APIKEY
    r = requests.post(url, data = rendered, headers =headers)
    process_qpx(r.content)

