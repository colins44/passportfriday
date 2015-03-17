# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrival_airport', models.ForeignKey(related_name='arrival_airport', to='flights.Airport')),
                ('departure_airport', models.ForeignKey(related_name='departure_airport', to='flights.Airport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('airport', models.ForeignKey(to='flights.Airport')),
                ('inbound_flights', models.ManyToManyField(related_name='inbound flights', to='flights.Flight')),
                ('outbound_flights', models.ManyToManyField(related_name='outbound flights', to='flights.Flight')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
