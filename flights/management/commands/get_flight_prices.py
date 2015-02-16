from django.core.management.base import BaseCommand, CommandError
from flights.models import Route

class Command(BaseCommand):
    help = 'Get the prices for the routes in the database' \
           'should be run after the delete_no_routes command'

    def handle(self, *args, **options):
        for route in Route.objects.all():
            origin_airport = route.airport.code
            print 'from: ', origin_airport
            print 'from: ', route.outbound_flights.all()[0].arrival_airport.code
            destination_airport = route.outbound_flights.all()[0].departure_airport.code
            print 'to: ', destination_airport
            leaving_date = route.outbound_flights.all()[0].departure_time.date()
            print 'leaving on: ' , leaving_date
            return_date = route.inbound_flights.all()[0].departure_time.date()
            print 'returning on: ', return_date



