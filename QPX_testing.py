import requests
import json
from passportfridays.settings import QPX_APIKEY
import urllib2

code = {
  "request": {
    "passengers": {
      "kind": "qpxexpress#passengerCounts",
      "adultCount": 1,
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": "DCA",
        "destination": "NYC",
        "date": "2015-11-20",
      }
    ],
    "refundable": "false",
    "solutions": 5
  }
}
headers ={'Content-type': 'application/json'}
url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s' %QPX_APIKEY
jsonreq = json.dumps(code, encoding = 'utf-8')
r = requests.post(url, data = jsonreq, headers =headers)
print r.status_code
returned_data = json.loads(r.content)
print returned_data


'''either book tickets through the website or offer customers to redirect to the airlines website'''
#http://www.ypsilon.net/
#http://xmldocs.travelfusion.com/
