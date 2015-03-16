from django.db import models
from location.models import City

ACCOMMODATION_CHOICES =(('hotel', 'hotel'),
                        ('hostel', 'hostel'))

class Accommodation(models.Model):
    city = models.ForeignKey(City)
    type = models.CharField(max_length=100, choices=ACCOMMODATION_CHOICES)
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return '%s %s in %s' % (self.name, self.type, self.city)
