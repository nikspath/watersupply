# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-12 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mainproperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyname', models.CharField(max_length=200)),
                ('propertydesc', models.CharField(max_length=255)),
                ('propertytype', models.CharField(max_length=200)),
                ('propertyrate', models.CharField(max_length=200)),
                ('propertyimg', models.FileField(upload_to='media/images/')),
            ],
        ),
    ]
