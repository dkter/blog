# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20170610_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, verbose_name='Time submitted'),
            preserve_default=False,
        ),
    ]
