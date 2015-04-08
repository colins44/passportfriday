from __future__ import absolute_import

import os

from flights.utils import TemplateEmailer
from celery import shared_task
import requests
from django.template import Context, Template
from passportfridays.settings import QPX_APIKEY
import json

@shared_task
def send_email(template, context,  to, subject):
    email = TemplateEmailer(
                template=template,
                context=context,
                subject=subject,
                to=to,
            )
    email.send()

@shared_task
def test_email():
    templates = ['flights/emails/set_up_notifications.html',]
    for template in templates:
        email = TemplateEmailer(
                    template=template,
                    context={},
                    subject='testing',
                    to=['colin.pringlewood@gmail.com',],
                )
        email.send()

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

@shared_task
def get_flight_price(route):
    t = Template(template)
    rendered = t.render(Context({'route':route}))
    headers ={'Content-type': 'application/json'}
    url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s' %QPX_APIKEY
    r = requests.post(url, data=rendered, headers =headers)
    returned_data = json.loads(r.content)
    print returned_data
    slice = returned_data.get('trips').get('tripOption')
    print slice.get('saleTotal')
    for segment in slice.get('segment'):
        print segment.get('flight').get('carrier')
        print segment.get('flight').get('number')
