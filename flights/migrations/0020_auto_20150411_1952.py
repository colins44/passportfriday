# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0019_auto_20150409_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='route',
            name='inbound_flights',
        ),
        migrations.RemoveField(
            model_name='route',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='route',
            name='outbound_flights',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]
