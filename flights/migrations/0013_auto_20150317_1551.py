# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0012_auto_20150317_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='timezone',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
    ]
