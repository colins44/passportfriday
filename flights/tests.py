"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from weekend.models import Dates
from flights.models import Flight, Airport
from location.models import City, Country, Currency


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class TaskTests(TestCase):

    def setUp(self):
        '''sets up the following models
        two currencies: the pound and euro,
        three countries UK, Germany and France,
        Three french cities and three german cities as well as london,
        One airport for every city,
        Weekend dates for a weekend in the future,
        Flights for that weekend'''
        self.pound = Currency.objects.create(
            name='pound',
            symbol='£',
            symbol_native='£',
            code = 'GBP',
            name_plural = 'British pounds sterling',

        )
        self.euro = Currency.objects.create(
            name='pound',
            symbol='£',
            symbol_native='£',
            code = 'GBP',
            name_plural = 'British pounds sterling',

        )
        self.uk = Country.objects.create(
            name='United Kingdom',
            phone=44,
            continent='EU',
            capital='London',
            currency=self.pound,
            code='GB',

        )
        self.france = Country.objects.create(
            name='France',
            phone=31,
            continent='EU',
            capital='Paris',
            currency=self.euro,
            code='FR',

        )
        self.germany = Country.objects.create(
            name='Germany',
            phone=32,
            continent='EU',
            capital='Berlin',
            currency=self.euro,
            code='DE',

        )
        self.London = City.objects.create(
            name='London',
            country=self.uk,
            code='LON',
        )
        self.Berlin = City.objects.create(
            name='Berlin',
            country=self.germany,
            code='BER',
        )
        self.Munich = City.objects.create(
            name='Munich',
            country=self.germany,
            code='MUC',
        )
        self.Frankfurt = City.objects.create(
            name='Frankfurt',
            country=self.germany,
            code='FRA',
        )
        self.Paris = City.objects.create(
            name='Paris',
            country=self.france,
            code='PAR',
        )
        self.Nice = City.objects.create(
            name='Nice',
            country=self.france,
            code='NCE',
        )
        self.Toulouse = City.objects.create(
            name='Toulouse',
            country=self.france,
            code='TLS',
        )
        self.Frankfurt_Airport = Airport.objects.create(
            name = 'Frankfurt Airport',
            city = self.Frankfurt,
            country= self.germany,
            iata='FRA',
            icao='EDDF',
            latitude = 0,
            longitude = 0,
            altitude = 0,
            timezone =1
        )
        self.Munich_Airport = Airport.objects.create(
            name = 'Munich Airport',
            city = self.Munich,
            country= self.germany,
            iata='MUQ',
            icao='asd',
            latitude = 0,
            longitude = 0,
            altitude = 0,
            timezone =1
        )
        self.Berlin_Airport = Airport.objects.create(
            name = 'Berlin Airport',
            city = self.Berlin,
            country= self.germany,
            iata='BER',
            icao='asd',
            latitude = 0,
            longitude = 0,
            altitude = 0,
            timezone =1
        )
        self.Nice_Airport = Airport.objects.create(
            name = 'Nice Airport',
            city = self.Nice,
            country= self.france,
            iata='NCE',
            icao='nce',
            latitude = 0,
            longitude = 0,
            altitude = 0,
            timezone =1
        )
        self.Toulouse_Airport = Airport.objects.create(
            name = 'Toulouse Airport',
            city = self.Toulouse,
            country= self.france,
            iata='TOU',
            icao='TOU',
            latitude = 0,
            longitude = 0,
            altitude = 0,
            timezone =1
        )
        self.Paris_Airport = Airport.objects.create(
            name = 'Paris Airport',
            city = self.Paris,
            country= self.france,
            iata='PAR',
            icao='PAR',
            latitude = 0,
            longitude = 0,
            altitude = 0,
            timezone =1
        )
        self.London_Airport = Airport.objects.create(
            name = 'Paris Airport',
            city = self.London,
            country= self.uk,
            iata='LON',
            icao='LON',
            latitude = 0,
            longitude = 0,
            altitude = 0,
            timezone =1
        )




