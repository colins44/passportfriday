from django.core.management.base import BaseCommand, CommandError
from location.models import Country, Currency, City
from flights.models import Airport
from location.countries import countries, country_codes
from location.currencies import currencies
from flights.airports import airports
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Import the cities, currencies and airports into the database'
    countries = countries['countries']

    def handle(self, *args, **options):

        for currency in currencies:
            Currency.objects.get_or_create(symbol = currencies.get(currency).get('symbol'),
                                           name = currencies.get(currency).get('name'),
                                           symbol_native= currencies.get(currency).get('symbol_native'),
                                           decimal_digits= currencies.get(currency).get('decimal_digits'),
                                           rounding = currencies.get(currency).get('rounding'),
                                           code = currencies.get(currency).get('code'),
                                           name_plural=currencies.get(currency).get('name_plural'))

        for country in countries.get('countries'):
            try:
                currency = Currency.objects.get(code = countries.get('countries').get(country).get('currency'))
            except ObjectDoesNotExist:
                currency = Currency.objects.get(code ="USD")
            Country.objects.get_or_create(currency=currency,
                                          name = countries.get('countries').get(country).get('name'),
                                          phone = countries.get('countries').get(country).get('phone'),
                                          continent = countries.get('countries').get(country).get('continent'),
                                          capital = countries.get('countries').get(country).get('capital'))

            for country in country_codes:
                try:
                    count = Country.objects.get(name=country.get('name'))
                except ObjectDoesNotExist:
                    continue
                else:
                    count.code = country.get('code')
                    count.save()

        for airport in airports:
            try:
                country = Country.objects.get(name = airports.get(airport).get('country'))
            except ObjectDoesNotExist:
                country = Country.objects.get(name = 'Zimbabwe')
            city = City.objects.get_or_create(country=country, name=airports.get(airport).get('city'))
            Airport.objects.get_or_create(name=airports.get(airport).get('name'),
                                          country=country,
                                          city=city[0],
                                          iata=airports.get(airport).get('iata'),
                                          icao=airports.get(airport).get('icao'),
                                          latitude=airports.get(airport).get('latitude'),
                                          longitude=airports.get(airport).get('longitude'),
                                          altitude=airports.get(airport).get('altitude'),
                                          timezone=airports.get(airport).get('timezone'))
