from django.db import models
from location.models import City, Country, Currency
from weekend.models import Dates


class Airport(models.Model):
    name = models.CharField(blank=True, null=True, max_length=75)
    city = models.ForeignKey(City)
    country = models.ForeignKey(Country)
    iata = models.CharField(blank=True, null=True, max_length=10)
    icao = models.CharField(blank=True, null=True, max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    altitude = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    timezone = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __unicode__(self):
        return '%s' % self.name

class Flight(models.Model):
    departure_airport = models.ForeignKey(Airport, related_name='departure_airport')
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_airport')
    departure_time = models.DateTimeField(blank=True, null=True)
    flight_no = models.IntegerField(blank=True, null=True)
    carrier_code = models.CharField(max_length=5, blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    stops = models.IntegerField(blank=True, null=True, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def get_outbound_flights(self):
        return Flight.objects.filter(departure_airport=self.departure_airport)

    def get_inbound_flights(self):
        return Flight.objects.filter(arrival_airport=self.arrival_airport)

    def __unicode__(self):
        return '%s %s' % (self.carrier_code, self.flight_no)


class Route(models.Model):
    origin = models.ForeignKey(City, related_name='origin')
    destination = models.ForeignKey(City, related_name='destination')
    departure_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    outbound_flights = models.ManyToManyField(Flight, related_name='outbound flights')
    inbound_flights = models.ManyToManyField(Flight, related_name='inbound flights')

    def __unicode__(self):
        return unicode(self.id)

class Slice(models.Model):
    dates = models.ForeignKey(Dates)
    origin = models.ForeignKey(City, related_name='origin city')
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey(Currency)
    destination = models.ForeignKey(City, related_name='destination city')
    outbound_flight = models.ForeignKey(Flight, related_name='departing flight')
    inbound_flight = models.ForeignKey(Flight, related_name='return flight')

    class Meta:
        ordering = ['price']

    def __unicode__(self):
        return self.origin.name

# class Destinations(models.Model):
#     origin = models.ForeignKey(City, related_name='origin')
#     dates = models.ForeignKey(Dates)
#     destinations = models.ManyToManyField(City, related_name='destinations')
#
#     def __unicode__(self):
#         return self.origin.name




