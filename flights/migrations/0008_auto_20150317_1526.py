# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0007_auto_20150317_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='altitude',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
