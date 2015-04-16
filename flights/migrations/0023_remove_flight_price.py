# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0022_auto_20150413_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='price',
        ),
    ]
