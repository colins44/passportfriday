# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_activity_placesofintrest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='iso_code',
        ),
        migrations.RemoveField(
            model_name='country',
            name='language',
        ),
        migrations.AddField(
            model_name='country',
            name='capital',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='currency',
            name='code',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='decimal_digits',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='currency',
            name='name_plural',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='rounding',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='currency',
            name='symbol_native',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
