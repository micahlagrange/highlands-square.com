# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20150924_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': 'Merchant', 'ordering': ['category', 'name']},
        ),
        migrations.AlterModelOptions(
            name='categoryimage',
            options={'verbose_name': 'Carousel Category Image', 'ordering': ['category']},
        ),
        migrations.AlterModelOptions(
            name='shopcategory',
            options={'verbose_name': 'Merchant Category'},
        ),
    ]
