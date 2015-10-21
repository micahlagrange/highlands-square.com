# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150812_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopgallery',
            name='business',
        ),
        migrations.AddField(
            model_name='shopgallery',
            name='category',
            field=models.ForeignKey(null=True, to='home.ShopCategory'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventimage',
            field=models.ImageField(null=True, blank=True, upload_to='events/images'),
        ),
        migrations.AlterField(
            model_name='shopgallery',
            name='image',
            field=models.ImageField(null=True, upload_to='categories/None'),
        ),
    ]
