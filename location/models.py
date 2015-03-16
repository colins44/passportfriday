# -*- coding: utf-8 -*-
from django.db import models


SYMBOL = (('pound', u"£"),
          ('euro', u'€'),)

class Currency(models.Model):
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=10, choices=SYMBOL)

    def __unicode__(self):
        return self.name


LANGUAGES = (('EN', 'english'),)

class Country(models.Model):
    name = models.CharField(max_length=60)
    iso_code = models.CharField(max_length=3)
    language = models.CharField(max_length=25, choices=LANGUAGES)
    currency = models.ForeignKey(Currency)

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

