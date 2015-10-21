# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150812_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventimage',
            field=models.ImageField(upload_to='events/images', null=True),
        ),
    ]
