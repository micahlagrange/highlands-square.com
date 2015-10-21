# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150801_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.TextField(null=True, max_length=800),
        ),
    ]
