# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appoint',
            options={'ordering': ['finished']},
        ),
        migrations.AlterField(
            model_name='appoint',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
