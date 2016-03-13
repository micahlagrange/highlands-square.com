# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_eventlink_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventlink',
            name='href',
        ),
    ]
