from django.core.management.base import BaseCommand, CommandError
from flights.models import Route

class Command(BaseCommand):
    help = 'Delete routes that have no return trip'

    def handle(self, *args, **options):
        for route in Route.objects.all():
            if len(route.inbound_flights.all()) == 0 or len(route.outbound_flights.all()) == 0:
                route.delete()
            else:
                pass