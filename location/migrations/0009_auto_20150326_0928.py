# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0008_auto_20150325_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=25, choices=[(b'Do', b'Do'), (b'See', b'See'), (b'Get around', b'Get around')])),
                ('text', models.TextField(blank=True)),
                ('city', models.ForeignKey(to='location.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('directions', models.CharField(max_length=250, blank=True)),
                ('category', models.CharField(max_length=25, choices=[(b'Do', b'Do'), (b'See', b'See'), (b'Get around', b'Get around')])),
                ('description', models.TextField(blank=True)),
                ('city', models.ForeignKey(to='location.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=25, choices=[(b'Do', b'Do'), (b'See', b'See'), (b'Get around', b'Get around')])),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField(blank=True)),
                ('url', models.URLField(null=True)),
                ('city', models.ForeignKey(to='location.City')),
                ('listings', models.ManyToManyField(to='location.Listing', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cityinfo',
            name='sections',
            field=models.ManyToManyField(to='location.Section', null=True, blank=True),
            preserve_default=True,
        ),
    ]
