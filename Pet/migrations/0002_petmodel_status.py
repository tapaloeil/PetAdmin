# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petmodel',
            name='Status',
            field=models.CharField(choices=[('A adopter', 'A adopter'), ('Adopté', 'Adopté'), ('Caché', 'Caché')], default='A adopter', max_length=30),
        ),
    ]
