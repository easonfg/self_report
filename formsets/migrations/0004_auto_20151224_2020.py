# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsets', '0003_todoitem_another'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='another',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='items',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='Descriptions',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='Type',
            field=models.CharField(default='', max_length=150),
        ),
    ]
