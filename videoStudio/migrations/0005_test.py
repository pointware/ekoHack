# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoStudio', '0004_item_vip_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naem', models.CharField(max_length=200)),
            ],
        ),
    ]
