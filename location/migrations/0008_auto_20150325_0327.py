# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_country_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='city',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.RemoveField(
            model_name='placesofintrest',
            name='city',
        ),
        migrations.DeleteModel(
            name='PlacesOfIntrest',
        ),
    ]
