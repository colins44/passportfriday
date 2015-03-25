#http://www.wikisherpa.com/api/1/page/en/Madrid
#http://wikitravel.org/wiki/en/api.php?format=xml&action=query&titles=Berlin&prop=revisions&rvprop=content

from django.core.management.base import BaseCommand
from location.models import Country
import requests

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        countries = Country.objects.filter(continent='EU')[:1]
        for country in countries:
            url = "http://www.wikisherpa.com/api/1/page/en/%s" % country.capital
            r = requests.get(url)
            print r.status_code
            print r.url
