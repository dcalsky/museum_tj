# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 14:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vector', '0004_auto_20160523_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 23, 22, 7, 4, 100474)),
        ),
    ]