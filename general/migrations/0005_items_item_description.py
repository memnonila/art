# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_items_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_description',
            field=models.CharField(blank=True, max_length=85L),
        ),
    ]
