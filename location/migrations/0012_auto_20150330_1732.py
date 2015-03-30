# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0011_auto_20150326_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cityinfo',
            name='city',
        ),
        migrations.RemoveField(
            model_name='cityinfo',
            name='sections',
        ),
        migrations.DeleteModel(
            name='CityInfo',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='city',
        ),
        migrations.RemoveField(
            model_name='section',
            name='city',
        ),
        migrations.RemoveField(
            model_name='section',
            name='listings',
        ),
        migrations.DeleteModel(
            name='Listing',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
