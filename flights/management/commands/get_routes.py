from django.core.management.base import BaseCommand, CommandError
from flights.models import Flight, Airport, Route
from flights.flightdata import inbound_flights, outbound_flights
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

# def build_route(self, content_type, object_id, ):


class Command(BaseCommand):
    help = 'Creates the routes to and from each airport'

    def handle(self, *args, **options):
        for flight in outbound_flights['scheduledFlights']:

            departure_airport = Airport.objects.get_or_create(code=flight['departureAirportFsCode'])
            arrival_airport = Airport.objects.get_or_create(code=flight['arrivalAirportFsCode'])

        for flight in outbound_flights['scheduledFlights']:
            try:
                departure_date = datetime.strptime(flight['departureTime'], '%Y-%m-%dT%H:%M:%S.000')
                arrival_date = datetime.strptime(flight['arrivalTime'], '%Y-%m-%dT%H:%M:%S.000')
                departure_airport = Airport.objects.get(code=flight['departureAirportFsCode'])
                arrival_airport = Airport.objects.get(code=flight['arrivalAirportFsCode'])
                Flight.objects.create(departure_airport=departure_airport,
                                      arrival_airport=arrival_airport,
                                      departure_time=departure_date,
                                      flight_no= flight['flightNumber'],
                                      carrier_code= flight['carrierFsCode'],
                                      arrival_time= arrival_date,
                                      stops= flight['stops'],)
            except ObjectDoesNotExist:
                print 'we could not find your airport, or more than one airport was returned'

        for flight in inbound_flights['scheduledFlights']:
            departure_airport = Airport.objects.get_or_create(code=flight['departureAirportFsCode'],)
            arrival_airport = Airport.objects.get_or_create(code=flight['arrivalAirportFsCode'])

        for flight in inbound_flights['scheduledFlights']:
            try:
                departure_date = datetime.strptime(flight['departureTime'], '%Y-%m-%dT%H:%M:%S.000')
                arrival_date = datetime.strptime(flight['arrivalTime'], '%Y-%m-%dT%H:%M:%S.000')
                departure_airport = Airport.objects.get(code=flight['departureAirportFsCode'])
                arrival_airport = Airport.objects.get(code=flight['arrivalAirportFsCode'])
                Flight.objects.create(departure_airport=departure_airport,
                                      arrival_airport=arrival_airport,
                                      departure_time=departure_date,
                                      flight_no= flight['flightNumber'],
                                      carrier_code= flight['carrierFsCode'],
                                      arrival_time= arrival_date,
                                      stops= flight['stops'],)
            except ObjectDoesNotExist:
                print 'we could not find your airport, or more than one airport was returned'

        airports = Airport.objects.all()

        for airport in airports:
            airport_inbound_flights = Flight.objects.filter(arrival_airport=airport)
            airport_outbound_flights = Flight.objects.filter(departure_airport=airport)

            #get or create round trip
            route = Route(airport = airport)
            route.save()
            if len(airport_outbound_flights) != 0:
                route.outbound_flights.add(airport_outbound_flights[0])

            if len(airport_inbound_flights) != 0:
                route.inbound_flights.add(airport_inbound_flights[0])
            route.save()





