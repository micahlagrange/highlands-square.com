# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(upload_to='businesses/logos', null=True),
        ),
        migrations.AlterField(
            model_name='shopgallery',
            name='image',
            field=models.ImageField(upload_to='businesses/gallery', null=True),
        ),
    ]
