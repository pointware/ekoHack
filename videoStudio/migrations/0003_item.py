# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoStudio', '0002_auto_20171024_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('gd_no', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]