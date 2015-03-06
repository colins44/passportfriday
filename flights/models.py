from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType


class Airport(models.Model):
    code = models.CharField(max_length=5, unique=True)

    def __unicode__(self):
        return self.code

class Flight(models.Model):
    departure_airport = models.ForeignKey(Airport, related_name='departure_airport')
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_airport')
    departure_time = models.DateTimeField(blank=True, null=True)
    flight_no = models.IntegerField(blank=True, null=True)
    carrier_code = models.CharField(max_length=5, blank=True, null=True)
    arrival_time = models.DateTimeField(blank=True, null=True)
    stops = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def get_outbound_flights(self):
        return Flight.objects.filter(departure_airport=self.departure_airport)

    def get_inbound_flights(self):
        return Flight.objects.filter(arrival_airport=self.arrival_airport)

    def __unicode__(self):
        return unicode(self.id)

    # class Meta:
    #     ordering = ['price']

class Route(models.Model):
    airport = models.ForeignKey(Airport) #airport to which the flight is going to
    outbound_flights = models.ManyToManyField(Flight, related_name='outbound flights')
    inbound_flights = models.ManyToManyField(Flight, related_name='inbound flights')

    def __unicode__(self):
        return unicode(self.id)




