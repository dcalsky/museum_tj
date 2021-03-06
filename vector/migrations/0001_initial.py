# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('secret', models.BooleanField(default=False)),
                ('page_view', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vector.Part'),
        ),
    ]
