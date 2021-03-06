# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filer.fields.image
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('Pet', '0008_auto_20170729_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('Image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='filer.Image')),
                ('Pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pet.PetModel', verbose_name='Animal')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
