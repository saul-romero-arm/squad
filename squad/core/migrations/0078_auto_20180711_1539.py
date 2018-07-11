# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-11 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_knownissue'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectstatus',
            name='tests_known_failures',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='status',
            name='tests_known_failures',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='result',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]