# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weekend', '0006_dates'),
        ('location', '0015_destinations'),
        ('flights', '0023_remove_flight_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricSlice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('quote_time', models.DateTimeField(default=datetime.datetime(2015, 4, 16, 8, 20, 49, 785415, tzinfo=utc))),
                ('currency', models.ForeignKey(to='location.Currency')),
                ('dates', models.ForeignKey(to='weekend.Dates')),
                ('destination', models.ForeignKey(related_name='historic destination city', to='location.City')),
                ('inbound_flight', models.ForeignKey(related_name='historic return flight', to='flights.Flight')),
                ('origin', models.ForeignKey(related_name='historic origin city', to='location.City')),
                ('outbound_flight', models.ForeignKey(related_name='historic departing flight', to='flights.Flight')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slice',
            name='quote_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 8, 20, 49, 784650, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
