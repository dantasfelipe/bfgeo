# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('formacao', models.CharField(max_length=200, verbose_name=b'Forma\xc3\xa7\xc3\xa3o')),
                ('email', models.EmailField(unique=True, max_length=50, verbose_name=b'E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name=b'T\xc3\xadtulo')),
                ('texto', models.TextField()),
                ('criado_data', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Criado em')),
                ('publicado_data', models.DateTimeField(null=True, verbose_name=b'Publicado', blank=True)),
                ('nome', models.ForeignKey(to='homeapp.Autor', null=True)),
            ],
        ),
    ]
