# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0003_auto_20160523_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoint',
            name='amount',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='phone',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='appoint',
            name='time',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
