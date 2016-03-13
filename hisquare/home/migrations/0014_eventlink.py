# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20151212_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=200, null=True)),
                ('event', models.ForeignKey(to='home.Event')),
            ],
        ),
    ]
