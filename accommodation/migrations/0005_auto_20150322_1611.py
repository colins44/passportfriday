# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20150317_1449'),
        ('accommodation', '0004_auto_20150322_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_occupancy', models.IntegerField(null=True, blank=True)),
                ('quoted_occupancy', models.IntegerField(null=True, blank=True)),
                ('room_description', models.CharField(max_length=150, null=True, blank=True)),
                ('room_type_code', models.IntegerField(null=True, blank=True)),
                ('rate_code', models.IntegerField(null=True, blank=True)),
                ('arrival_date', models.DateField()),
                ('departure_date', models.DateField()),
                ('no_of_adults', models.IntegerField(null=True, blank=True)),
                ('no_of_children', models.IntegerField(null=True, blank=True)),
                ('promotion', models.BooleanField(default=False)),
                ('deeplink', models.URLField(null=True, blank=True)),
                ('total', models.FloatField(null=True, blank=True)),
                ('rate_type', models.CharField(max_length=150, null=True, blank=True)),
                ('currency', models.ForeignKey(to='location.Currency')),
                ('hotel', models.ForeignKey(to='accommodation.Accommodation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='rates',
            name='accommodation',
        ),
        migrations.DeleteModel(
            name='Rates',
        ),
        migrations.AddField(
            model_name='accommodation',
            name='high_rate',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accommodation',
            name='low_rate',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
