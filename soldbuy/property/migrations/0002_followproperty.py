# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-17 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='followproperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('propertyid', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
