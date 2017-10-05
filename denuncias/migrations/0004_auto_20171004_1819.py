# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 18:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0003_auto_20171003_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='denuncias', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]