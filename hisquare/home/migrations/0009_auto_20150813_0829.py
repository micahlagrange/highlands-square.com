# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20150813_0825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryimage',
            options={'ordering': ['category']},
        ),
    ]
