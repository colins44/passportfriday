# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0015_auto_20150401_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='airport',
        ),
        migrations.AddField(
            model_name='route',
            name='destination_airport',
            field=models.ForeignKey(related_name='destination airport', default=1, to='flights.Airport'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='origin_airport',
            field=models.ForeignKey(related_name='origin airport', default=1, to='flights.Airport'),
            preserve_default=False,
        ),
    ]
