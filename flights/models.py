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

    def get_outbound_flights(self):
        return Flight.objects.filter(departure_airport=self.departure_airport)

    def get_inbound_flights(self):
        return Flight.objects.filter(arrival_airport=self.arrival_airport)

    def __unicode__(self):
        return unicode(self.id)
        return "%s to %s" % (self.departure_airport, self.arrival_airport)

class Route(models.Model):
    airport = models.ForeignKey(Airport)
    outbound_flights = models.ManyToManyField(Flight, related_name='outbound flights')
    inbound_flights = models.ManyToManyField(Flight, related_name='inbound flights')

    def __unicode__(self):
        return unicode(self.id)

flights = models.Q(app_label = 'flights', model = 'Flight')

class OutboundFlights(models.Model):
    """
    Relates any one entry to another entry irrespective of their individual models.
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=225, blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    parent_content_type = models.ForeignKey(ContentType, related_name="outbound flights")
    parent_object_id = models.CharField(max_length=225, blank=True, null=True)
    parent_content_object = generic.GenericForeignKey('parent_content_type', 'parent_object_id')

    class Meta:
        verbose_name = 'Outbound Flight'
        verbose_name_plural = 'Outbound Flights'


    def __unicode__(self):
        return "%s: %s" % (self.content_type.name, self.content_object)


class InboundFlights(models.Model):
    """
    Relates any one entry to another entry irrespective of their individual models.
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=225, blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    parent_content_type = models.ForeignKey(ContentType, related_name="inbound flights")
    parent_object_id = models.CharField(max_length=225, blank=True, null=True)
    parent_content_object = generic.GenericForeignKey('parent_content_type', 'parent_object_id')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Inbound Flight'
        verbose_name_plural = 'Inbound Flights'



    def __unicode__(self):
        return "%s: %s" % (self.content_type.name, self.content_object)

class RoundTrip(models.Model):
    name = models.CharField(max_length=255)
    outbound_flights = generic.GenericRelation(OutboundFlights,
                                              content_type_field='content_type',
                                              object_id_field='object_id',
                                              blank=True,
                                              null=True)

    inbound_flights = generic.GenericRelation(InboundFlights,
                                              content_type_field='content_type',
                                              object_id_field='object_id',
                                              blank=True,
                                              null=True)


    def __unicode__(self):
        return u'%s' % self.name
