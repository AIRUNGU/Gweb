# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gapp', '0002_auto_20180603_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='category',
        ),
    ]
