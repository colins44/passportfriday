from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import requests


class Command(BaseCommand):
    help = 'Get all the flights for the weekend from the flightstats api, then save the flight before making the route'
    url = "https://api.flightstats.com/flex/schedules/rest/v1/json/from/%s/departing/%s/%s/%s/%s?appId=%s&appKey=%s" % (airport, year, month, day, hour, settings.FLIGHTSTATS_APPID, settings.FLIGHTSTATS_APPKEY)



