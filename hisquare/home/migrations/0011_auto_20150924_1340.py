# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150813_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(blank=True, upload_to='businesses/logos', null=True),
        ),
        migrations.AlterField(
            model_name='shopcategory',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
