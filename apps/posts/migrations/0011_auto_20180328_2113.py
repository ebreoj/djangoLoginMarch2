# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_qoutelist_fav'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qoutelist',
            name='fav',
        ),
        migrations.AddField(
            model_name='qoutelist',
            name='itemname2',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
