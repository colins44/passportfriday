from django.core.management.base import BaseCommand, CommandError
from flights.models import Route
import subprocess
import os

class Command(BaseCommand):
    help = 'Get the prices for the routes in the database' \
           'should be run after the delete_no_routes command'

    def handle(self, *args, **options):
        for route in Route.objects.all()[:1]:
            inbound_flight_date = route.inbound_flights.all()[0].departure_time.date().strftime('%Y-%m-%d')
            for flight in route.outbound_flights.all():
                print flight.departure_time
                child = subprocess.Popen(['python',"scraping.py"], stdin=subprocess.PIPE)
                child.communicate(os.linesep.join([flight.departure_airport.code, flight.arrival_airport.code, flight.departure_time.date().strftime('%Y-%m-%d'), inbound_flight_date, flight.carrier_code]))





