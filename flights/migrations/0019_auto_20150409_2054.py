# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weekend', '0006_dates'),
        ('location', '0014_city_code'),
        ('flights', '0018_auto_20150401_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('currency', models.ForeignKey(to='location.Currency')),
                ('dates', models.ForeignKey(to='weekend.Dates')),
                ('destination', models.ForeignKey(related_name='destination city', to='location.City')),
                ('inbound_flight', models.ForeignKey(related_name='return flight', to='flights.Flight')),
                ('origin', models.ForeignKey(related_name='origin city', to='location.City')),
                ('outbound_flight', models.ForeignKey(related_name='departing flight', to='flights.Flight')),
            ],
            options={
                'ordering': ['price'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='flight',
            name='stops',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
