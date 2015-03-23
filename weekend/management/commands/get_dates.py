from django.core.management.base import BaseCommand
from weekend.models import Dates
import calendar
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'makes the dates for all weekend in the next couple of years'

    def handle(self, *args, **options):
        years =[2015, 2016, 2017, 2018, 2019, 2020]
        for year in years:
            for month in range(1, 13):
                cal = calendar.monthcalendar(year, month)
                for week in cal:
                    friday = week[calendar.FRIDAY]
                    if friday != 0:
                        departure_date = datetime.strptime(('%d/%d/%d' % (friday, month, year)), '%d/%m/%Y')
                        return_date = departure_date + timedelta(days=2)
                        Dates.objects.get_or_create(departure_date=departure_date, return_date=return_date)