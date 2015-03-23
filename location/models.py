# -*- coding: utf-8 -*-
from django.db import models


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

    def __unicode__(self):
        return self.name

PLACESOFINTEREST = (('statue','statue'),
                    ('museaum', 'museaum'),
                    ('building', 'building'),)

class PlacesOfIntrest(models.Model):
    '''A place of interest is a significant site and has no schedule attached to it eg, Museaums, Tate Gallery, Architecture'''
    city = models.ForeignKey(City)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=PLACESOFINTEREST)

    def __unicode__(self):
        return self.name

ACTIVITIES = (('tour', 'tour'),
              ('class', 'class'),
              ('show', 'show'),)

class Activity(models.Model):
    '''these denote a activity such as a tour, show, class and may have aschedule'''
    city = models.ForeignKey(City)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=PLACESOFINTEREST)

