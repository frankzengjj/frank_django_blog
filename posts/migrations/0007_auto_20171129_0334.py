# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20171129_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='100', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default='100', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', null=True, upload_to='media/', width_field='image_width'),
        ),
    ]
