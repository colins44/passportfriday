import requests


EAN_HOTEL_API  ={
    'application' : 'testing app',
    'key': '3rdyahz9hnfnba6nuqu8gedp',
    'shared_secret': 'UzhYX7kX',
}

def build_url(xml):
    url = 'http://api.ean.com/ean-services/rs/hotel/v3/list?api_key=%s&city=%s' % (EAN_HOTEL_API['key'], 'london')
    return url

xml="""<HotelListRequest>
	<city>London</city>
</HotelListRequest>"""


url = build_url(xml)

r = requests.get(url)
print r.status_code
print r.content


#http://developer.ean.com/docs/hotel-list/examples/xml-basic-availability/


# http://api.ean.com/ean-services/rs/hotel/v3/list?
# apiKey=#####
# &cid=#####
# &customerIpAddress=#####
# &customerUserAgent=######
# &customerSessionId=#####
# &minorRev=##
# &locale=en_US
# &currencyCode=USD
# &xml=
# <HotelListRequest>
# 	<city>Seattle</city>
# 	<stateProvinceCode>WA</stateProvinceCode>
# 	<countryCode>US</countryCode>
# 	<arrivalDate>08/01/2015</arrivalDate>
# 	<departureDate>08/03/2015</departureDate>
# 	<RoomGroup>
# 	  <Room>
# 	    <numberOfAdults>2</numberOfAdults>
# 	  </Room>
# 	</RoomGroup>
# </HotelListRequest>