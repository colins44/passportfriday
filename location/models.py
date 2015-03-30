# -*- coding: utf-8 -*-
from django.db import models

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

    def __unicode__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150, unique=True)

    def __unicode__(self):
        return self.name

class Activities(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150)
    city = models.ForeignKey(City)
    catergories = models.ManyToManyField(Categories)
    text = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name




