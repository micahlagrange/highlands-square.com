# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150813_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(null=True, upload_to='categories/None')),
                ('category', models.ForeignKey(null=True, to='home.ShopCategory')),
            ],
        ),
        migrations.RemoveField(
            model_name='shopgallery',
            name='category',
        ),
        migrations.DeleteModel(
            name='ShopGallery',
        ),
    ]
