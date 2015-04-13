# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from weekend.models import Dates
from flights.models import Flight, Airport, Destinations
from location.models import City, Country, Currency
from datetime import timedelta, date


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
            name='euro',
            symbol='€',
            symbol_native='€',
            code = 'EUR',
            name_plural = 'euros',

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
            latitude=0,
            longitude=0,
            altitude=0,
            timezone=1
        )
        self.Munich_Airport = Airport.objects.create(
            name='Munich Airport',
            city =self.Munich,
            country=self.germany,
            iata='MUQ',
            icao='asd',
            latitude =0,
            longitude=0,
            altitude=0,
            timezone=1
        )
        self.Berlin_Airport = Airport.objects.create(
            name='Berlin Airport',
            city=self.Berlin,
            country=self.germany,
            iata='BER',
            icao='asd',
            latitude=0,
            longitude=0,
            altitude=0,
            timezone=1
        )
        self.Nice_Airport = Airport.objects.create(
            name='Nice Airport',
            city=self.Nice,
            country=self.france,
            iata='NCE',
            icao='nce',
            latitude=0,
            longitude=0,
            altitude=0,
            timezone=1
        )
        self.Toulouse_Airport = Airport.objects.create(
            name = 'Toulouse Airport',
            city = self.Toulouse,
            country= self.france,
            iata='TOU',
            icao='TOU',
            latitude=0,
            longitude=0,
            altitude=0,
            timezone=1
        )
        self.Paris_Airport = Airport.objects.create(
            name = 'Paris Airport',
            city = self.Paris,
            country= self.france,
            iata='PAR',
            icao='PAR',
            latitude=0,
            longitude=0,
            altitude=0,
            timezone=1
        )
        self.London_Airport = Airport.objects.create(
            name='Paris Airport',
            city=self.London,
            country= self.uk,
            iata='LON',
            icao='LON',
            latitude=0,
            longitude=0,
            altitude=0,
            timezone=1
        )
        today = date.today()
        next_friday = (today + timedelta( (4-today.weekday()) % 7))+timedelta(days=7)
        next_sunday = (today + timedelta( (6-today.weekday()) % 7))+timedelta(days=7)
        self.weekend = Dates.objects.create(departure_date=next_friday,
                                            return_date=next_sunday)
        self.outbound_flight1 = Flight.objects.create(departure_airport=self.London_Airport,
                                             arrival_airport=self.Frankfurt_Airport,
                                             departure_time=self.weekend.departure_date,
                                             flight_no=1,
                                             carrier_code='BA')
        self.outbound_flight2 = Flight.objects.create(departure_airport=self.London_Airport,
                                             arrival_airport=self.Munich_Airport,
                                             departure_time=self.weekend.departure_date,
                                             flight_no=2,
                                             carrier_code='BA')
        self.outbound_flight3 = Flight.objects.create(departure_airport=self.London_Airport,
                                             arrival_airport=self.Berlin_Airport,
                                             departure_time=self.weekend.departure_date,
                                             flight_no=3,
                                             carrier_code='BA')
        self.outbound_flight4 = Flight.objects.create(departure_airport=self.London_Airport,
                                             arrival_airport=self.Paris_Airport,
                                             departure_time=self.weekend.departure_date,
                                             flight_no=4,
                                             carrier_code='BA')
        self.outbound_flight5 = Flight.objects.create(departure_airport=self.London_Airport,
                                             arrival_airport=self.Toulouse_Airport,
                                             departure_time=self.weekend.departure_date,
                                             flight_no=5,
                                             carrier_code='BA')
        self.outbound_flight6 = Flight.objects.create(departure_airport=self.London_Airport,
                                             arrival_airport=self.Nice_Airport,
                                             departure_time=self.weekend.departure_date,
                                             flight_no=6,
                                             carrier_code='BA')
        self.inbound_flight1 = Flight.objects.create(departure_airport=self.Frankfurt_Airport,
                                             arrival_airport=self.London_Airport,
                                             departure_time=self.weekend.return_date,
                                             flight_no=7,
                                             carrier_code='BA')
        self.inbound_flight2 = Flight.objects.create(departure_airport=self.Munich_Airport,
                                             arrival_airport=self.London_Airport,
                                             departure_time=self.weekend.return_date,
                                             flight_no=8,
                                             carrier_code='BA')
        self.inbound_flight3 = Flight.objects.create(departure_airport=self.Berlin_Airport,
                                             arrival_airport=self.London_Airport,
                                             departure_time=self.weekend.return_date,
                                             flight_no=9,
                                             carrier_code='BA')
        self.inbound_flight4 = Flight.objects.create(departure_airport=self.Paris_Airport,
                                             arrival_airport=self.London_Airport,
                                             departure_time=self.weekend.return_date,
                                             flight_no=10,
                                             carrier_code='BA')
        self.inbound_flight5 = Flight.objects.create(departure_airport=self.Nice_Airport,
                                             arrival_airport=self.London_Airport,
                                             departure_time=self.weekend.return_date,
                                             flight_no=11,
                                             carrier_code='BA')
        self.inbound_flight6 = Flight.objects.create(departure_airport=self.Toulouse_Airport,
                                             arrival_airport=self.London_Airport,
                                             departure_time=self.weekend.return_date,
                                             flight_no=12,
                                             carrier_code='BA')

    def test_data(self):
        self.assertEqual(Airport.objects.all().count(), 7)
        self.assertEqual(Flight.objects.all().count(), 12)
        self.assertEqual(Currency.objects.all().count(), 2)
        self.assertEqual(Country.objects.all().count(), 3)
        self.assertEqual(City.objects.all().count(), 7)

    def test_city_destinations(self):
        city, cities, dates = self.London.destinations(self.weekend)
        self.assertEqual(city, self.London)
        self.assertEqual(dates, self.weekend)
        destinations = Destinations.objects.get(origin=self.London, dates=self.weekend)
        self.assertEqual(destinations.dates, self.weekend)
        self.assertEqual(destinations.origin, self.London)
        #Currently there are 7 cities including London








