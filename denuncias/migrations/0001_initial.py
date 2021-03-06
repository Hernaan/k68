# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 17:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('lat', models.CharField(max_length=100, verbose_name='Longitud')),
                ('lng', models.CharField(max_length=100, verbose_name='Latitud')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_Servicio', models.CharField(max_length=100)),
                ('servicio_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='denuncias.Servicio')),
            ],
        ),
        migrations.AddField(
            model_name='denuncia',
            name='dn_servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.Servicio'),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='dn_tiposervicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='denuncias.TipoServicio'),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='denuncias', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
