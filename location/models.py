# -*- coding: utf-8 -*-
from django.db import models
from weekend.models import Dates


CATEGORIES =(
    ('Do', 'Do'),
    ('See', 'See'),
    ('Get around', 'Get around'),
)

class Currency(models.Model):
    name = models.CharField(max_length=60)
    symbol = models.CharField(max_length=10)
    symbol_native = models.CharField(max_length=10)
    decimal_digits = models.IntegerField(default=2)
    code = models.CharField(max_length=5)
    rounding =  models.IntegerField(default=0)
    name_plural = models.CharField(max_length=75)

    def __unicode__(self):
        return self.name



class Country(models.Model):
    name = models.CharField(max_length=60)
    phone = models.IntegerField(default=0)
    continent = models.CharField(max_length=10)
    capital = models.CharField(max_length=50)
    currency = models.ForeignKey(Currency)
    code = models.CharField(blank=True, max_length=4)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=75)
    country = models.ForeignKey(Country)
    code = models.CharField(max_length=5, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def possible_destinations(self, dates):
        from flights.models import Flight
        '''pass a dates object to this function and it will return a list of cities you will be able
            to fly to for the week in question'''
        outbound_flights = Flight.objects.filter(departure_airport__city=self,
                                                 departure_time__year=dates.departure_date.year,
                                                 departure_time__month=dates.departure_date.month,
                                                 departure_time__day=dates.departure_date.day,
                                                 ).exclude(arrival_airport__country=self.country)
        inbound_flights = Flight.objects.filter(arrival_airport__city=self,
                                                departure_time__year=dates.return_date.year,
                                                departure_time__month=dates.return_date.month,
                                                departure_time__day=dates.return_date.day,
                                                ).exclude(departure_airport__country=self.country)
        #make two lists of all the cities
        outbound_cities = []
        inbound_cites = []
        for flight in outbound_flights:
            outbound_cities.append(flight.arrival_airport.city)
        for flight in inbound_flights:
            inbound_cites.append(flight.departure_airport.city)

        # compare the lists and get the cites that match
        cites = set(outbound_cities).intersection(inbound_cites)
        destinations, created = Destinations.objects.get_or_create(origin=self,
                                                                   dates=dates)
        destinations.destinations = cites
        destinations.save()
        return self, cites, dates

class Destinations(models.Model):
    '''There is probs a better model name for this'''
    origin = models.ForeignKey(City, related_name='origin')
    dates = models.ForeignKey(Dates)
    destinations = models.ManyToManyField(City, related_name='destinations')

    def __unicode__(self):
        return self.origin.name

    class Meta:
        ordering = ('dates',)


class Category(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150, unique=True)

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150)
    city = models.ForeignKey(City)
    catergories = models.ManyToManyField(Category)
    text = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name




