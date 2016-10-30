import json

import requests

EAN_HOTEL_API = {
    'application': 'testing app',
    'key': '3rdyahz9hnfnba6nuqu8gedp',
    'shared_secret': 'UzhYX7kX',
}
api_key = '3rdyahz9hnfnba6nuqu8gedp'
cid = '55505'
customerIpAddress = '37.157.38.18'
customerUserAgent = 'mobile_web'
customerSessionId = 'somerandoneidentifyingstring'
minorRev = '28'
locale = 'en_US'
currencyCode = 'GBP'
city = 'london'
countryCode = 'UK'
# american dates mm/dd/yyyy
arrivalDate = '03/27/2015'
departureDate = '03/29/2015'
room1 = '2'

q = ''

url = 'http://dev.api.ean.com/ean-services/rs/hotel/v3/list?apiKey=%s&cid=%s&customerIpAddress=%s' \
      '&customerUserAgent=%s&customerSessionId=%s&minorRev=%s&locale=%s&currencyCode=%s&city=%s' \
      '&countryCode=%s&arrivalDate=%s&departureDate=%s&room1=%s' % (
          api_key, cid, customerIpAddress, customerUserAgent, customerSessionId, minorRev, locale,
          currencyCode, city, countryCode, arrivalDate, departureDate, room1)

print(url)

# print url


eanurl = 'http://dev.api.ean.com/ean-services/rs/hotel/v3/list?apiKey=3rdyahz9hnfnba6nuqu8gedp' \
         '&cid=55505'

city = 'london'
countryCode = 'UK'
arrivalDate = '09/19/2015'
departureDate = '09/21/2015'
room1 = '2'
ean_url = 'http://dev.api.ean.com/ean-services/rs/hotel/v3/list?apiKey=3rdyahz9hnfnba6nuqu8gedp' \
          '&cid=55505&customerIpAddress=37.157.38.18&customerUserAgent=mobile_web' \
          '&customerSessionId=somerandoneidentifyingstring&minorRev=28&locale=en_US&currencyCode' \
          '=GBP&arrivalDate=03%2F27%2F2015&city=london&departureDate=03%2F29%2F2015&countryCode' \
          '=UK&room1=2'

payload = {
    'city': 'london',
    # 'countryCode':'UK',
    'arrivalDate': '06/27/2015',
    'departureDate': '06/30/2015',
    'room1': '2',
}
#
r = requests.get(ean_url, params=payload)
print(r.url)
print(r.status_code)
data = json.loads(r.content)
hotels = data.get('HotelListResponse').get('HotelList').get('HotelSummary')
for hotel in hotels:
    # print hotel.get('name'), hotel.get('highRate'), hotel.get('lowRate')
    # print '$$$$$$$$$$$'
    room = hotel.get('RoomRateDetailsList').get('RoomRateDetails')
    # print room
    # print '$$$$$$$$$$'
    rate = room.get('RateInfos').get('RateInfo').get('ChargeableRateInfo').get('@total')
    print(rate)
