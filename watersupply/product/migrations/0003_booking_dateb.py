# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-18 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190418_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='dateB',
            field=models.DateField(blank=True, default='2019-04-18', null=True),
        ),
    ]