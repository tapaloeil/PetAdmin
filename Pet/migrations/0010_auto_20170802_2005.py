# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Pet', '0009_petimagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('Nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('Prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('Adresse', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adresse')),
                ('Adresse2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adresse 2')),
                ('CP', models.CharField(blank=True, max_length=10, null=True, verbose_name='CP')),
                ('Ville', models.CharField(max_length=100, verbose_name='Ville')),
                ('Pays', models.CharField(choices=[('France', 'France'), ('Belgique', 'Belgique'), ('Suisse', 'Suisse'), ('Espagne', 'Espagne')], default='France', max_length=100, verbose_name='Pays')),
                ('Telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Téléphone')),
                ('Telephone2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Téléphone 2')),
                ('TypeMaison', models.CharField(default='Maison', max_length=30, verbose_name='Type habitation')),
                ('TailleMaison', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('OK_CHAT', models.CharField(choices=[('Y', 'Oui'), ('N', 'Non'), ('U', 'Je ne sais pas')], default='U', max_length=1, verbose_name='OK Chat ?')),
                ('OK_CHIEN', models.CharField(choices=[('Y', 'Oui'), ('N', 'Non'), ('U', 'Je ne sais pas')], default='U', max_length=1, verbose_name='OK Chien ?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='petmodel',
            name='FA',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pet.FA', verbose_name="Famille d'accueil"),
        ),
    ]
