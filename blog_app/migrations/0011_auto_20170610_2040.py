# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 00:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_auto_20170610_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date']},
        ),
    ]