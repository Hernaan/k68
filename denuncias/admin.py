# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from denuncias.models import Denuncia, Servicio, TipoServicio


admin.site.register(Denuncia)
admin.site.register(Servicio)
admin.site.register(TipoServicio)