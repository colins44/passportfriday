import requests
import json
from django.core.management.base import BaseCommand
from location.models import Country, City, CityInfo, Listing, Section


class Command(BaseCommand):
    help = 'Gets data from the wikisherpa api for cities and saves to the database'

    def handle(self, *args, **options):
        city = City.objects.get(name='Madrid')
        url = "http://www.wikisherpa.com/api/1/page/en/%s" % city.name
        print url
        r = requests.get(url)
        page = json.loads(r.content)
        sections = page['sections']
        for section in sections:
            if section['name'] == 'Get Around':
                get_around = section
            if section['name'] == 'Do':
                do = section
            if section['name'] == 'See':
                see = section



        cityinfo, created = CityInfo.objects.get_or_create(city=city, category=see.get('name'))
        cityinfo.text = see.get('text')
        cityinfo.save()

        for obj in see.get('sections'):
            section, created, Section.objects.get_or_create(city=city, category=see.get('name'), name=obj['name'])
            if obj.get('text'):
                section.text = obj.get('text')
                section.save()

            if obj.get('listings'):
                for listing in obj.get('listings'):
                    list, created = Listing.objects.get_or_create(city=city, category=see.get('name'), name=listing['name'])
                    list.url = listing.get('url')
                    list.directions = listing.get('directions')
                    list.description = listing.get('description')
                    list.save()






