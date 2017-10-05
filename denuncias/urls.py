from django.conf.urls import url, include
from django.contrib import admin
from denuncias.views import index, DenunciaCreate, listar, detail, check_pubs, listaDetalles, contacto, nosotros
from denuncias.views import RegistroUsuario, terminos
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'registrar',RegistroUsuario.as_view(), name="registrar"),
    url(r'^$', login_required(index), name='index'),
    url(r'^crear/', login_required(DenunciaCreate.as_view()), name='denuncia_crear'),
    url(r'^listar/', login_required(listar.as_view()), name='listar'),
    url(r'^(?P<denuncia_id>[0-9]+)/$', login_required(detail), name='detail'),
    url(r'^check_pubs/$', check_pubs, name='check_pubs'),
	url(r'^detalles/', listaDetalles, name='listaDetalles'),
	url(r'^contacto', contacto, name='contacto'),
	url(r'^nosotros', nosotros, name='nosotros'),
	url(r'^terminos', terminos, name='terminos'),
]