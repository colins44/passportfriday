# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20150209_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
