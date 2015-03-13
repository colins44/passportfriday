# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('weekend', '0003_auto_20150313_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekendItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.SlugField()),
                ('object_id', models.PositiveIntegerField()),
                ('parent_object_id', models.IntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('parent_content_type', models.ForeignKey(related_name='Flights', to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='taggeditem',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='taggeditem',
            name='parent_content_type',
        ),
        migrations.DeleteModel(
            name='TaggedItem',
        ),
    ]
