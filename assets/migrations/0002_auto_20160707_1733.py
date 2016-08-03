# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='category',
            field=models.CharField(choices=[('it', 'IT EQUIPMENT'), ('leisure', 'LEISURE')], default='IT EQUIPMENT', max_length=100),
        ),
    ]
