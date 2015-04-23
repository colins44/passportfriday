# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0024_auto_20150416_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='arrival_date',
        ),
        migrations.AlterField(
            model_name='historicslice',
            name='quote_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 7, 59, 10, 884749, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slice',
            name='quote_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 7, 59, 10, 883982, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
