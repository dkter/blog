# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_auto_20170610_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(verbose_name='Time submitted'),
        ),
    ]