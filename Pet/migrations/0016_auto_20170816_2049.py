# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-16 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet', '0015_auto_20170815_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petimagemodel',
            name='Image',
            field=models.ImageField(upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='PetName',
            field=models.CharField(max_length=200, verbose_name='Nom\t'),
        ),
    ]
