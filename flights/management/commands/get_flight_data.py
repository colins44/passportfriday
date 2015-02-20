from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import requests
import datetime
import json
from time import sleep
from flights.models import Airport, Flight

leaving_hours =(18,)
airports =['HRE',]

class Command(BaseCommand):

    def handle(self, *args, **options):
        ###get fridays and sundays flights a month from now
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

                    Airport.objects.get_or_create(code=flight['departureAirportFsCode'])
                    Airport.objects.get_or_create(code=flight['arrivalAirportFsCode'])

                    departure_date = datetime.datetime.strptime(flight['departureTime'], '%Y-%m-%dT%H:%M:%S.000')
                    arrival_date = datetime.datetime.strptime(flight['arrivalTime'], '%Y-%m-%dT%H:%M:%S.000')
                    departure_airport = Airport.objects.get(code=flight['departureAirportFsCode'])
                    arrival_airport = Airport.objects.get(code=flight['arrivalAirportFsCode'])
                    Flight.objects.create(departure_airport=departure_airport,
                                          arrival_airport=arrival_airport,
                                          departure_time=departure_date,
                                          flight_no= flight['flightNumber'],
                                          carrier_code= flight['carrierFsCode'],
                                          arrival_time= arrival_date,
                                          stops= flight['stops'],)

            month_from_now +=datetime.timedelta(2)

            for hour in leaving_hours:
                url = "https://api.flightstats.com/flex/schedules/rest/v1/json/to/%s/arriving/%s/%s/%s/%d?appId=%s&appKey=%s" % (airport, month_from_now.year, month_from_now.month, month_from_now.day, hour, settings.FLIGHTSTATS_APPID, settings.FLIGHTSTATS_APPKEY)
                print url
                r = requests.get(url)
                inbound_flights = json.loads(r.content)
                sleep(2)

                for flight in inbound_flights['scheduledFlights']:

                    Airport.objects.get_or_create(code=flight['departureAirportFsCode'])
                    Airport.objects.get_or_create(code=flight['arrivalAirportFsCode'])

                    departure_date = datetime.datetime.strptime(flight['departureTime'], '%Y-%m-%dT%H:%M:%S.000')
                    arrival_date = datetime.datetime.strptime(flight['arrivalTime'], '%Y-%m-%dT%H:%M:%S.000')
                    departure_airport = Airport.objects.get(code=flight['departureAirportFsCode'])
                    arrival_airport = Airport.objects.get(code=flight['arrivalAirportFsCode'])
                    Flight.objects.create(departure_airport=departure_airport,
                                          arrival_airport=arrival_airport,
                                          departure_time=departure_date,
                                          flight_no= flight['flightNumber'],
                                          carrier_code= flight['carrierFsCode'],
                                          arrival_time= arrival_date,
                                          stops= flight['stops'],)





