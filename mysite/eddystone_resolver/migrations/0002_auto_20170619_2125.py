# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eddystone_resolver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beacon',
            name='key',
            field=models.CharField(max_length=32),
        ),
    ]