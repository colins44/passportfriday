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
        "origin": "{{ route.origin.code }}",
        "destination": "{{ route.destination.code }}",
        "date": "{{ route.departure_date|date:"c" }}",
        "maxStops": 0,
        "permittedDepartureTime": {
          "earliestTime": "18:00",
          "latestTime": "23:59"
        }
      },
      {
        "origin": "{{ route.destination.code }}",
        "destination": "{{ route.origin.code }}",
        "date": "{{ route.return_date|date:"c" }}",
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
    "solutions": 1,
    "refundable": false
  }
}"""

class Command(BaseCommand):
    help = 'Get the prices for the routes in the database' \
           'should be run after the delete_no_routes command'

    def handle(self, *args, **options):
        for route in Route.objects.all()[:1]:
            t = Template(template)
            rendered = t.render(Context({'route':route}))
            print rendered
            headers ={'Content-type': 'application/json'}
            url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s' %QPX_APIKEY
            # jsonreq = json.dumps(code, encoding = 'utf-8')
            r = requests.post(url, data = rendered, headers =headers)
            print r.status_code
            returned_data = json.loads(r.content)
            print returned_data
            print '$$$$$$$$$$'
            trips = returned_data.get('trips').get('tripOption')
            for trip in trips:
                print '$$$$$$$$$$$$$'
                print trip.get('saleTotal')
                for slice in trip.get('slice'):
                    for segment in slice.get('segment'):
                        print segment.get('flight').get('carrier')
                        print segment.get('flight').get('number')

