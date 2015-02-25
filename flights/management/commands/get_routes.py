from django.core.management.base import BaseCommand, CommandError
from flights.models import Flight, Airport, Route
from flights.flightdata import inbound_flights, outbound_flights
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from time import sleep

# def build_route(self, content_type, object_id, ):

# london_airports = ['LHR','LGW','STN','LCY','LTN']

london_airports =['LGW', 'LHR']


class Command(BaseCommand):
    help = 'Creates the routes to and from each airport'

    def handle(self, *args, **options):

        for x in london_airports:
            london_airport = Airport.objects.get(code=x)
            airports = Airport.objects.exclude(code=outbound_flights['scheduledFlights'][0]['departureAirportFsCode'])

            for airport in airports:
                #this is the airport to which the flight is going to
                airport_inbound_flights = Flight.objects.filter(departure_airport=airport, arrival_airport=london_airport)
                airport_outbound_flights = Flight.objects.filter(arrival_airport=airport, departure_airport=london_airport)


                #get or create round trip
                #this is the airport to which the flight is going to
                route = Route(airport = airport)
                route.save()
                if len(airport_outbound_flights) != 0:
                    for flight in airport_outbound_flights:
                        route.outbound_flights.add(flight)

                if len(airport_inbound_flights) != 0:
                    for flight in airport_inbound_flights:
                        route.inbound_flights.add(flight)
                route.save()







