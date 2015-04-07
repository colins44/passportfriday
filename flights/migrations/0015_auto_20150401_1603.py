# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0013_auto_20150330_2034'),
        ('flights', '0014_auto_20150317_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='destination',
            field=models.ForeignKey(related_name='destination', default=1, to='location.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='origin',
            field=models.ForeignKey(related_name='origin', default=1, to='location.City'),
            preserve_default=False,
        ),
    ]
