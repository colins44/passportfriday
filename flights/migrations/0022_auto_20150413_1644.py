# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0021_destinations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinations',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='destinations',
            name='destinations',
        ),
        migrations.RemoveField(
            model_name='destinations',
            name='origin',
        ),
        migrations.DeleteModel(
            name='Destinations',
        ),
    ]
