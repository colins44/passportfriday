import re
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.views.generic.base import TemplateResponseMixin
import requests
import json
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from location.models import City, Currency
from flights.models import Airport, Flight, Slice, HistoricSlice
from weekend.models import Dates
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

def make_historic_slice(slice):
    data = {}
    for field in slice._meta.fields:
        data[field.name] = getattr(slice, field.name)
    hs = HistoricSlice.objects.create(**data)
    hs.save()

def create_slice(price, outbound_flight, inbound_flight):
    price = re.split('(\d.*)',price)
    currency = Currency.objects.get(code=price[0])
    price = price[1]
    outbound_date = datetime.strptime(outbound_flight.get('leg')[0].get('departureTime')[:16], '%Y-%m-%dT%H:%M')
    outbound_flight_departure_airport = Airport.objects.get(iata=outbound_flight.get('leg')[0].get('origin'))
    outbound_flight_arrival_airport = Airport.objects.get(iata=outbound_flight.get('leg')[0].get('destination'))
    outbound_flight_departure_time = datetime.strptime(outbound_flight.get('leg')[0].get('departureTime')[:16], '%Y-%m-%dT%H:%M')
    outbound_flight_arrival_time = datetime.strptime(outbound_flight.get('leg')[0].get('arrivalTime')[:16], '%Y-%m-%dT%H:%M')
    outbound_flight_carrier_code = outbound_flight.get('flight').get('carrier')
    outbound_flight_flight_no = outbound_flight.get('flight').get('number')
    inbound_date = datetime.strptime(inbound_flight.get('leg')[0].get('departureTime')[:16], '%Y-%m-%dT%H:%M')
    inbound_flight_departure_airport = Airport.objects.get(iata=inbound_flight.get('leg')[0].get('origin'))
    inbound_flight_arrival_airport = Airport.objects.get(iata=inbound_flight.get('leg')[0].get('destination'))
    inbound_flight_departure_time =  datetime.strptime(inbound_flight.get('leg')[0].get('departureTime')[:16], '%Y-%m-%dT%H:%M')
    inbound_flight_arrival_time = datetime.strptime(inbound_flight.get('leg')[0].get('arrivalTime')[:16], '%Y-%m-%dT%H:%M')
    inbound_flight_carrier_code = inbound_flight.get('flight').get('carrier')
    inbound_flight_flight_no = inbound_flight.get('flight').get('number')
    ob_flight, _ = Flight.objects.get_or_create(carrier_code=outbound_flight_carrier_code,
                                                flight_no=outbound_flight_flight_no,
                                                departure_airport=outbound_flight_departure_airport,
                                                arrival_airport=outbound_flight_arrival_airport,
                                                departure_time__year=outbound_date.year,
                                                departure_time__month=outbound_date.month,
                                                departure_time__day=outbound_date.day,
                                                )
    inb_flight, _ = Flight.objects.get_or_create(carrier_code=inbound_flight_carrier_code,
                                                flight_no=inbound_flight_flight_no,
                                                departure_airport=inbound_flight_departure_airport,
                                                arrival_airport=inbound_flight_arrival_airport,
                                                departure_time__year=inbound_date.year,
                                                departure_time__month=inbound_date.month,
                                                departure_time__day=inbound_date.day,
                                                )
    ob_flight.departure_date=outbound_flight_departure_time
    ob_flight.arrival_date=outbound_flight_arrival_time
    inb_flight.departure_date=inbound_flight_departure_time
    inb_flight.arrival_date=inbound_flight_arrival_time
    ob_flight.save()
    inb_flight.save()
    dates = Dates.objects.get(departure_date=outbound_date.date(), return_date=inbound_date.date())

    Slice.objects.create(
        dates=dates,
        origin=outbound_flight_departure_airport.city,
        destination=outbound_flight_arrival_airport.city,
        outbound_flight=ob_flight,
        inbound_flight=inb_flight,
        currency=currency,
        price=price,
    )


def process_qpx(qpx_data, dates):
    '''this function takes the dict that is returned from qpx breaks it down itnot the slice and saves it
    by doing this we can get the data through an api call or any other function'''
    if type(qpx_data) is str:
        returned_data = json.loads(qpx_data)
    else:
        returned_data = qpx_data
    #first you have to find all the other slices for that destination for that date and delete there
    #this is cause prices will go up, but before we delete the slice we should log the price between the two cites
    trip_data = returned_data.get('trips').get('data')
    try:
        origin_city = trip_data.get('city')[0]
    except TypeError:
        pass
    else:
        try:
            origin_city = City.objects.get(name=origin_city.get('name'), code=origin_city.get('code'))
        except City.DoesNotExist:
            origin_city = None
        destination_city = trip_data.get('city')[1]
        try:
            destination_city = City.objects.get(name=destination_city.get('name'))
        except City.DoesNotExist:
            destination_city = None
        if origin_city and destination_city:
            slices = Slice.objects.filter(dates=dates,
                                        origin=origin_city,
                                        destination=destination_city,
                                        )
            for slice in slices:
                make_historic_slice(slice)
                slice.delete()

        #Then we start to process the qpx data
        trips = returned_data.get('trips').get('tripOption')
        for trip in trips:
            price = trip.get('saleTotal')
            slices = trip.get('slice')
            outbound_flight = slices[0]
            inbound_flight = slices[1]
            outbound_flight = outbound_flight.get('segment')[0]
            inbound_flight = inbound_flight.get('segment')[0]
            create_slice(price, outbound_flight, inbound_flight)


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
    process_qpx(r.content, dates)

def flight_price_lookup_logic():
    """Here we put the logic that dictates which city pairs for which dates the QPX API should be called for"""
    slices = Slice.objects.all().order_by('price')[:50]
    where_to_go =[]
    for slice in slices:
        data ={}
        data['origin_city']:slice.origin,
        data['destination']:slice.destination,
        data['dates']:slice.dates
        where_to_go.append(data)
    return data

