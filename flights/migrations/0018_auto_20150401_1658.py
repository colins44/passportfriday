# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0017_auto_20150401_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='departure_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='route',
            name='return_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
