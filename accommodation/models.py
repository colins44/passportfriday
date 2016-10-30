from datetime import datetime

from django.db import models

from location.models import City, Currency

ACCOMMODATION_CHOICES = (('1', 'hotel'),
                         ('5', 'bed and breakfast'),)


class Accommodation(models.Model):
    city = models.ForeignKey(City)
    type = models.CharField(max_length=100, choices=ACCOMMODATION_CHOICES)
    name = models.CharField(max_length=150)
    address1 = models.CharField(max_length=150, blank=True, null=True)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    post_code = models.CharField(max_length=50, blank=True, null=True)
    rating = models.FloatField(default=3)
    high_rate = models.IntegerField(blank=False, null=True)
    low_rate = models.IntegerField(blank=True, null=True)
    ean_hotel_id = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return '%s in %s' % (self.name, self.city)


class RoomRate(models.Model):
    hotel = models.ForeignKey(Accommodation)
    max_occupancy = models.IntegerField(blank=True, null=True)
    quoted_occupancy = models.IntegerField(blank=True, null=True)
    room_description = models.CharField(max_length=150, blank=True, null=True)
    room_type_code = models.IntegerField(blank=True, null=True)
    rate_code = models.IntegerField(blank=True, null=True)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    no_of_adults = models.IntegerField(blank=True, null=True)
    no_of_children = models.IntegerField(blank=True, null=True)
    promotion = models.BooleanField(default=False)
    deeplink = models.URLField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    rate_type = models.CharField(max_length=150, blank=True, null=True)
    currency = models.ForeignKey(Currency)
    created = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.now()
        return super(RoomRate, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%d for %s' % (self.total, self.hotel.name)
