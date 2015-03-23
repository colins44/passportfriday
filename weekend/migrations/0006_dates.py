# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weekend', '0005_weekend_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departure_date', models.DateField()),
                ('return_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
