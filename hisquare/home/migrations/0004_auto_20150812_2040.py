# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150810_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('starttime', models.TimeField(default=datetime.time(0, 0), null=True, blank=True)),
                ('endtime', models.TimeField(default=datetime.time(23, 59, 59, 999999), null=True, blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['category', 'name']},
        ),
    ]
