import requests
import json
from django.core.management.base import BaseCommand, CommandError
from location.models import City, Currency
from accommodation.models import Accommodation, RoomRate
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

cities =[
    {
    'city':'London',
    'country':'United Kingdom'
    }
        ]

ean_url = 'http://dev.api.ean.com/ean-services/rs/hotel/v3/list?apiKey=3rdyahz9hnfnba6nuqu8gedp&cid=55505&customerIpAddress=37.157.38.18&customerUserAgent=mobile_web&customerSessionId=somerandoneidentifyingstring&minorRev=28'


class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'finds the prices of hotels in a city for a given weekend'

    def handle(self, *args, **options):
        for city in cities:
            city =  City.objects.get(name=city.get('city'), country__name = city.get('country'))
            currency = Currency.objects.get(code='GBP')
            payload = {
                'city':city.name,
                'countryCode':'UK',
                'arrivalDate':'06/27/2015',
                'departureDate':'06/30/2015',
                'room1':"2",
                'currencyCode':currency.code,
                'countryCode': 'UK',
                'locale':'en_US',
                }
            r = requests.get(ean_url, params=payload)
            data = json.loads(r.content)
            hotels =  data.get('HotelListResponse').get('HotelList').get('HotelSummary')
            for hotel in hotels:
                try:
                    accomo= Accommodation.objects.get(name=hotel.get('name'), ean_hotel_id=hotel.get('hotelId'),)
                except ObjectDoesNotExist:
                    accomo = Accommodation.objects.create(name = hotel.get('name'),
                                                          ean_hotel_id=hotel.get('hotelId'),
                                                          address1 = hotel.get('address1'),
                                                          address2 = hotel.get('address2'),
                                                          city =city,
                                                          type = hotel.get('propertyCategory'),
                                                          post_code = hotel.get('postalCode'),
                                                          rating = hotel.get('hotelRating'),
                                                          high_rate = hotel.get('highRate'),
                                                          low_rate = hotel.get('lowRate'))

                accomo.high_rate = hotel.get('highRate')
                accomo.low_rate = hotel.get('lowRate')
                accomo.save()

                room = hotel.get('RoomRateDetailsList').get('RoomRateDetails')
                rate = room.get('RateInfos').get('RateInfo')
                arrival_date = datetime.strptime(payload.get('arrivalDate'), '%m/%d/%Y')
                departure_date = datetime.strptime(payload.get('departureDate'), '%m/%d/%Y')
                try:
                    roomrate = RoomRate.objects.get(hotel=accomo,
                                                    quoted_occupancy=room.get('quotedRoomOccupancy'),
                                                    arrival_date=arrival_date,
                                                    departure_date=departure_date,
                                                    currency = currency)
                except ObjectDoesNotExist:
                    roomrate = RoomRate.objects.create(hotel=accomo,
                                                    quoted_occupancy=room.get('quotedRoomOccupancy'),
                                                    arrival_date=arrival_date,
                                                    departure_date=departure_date,
                                                    currency = currency)

                roomrate.max_occupancy = room.get('maxRoomOccupancy')
                roomrate.room_description = room.get('roomDescription')
                roomrate.room_type_code = room.get('roomTypeCode')
                roomrate.rate_code = room.get('rateCode')
                roomrate.no_of_adults = int(payload.get('room1'))
                roomrate.no_of_children = 0
                if rate.get('promo') == 'true':
                    roomrate.promotion = True
                else:
                    roomrate.promotion = False
                roomrate.deeplink = hotel.get('deepLink')
                roomrate.total = rate.get('ChargeableRateInfo').get('@total')
                roomrate.rate_type = rate.get('rateType')
                roomrate.save()
