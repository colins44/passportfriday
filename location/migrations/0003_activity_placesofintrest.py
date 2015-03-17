# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20150313_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100, choices=[(b'statue', b'statue'), (b'museaum', b'museaum'), (b'building', b'building')])),
                ('city', models.ForeignKey(to='location.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlacesOfIntrest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100, choices=[(b'statue', b'statue'), (b'museaum', b'museaum'), (b'building', b'building')])),
                ('city', models.ForeignKey(to='location.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
