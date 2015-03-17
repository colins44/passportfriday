# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('weekend', '0002_weekend'),
    ]

    operations = [
        migrations.AddField(
            model_name='taggeditem',
            name='parent_content_type',
            field=models.ForeignKey(related_name='Flights', default=1, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taggeditem',
            name='parent_object_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
