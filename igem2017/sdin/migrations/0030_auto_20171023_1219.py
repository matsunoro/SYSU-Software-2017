# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdin', '0029_merge_20171023_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='logo',
            field=models.URLField(default='static\\img\\Team_img\\none.jpg'),
        ),
        migrations.AlterField(
            model_name='works',
            name='DefaultImg',
            field=models.URLField(default='static\\img\\Team_img\\none.jpg'),
        ),
    ]