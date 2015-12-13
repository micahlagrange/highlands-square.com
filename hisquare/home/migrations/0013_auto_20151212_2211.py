# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20151021_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcategory',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.TextField(blank=True, null=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='business',
            name='tagline',
            field=models.CharField(blank=True, null=True, max_length=75),
        ),
    ]
