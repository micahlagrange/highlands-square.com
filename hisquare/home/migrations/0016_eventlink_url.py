# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20160312_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlink',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
