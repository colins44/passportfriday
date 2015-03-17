# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20150317_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name_plural',
            field=models.CharField(max_length=75),
            preserve_default=True,
        ),
    ]
