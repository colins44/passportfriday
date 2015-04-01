from django.core.management.base import BaseCommand
from flights.models import Route
import requests
import json
from passportfridays.settings import QPX_APIKEY
from django.template import Context, Template




template ="""{
  "request": {
    "slice": [
      {
        "origin": "{{ route.origin.name }}",
        "destination": "{{ route.destination.name }}",
        "date": "{{ route.departure_date.year }}-{{ route.departure_date.month }}-{{ route.departure_date.day }}",
        "maxStops": 0,
        "permittedDepartureTime": {
          "earliestTime": "18:00",
          "latestTime": "23:59"
        }
      },
      {
        "origin": "{{ route.destination.name }}",
        "destination": "{{ route.origin.name }}",
        "date": "{{ route.return_date.year }}-{{ route.return_date.month }}-{{ route.return_date.day }}",
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

class Command(BaseCommand):
    help = 'Get the prices for the routes in the database' \
           'should be run after the delete_no_routes command'

    def handle(self, *args, **options):
        for route in Route.objects.all()[:1]:

            t = Template(template)
            print t.render(Context({'route':route}))
            #this is where we should call the google api