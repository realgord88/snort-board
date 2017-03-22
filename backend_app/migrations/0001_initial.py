# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 22:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_off', models.BooleanField(default=True)),
                ('last_start', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
    ]
