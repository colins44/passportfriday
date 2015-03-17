from django.core.management.base import BaseCommand, CommandError
import yelp
from location.models import City
from accommodation.models import Accommodation

YELP_KEYS ={
    'consumer_key': 'z6L-YNjSpzs6fbkVL1TjEQ',
    'consumer_secret': 'reGK0qmvKqrn5P2PSEIwxdyNUT0',
    'token': '1tAwl4Ypsg7iO_UBXwhMnnQ33eaRRSyE',
    'token_secret': 'QK_bVGJnl91CBxSfnSJoS9hhGoA',
}

yelp_api = yelp.Api(consumer_key=YELP_KEYS['consumer_key'],
                    consumer_secret=YELP_KEYS['consumer_secret'],
                    access_token_key=YELP_KEYS['token'],
                    access_token_secret=YELP_KEYS['token_secret'])

accommodation_choices =('hotel', 'hostel')

class Command(BaseCommand):
    help = 'Gets the hostel and hotel data for all cities in the database'

    def handle(self, *args, **options):
        cities = City.objects.all()
        for city in cities:
            for choice in accommodation_choices:
                search_results = yelp_api.Search(term=choice, location=city)

                for result in search_results:

