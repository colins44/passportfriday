from django.core.management.base import BaseCommand
import yelp
from location.models import Categories, Activities


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
    help = 'Get the top things that yelp suggest doing in a city then try look them up in the api'

    def handle(self, *args, **options):
        search_results = yelp_api.Search(term='things to do', location='london')
        for result in search_results.businesses:
            categories =  [item for sublist in result.categories for item in sublist]
            categories = [item.lower() for item in categories]
            categories = set(categories)
            base_queryset = Categories.objects.none()

            for cat in categories:
                cats, created =Categories.objects.get_or_create(name=cat)
                base_queryset= base_queryset|cats

            Activities.objects.get_or_create(city= city, name=result.name)




