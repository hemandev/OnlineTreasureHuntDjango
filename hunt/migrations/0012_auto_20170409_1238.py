# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0011_auto_20170409_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levelmodel',
            name='placeholder_ans',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]