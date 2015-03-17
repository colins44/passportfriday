from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class WeekendItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent_object_id = models.IntegerField(blank=True, null=True)
    parent_content_type = models.ForeignKey(ContentType, related_name='Flights')

    def __unicode__(self):
        return self.tag


class Weekend(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    items = generic.GenericRelation(WeekendItem,
                                              content_type_field='content_type',
                                              object_id_field='object_id',
                                              blank=True,
                                              null=True)

    def __unicode__(self):
        return self.name
