# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_name', models.CharField(max_length=250)),
                ('value', models.IntegerField()),
                ('currency', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
