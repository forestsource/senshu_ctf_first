# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='description',
            field=models.TextField(default=''),
        ),
    ]