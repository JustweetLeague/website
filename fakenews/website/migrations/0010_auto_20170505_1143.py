# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170505_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.CharField(default='', max_length=200),
        ),
    ]