from django.conf.urls import url, include
from django.contrib import admin
from denuncias.views import index, listar, detail, check_pubs, listaDetalles, contacto, nosotros
from denuncias.views import RegistroUsuario, terminos, denuncia_create
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'registrar',RegistroUsuario.as_view(), name="registrar"),
    url(r'^$', login_required(index), name='index'),
    #url(r'^crear/', login_required(DenunciaCreate.as_view()), name='denuncia_crear'), Falta importar si vas a usar
    url(r'^crear2/', login_required(denuncia_create), name='denuncia_crear'),
    url(r'^listar/', listar.as_view(), name='listar'),
    url(r'^(?P<denuncia_id>[0-9]+)/$', detail, name='detail'),
    url(r'^check_pubs/$', check_pubs, name='check_pubs'),
	url(r'^detalles/', login_required(listaDetalles), name='listaDetalles'),
	url(r'^contacto', login_required(contacto), name='contacto'),
	url(r'^nosotros', login_required(nosotros), name='nosotros'),
	url(r'^terminos', terminos, name='terminos'),
]