# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from weekend.models import Dates
from flights.models import Flight, Airport, Slice, HistoricSlice
from location.models import City, Destinations
from datetime import timedelta, datetime
from flights.utils import process_qpx, flight_price_lookup_logic, get_flight_data
from flights.tasks import get_dates
from flights.qpx import flight_data, trip_dates, no_data
from django.utils import timezone
import json


class FixturesTest(TestCase):

    fixtures = ['flights/fixtures/dates.yaml','flights/fixtures/location.yaml', 'flights/fixtures/flights.yaml', ]
    #http://django-testing-docs.readthedocs.org/en/latest/fixtures.html

    def setUp(self):
        dates = timezone.now()+timedelta(days=30)
        self.weekend = Dates.objects.filter(departure_date__gte=dates)[0]
        self.London_Airport = Airport.objects.get(iata='LHR')
        self.Berlin_Airport = Airport.objects.get(iata='TXL')
        self.Paris_Airport = Airport.objects.get(iata='ORY')
        self.Nice_Airport = Airport.objects.get(iata='NCE')
        self.Barc_Airport = Airport.objects.get(iata='BCN')
        self.Munich_Airport = Airport.objects.get(iata='MUC')
        self.Frankfurt_Airport = Airport.objects.get(iata='FRA')
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
                                             arrival_airport=self.Barc_Airport,
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

    def test_get_cities(self):
        london = City.objects.get(name='London', country__name='United Kingdom')
        results = london.possible_destinations(self.weekend)
        self.assertEqual(results[0], london)
        self.assertEqual(results[2], self.weekend)
        self.assertEqual(len(results[1]), 5)
        dest = Destinations.objects.get(origin=results[0], dates=results[2])
        self.assertEqual(len(dest.destinations.all()), 5)


    def test_process_qpx(self):
        #got to figure our how to load initial data
        departure_date = datetime.strptime(trip_dates.get('departure_date'), '%Y-%m-%d')
        dates = Dates.objects.get(departure_date=departure_date)
        self.assertEqual(Slice.objects.count(), 0)
        self.assertEqual(HistoricSlice.objects.count(), 0)
        process_qpx(flight_data, dates)
        self.assertEqual(Slice.objects.count(), 20)
        self.assertEqual(HistoricSlice.objects.count(), 0)
        process_qpx(flight_data, dates)
        self.assertEqual(Slice.objects.count(), 20)
        self.assertEqual(HistoricSlice.objects.count(), 20)
        self.assertEqual(Slice.objects.count(), HistoricSlice.objects.count())

    def test_process_qpx_no_data(self):
        departure_date = datetime.strptime(trip_dates.get('departure_date'), '%Y-%m-%d')
        dates = Dates.objects.get(departure_date=departure_date)
        process_qpx(no_data, dates)
        self.assertEqual(Slice.objects.count(), HistoricSlice.objects.count())

    def test_api_qpx_post(self):
        payload ={
            'dates': {'departure_date': trip_dates.get('departure_date'), 'return_date': trip_dates.get('return_date')},
            'qpx_data':flight_data
        }
        r = self.client.post('/api/qpx/',
                             content_type='application/json',
                             data=json.dumps(payload))
        self.assertEqual(r.status_code, 201)
        self.assertEqual(Slice.objects.count(), 20)
        self.assertEqual(HistoricSlice.objects.count(), 0)

    def test_flight_price_lookup_logic(self):
        results = flight_price_lookup_logic()
        self.assertEqual(results, 1)

    def test_get_flight_data(self):
        #going to get flights from Glasgow between 9 and 11
        dates = get_dates(120)
        hours = [9,10]
        airport = Airport.objects.get(iata='GLA')
        for hour in hours:
            get_flight_data(airport.iata, dates, hour)
        outbound_flights = Flight.objects.filter(departure_airport=airport, departure_date=dates.departure_date)
        inbound_flights = Flight.objects.filter(arrival_airport=airport, departure_date=dates.return_date)
        outbound_flight = outbound_flights[0]
        inbound_flight = inbound_flights[0]
        self.assertEqual(outbound_flight.departure_airport, airport)
        self.assertEqual(outbound_flight.departure_time.date(), dates.departure_date)
        self.assertEqual(inbound_flight.departure_airport, airport)
        self.assertEqual(inbound_flight.departure_time.date(), dates.return_date)

















