from django.core.management.base import BaseCommand
from flights.models import Route, Slice, Flight
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
    "solutions": 20,
    "refundable": false
  }
}"""

class Command(BaseCommand):
    help = 'Get the prices for the routes in the database' \
           'should be run after the delete_no_routes command'

    def handle(self, *args, **options):
        for route in Route.objects.all()[3:4]:
            t = Template(template)
            rendered = t.render(Context({'route':route}))
            print rendered
            headers ={'Content-type': 'application/json'}
            url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s' %QPX_APIKEY
            r = requests.post(url, data = rendered, headers =headers)
            print r.status_code
            returned_data = json.loads(r.content)
            trips = returned_data.get('trips').get('tripOption')
            for trip in trips:
                print trip.get('saleTotal')
                slices = trip.get('slice')
                outbound_flight = slices[0]
                inbound_flight = slices[1]
                print '!!!!!!!!!!!!'
                print oubound_flight
                print inbound_flight
                inb_flight = Flight.objects.get(flight_no=inbound_flight.get('segment').get('flight').get('number'),
                                                carrier_code=inbound_flight.get('segment').get('flight').get('carrier'))
                outb_flight = Flight.objects.get(flight_no=outbound_flight.get('segment').get('flight').get('number'),
                                                carrier_code=outbound_flight.get('segment').get('flight').get('carrier'))

                slice, created = Slice.objects.get_or_create(
                    outbound_flight
                )
                # for slice in trip.get('slice'):
                #     print type(slice)
                #     print slice
                    # for segment in slice.get('segment'):
                    #     print type(segment)
                    #     print segment
                        # print segment.get('flight').get('carrier')
                        # print segment.get('flight').get('number')

