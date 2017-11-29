# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20171129_0334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
