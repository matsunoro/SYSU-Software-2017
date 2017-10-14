# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sdin', '0004_auto_20171010_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='CircuitDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Circuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sdin.Circuit')),
                ('Subparts', models.ManyToManyField(to='sdin.CircuitParts')),
            ],
        ),
        migrations.AddField(
            model_name='works',
            name='Circuit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sdin.Circuit'),
        ),
        migrations.AlterField(
            model_name='works',
            name='Description',
            field=models.TextField(default='To be add'),
        ),
        migrations.AlterField(
            model_name='works',
            name='Use_parts',
            field=models.TextField(),
        ),
    ]
