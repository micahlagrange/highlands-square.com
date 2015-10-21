# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150813_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryimage',
            name='image',
            field=models.ImageField(null=True, upload_to='categories/images'),
        ),
    ]
