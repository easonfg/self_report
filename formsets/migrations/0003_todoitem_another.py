# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsets', '0002_auto_20151224_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='another',
            field=models.CharField(default='SOME STRING', help_text='e.g. Buy milk, wash dog etc', max_length=150),
        ),
    ]