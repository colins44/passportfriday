# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0010_auto_20150317_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='timezone',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=6),
            preserve_default=True,
        ),
    ]
