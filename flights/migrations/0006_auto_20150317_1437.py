# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20150317_1437'),
        ('flights', '0005_auto_20150301_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='code',
        ),
        migrations.AddField(
            model_name='airport',
            name='altitude',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(default=1, to='location.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(default=1, to='location.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='iata',
            field=models.CharField(max_length=10, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='airport',
            name='icao',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='airport',
            name='latitude',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='longitude',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='name',
            field=models.CharField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='airport',
            name='timezone',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
