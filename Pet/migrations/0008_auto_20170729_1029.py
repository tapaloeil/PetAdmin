# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pet', '0007_auto_20170729_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petimagemodel',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='petimagemodel',
            name='Pet',
        ),
        migrations.DeleteModel(
            name='PetImageModel',
        ),
    ]
