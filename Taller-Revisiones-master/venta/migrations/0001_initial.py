# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-01 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=25)),
                ('color', models.CharField(choices=[('Verde', 'Verde'), ('Azul', 'Azul'), ('Rojo', 'Rojo'), ('Amarillo', 'Amarillo')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.Auto')),
            ],
        ),
        migrations.CreateModel(
            name='Consecionario',
            fields=[
                ('nit', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filtro', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=50)),
                ('aceite', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=50)),
                ('frenos', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=50)),
                ('motor', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=50)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.Auto')),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='consecionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.Consecionario'),
        ),
    ]
