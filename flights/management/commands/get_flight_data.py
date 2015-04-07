from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import requests
import datetime
import json
from time import sleep
from flights.models import Airport, Flight
from location.models import City
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


leaving_hours =(18, 19, 20, 21, 22, 23)

airports =['LHR', 'LGW']

class Command(BaseCommand):

    def handle(self, *args, **options):
        ###get fridays and sundays flights a month from now
        ###we have weekends now in the database so should be looking up on those values
        help = 'Get all the flights for the weekend from the flightstats api, then save the flight before making the route'
        month_from_now = datetime.date.today()+datetime.timedelta(days=30)
        while month_from_now.weekday() != 4:
            month_from_now +=datetime.timedelta(1)

        for airport in airports:
            for hour in leaving_hours:
                url = "https://api.flightstats.com/flex/schedules/rest/v1/json/from/%s/departing/%s/%s/%s/%d?appId=%s&appKey=%s" % (airport, month_from_now.year, month_from_now.month, month_from_now.day, hour, settings.FLIGHTSTATS_APPID, settings.FLIGHTSTATS_APPKEY)
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

                for airport in outbound_flights['appendix']['airports']:
                    try:
                        city = City.objects.get(name__icontains=airport.get('city'), country__code=airport.get('countryCode'))
                    except ObjectDoesNotExist:
                        pass
                    except MultipleObjectsReturned:
                        pass
                    else:
                        city.code = airport.get('cityCode')
                        city.save()

            month_from_now +=datetime.timedelta(2)

            for hour in leaving_hours:
                url = "https://api.flightstats.com/flex/schedules/rest/v1/json/to/%s/arriving/%s/%s/%s/%d?appId=%s&appKey=%s" % (airport, month_from_now.year, month_from_now.month, month_from_now.day, hour, settings.FLIGHTSTATS_APPID, settings.FLIGHTSTATS_APPKEY)
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

                for airport in inbound_flights['appendix']['airports']:
                    try:
                        city = City.objects.get(name__icontains=airport.get('city'), country__code=airport.get('countryCode'))
                    except ObjectDoesNotExist:
                        pass
                    except MultipleObjectsReturned:
                        pass
                    else:
                        city.code = airport.get('cityCode')
                        city.save()






