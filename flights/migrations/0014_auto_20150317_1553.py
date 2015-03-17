# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0013_auto_20150317_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='altitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='airport',
            name='timezone',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]
