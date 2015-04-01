from django.core.management.base import BaseCommand, CommandError
from flights.models import Flight, Airport, Route
from flights.flightdata import inbound_flights, outbound_flights
from location.models import City
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from time import sleep

# def build_route(self, content_type, object_id, ):

london_airports = ['LHR','LGW','STN','LCY','LTN']
#
# london_airports =['LGW', 'LHR']


class Command(BaseCommand):
    help = 'Creates the routes to and from each airport'

    def handle(self, *args, **options):
        london = City.objects.get(name='London', country__name="United Kingdom")
        for london_airport in london_airports:
            london_airport = Airport.objects.get(iata=london_airport)
            airports = Airport.objects.filter(country__continent='EU')
            airports = airports.exclude(country__name='United Kingdom')

            for airport in airports:
                #this is the airport to which the flight is going to
                route, created = Route.objects.get_or_create(origin = london_airport.city, destination=airport.city)
                airport_inbound_flights = Flight.objects.filter(departure_airport=airport, arrival_airport=london_airport)
                airport_outbound_flights = Flight.objects.filter(arrival_airport=airport, departure_airport=london_airport)


                #get or create round trip
                #this is the airport to which the flight is going to
                # route = Route(destination_airport = airport)
                route.origin_airport=london_airport
                route.destination=airport.city
                route.origin=london

                if len(airport_outbound_flights) != 0:
                    for flight in airport_outbound_flights:
                        route.outbound_flights.add(flight)
                        route.departure_date = airport_outbound_flights[0].departure_time.date()

                if len(airport_inbound_flights) != 0:
                    for flight in airport_inbound_flights:
                        route.inbound_flights.add(flight)
                        route.return_date = airport_inbound_flights[0].departure_time.date()
                route.save()










