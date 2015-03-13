# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20150313_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, choices=[(b'hotel', b'hotel'), (b'hostel', b'hostel'), (b'air b and b', b'airb&b'), (b'private', b'private'), (b'bed and breakfast', b'B&B')])),
                ('city', models.ForeignKey(to='location.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
