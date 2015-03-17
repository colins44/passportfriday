# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_auto_20150317_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='altitude',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=6, blank=True),
            preserve_default=True,
        ),
    ]
