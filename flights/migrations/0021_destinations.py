# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weekend', '0006_dates'),
        ('location', '0014_city_code'),
        ('flights', '0020_auto_20150411_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dates', models.ForeignKey(to='weekend.Dates')),
                ('destinations', models.ManyToManyField(related_name='destinations', to='location.City')),
                ('origin', models.ForeignKey(related_name='origin', to='location.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
