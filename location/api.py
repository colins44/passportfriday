# -*- coding: utf-8 -*-
from location.models import City, Currency, Country
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

class CityResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'pk',
        'name': 'name',
    })

    def list(self):
        return City.objects.all()

    def detail(self, pk):
        return City.objects.get(id=pk)


class CountryResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'pk',
        'name': 'name',
        'phone': 'phone',
        'continent': 'continent',
        'capital': 'capital',
    })

    def list(self):
        return Country.objects.all()

    def detail(self, pk):
        return Country.objects.get(id=pk)

class CurrencyResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'pk',
        'name': 'name',
        'symbol': 'symbol',
        'symbol_native': 'symbol_native',
        'code': 'code',
        'rounding': 'rounding',
        'name_plural': 'name_plural',

    })

    def list(self):
        return Currency.objects.all()

    def detail(self, pk):
        return Currency.objects.get(id=pk)