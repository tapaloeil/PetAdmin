# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pet', '0013_auto_20170813_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petimagemodel',
            name='Pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PetPhotos', to='Pet.PetModel'),
        ),
    ]