# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0002_accommodation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='type',
            field=models.CharField(max_length=100, choices=[(b'hotel', b'hotel'), (b'hostel', b'hostel')]),
            preserve_default=True,
        ),
    ]
