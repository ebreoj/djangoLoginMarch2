# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_qoutelist_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='qoutelist',
            name='fav',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='posts.User'),
            preserve_default=False,
        ),
    ]
