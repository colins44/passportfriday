# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0006_auto_20150322_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomrate',
            name='created',
            field=models.DateTimeField(null=True, editable=False),
            preserve_default=True,
        ),
    ]
