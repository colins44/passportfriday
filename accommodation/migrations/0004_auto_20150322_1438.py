# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0003_auto_20150317_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrival_date', models.DateField()),
                ('departure_date', models.DateField()),
                ('accommodation', models.ForeignKey(to='accommodation.Accommodation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='address1',
            field=models.CharField(default=1, max_length=150, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accommodation',
            name='address2',
            field=models.CharField(default=1, max_length=150, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accommodation',
            name='ean_hotel_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accommodation',
            name='post_code',
            field=models.CharField(default=1, max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accommodation',
            name='rating',
            field=models.FloatField(default=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='type',
            field=models.CharField(max_length=100, choices=[(b'1', b'hotel'), (b'5', b'bed and breakfast')]),
            preserve_default=True,
        ),
    ]
