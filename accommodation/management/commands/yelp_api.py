from django.core.management.base import BaseCommand
import yelp
import wikipedia
from location.models import Category, Activity, Country, City
from time import sleep


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
        for country in Country.objects.filter(name='Germany')[:1]:
            print country.capital
            search_results = yelp_api.Search(term='Landmarks & Historic Buildings', location=country.capital)
            for result in search_results.businesses:
                categories = [item for sublist in result.categories for item in sublist]
                categories = [item.lower() for item in categories]
                categories = set(categories)
                base_queryset = Category.objects.none()

                for cat in categories:
                    Category.objects.get_or_create(name=cat)
                    cats = Category.objects.filter(name=cat)
                    base_queryset = base_queryset | cats

                city = City.objects.get(name=country.capital)
                activity, created = Activity.objects.get_or_create(city=city, name=result.name)
                activity.category = base_queryset
                try:
                    activity.text = wikipedia.summary(activity.name)
                except:
                    pass
                activity.save()
                sleep(3)






