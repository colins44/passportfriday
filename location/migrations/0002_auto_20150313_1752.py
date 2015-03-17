# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=1, to='location.Country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(max_length=10, choices=[(b'pound', '\xa3'), (b'euro', '\u20ac')]),
            preserve_default=True,
        ),
    ]
