# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0016_auto_20150401_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='destination_airport',
        ),
        migrations.RemoveField(
            model_name='route',
            name='origin_airport',
        ),
    ]
