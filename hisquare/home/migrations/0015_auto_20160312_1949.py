# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_eventlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlink',
            name='href',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eventlink',
            name='text',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
