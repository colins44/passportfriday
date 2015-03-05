# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_flight_price'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='flight',
        #     name='price',
        # ),
        # migrations.AddField(
        #     model_name='route',
        #     name='price',
        #     field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        #     preserve_default=True,
        # ),
    ]
