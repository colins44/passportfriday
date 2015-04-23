# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0015_destinations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destinations',
            options={'ordering': ('dates',)},
        ),
    ]
