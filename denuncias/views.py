# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from denuncias.forms import RegistroForm, DenunciaForm
from django.contrib.messages.views import SuccessMessageMixin
from denuncias.models import Denuncia, Servicio, TipoServicio
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from datetime import datetime
from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponse

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('denuncias:nosotros')

def index(request):
	return render(request, 'denuncias/index.html')
"""
class DenunciaCreate(SuccessMessageMixin,CreateView):
	context_object_name = "servicios"
	model = Denuncia
	form_class = DenunciaForm
	template_name = 'denuncias/denuncias_crear.html'
	success_url = reverse_lazy('denuncias:denuncia_crear')#redirigimos a una url de urls.py
	success_message = 'Gracias!!!! Ya recibimos tu denuncia'

	def get_context_data(self, **kwargs):
		context = super(DenunciaCreate, self).get_context_data(**kwargs)
		context['servicios'] = Servicio.objects.all()
		return context
"""
def denuncia_create(request):
	if not request.user.is_authenticated():
		response = HttpResponse("No tienes permiso para hacer eso.")
		response.status_code = 403
		return response
	form = DenunciaForm(request.POST or None, request.FILES or None)
	if form.is_valid() and request.user.is_authenticated():
		instance = form.save(commit=False)
		instance.user = request.user 
		instance.save()
		messages.success(request, "Gracias!!! Ya recibimos tu denuncia !")
		
	context = {
		"form": form
	}
	return render(request, "denuncias/denuncias_crear.html", context)
class listar(ListView):
	model = Denuncia
	template_name = 'denuncias/listar_denuncias.html'
	paginate_by = 4
	ordering = ['-id'] #Si no ordenamos como se muestra los datos no va a funcionar la notificacion

	@method_decorator(permission_required('denuncia.add_denuncia',reverse_lazy('denuncias:index')))
	def dispatch(self, *args, **kwargs):
			return super(listar, self).dispatch(*args, **kwargs)

def detail(request, denuncia_id):
	denuncia = get_object_or_404(Denuncia, pk=denuncia_id)
	return render(request, 'denuncias/detail.html', {'denuncia': denuncia})

def check_pubs(request):
	start = request.GET.get('date')
	today = datetime.now()
	pubs = Denuncia.objects.filter(fecha__range=(start, today)).count() - 1
	return JsonResponse({'num_pubs': pubs})

def listaDetalles(request):
	nombre_servicio = request.GET['servicio']
	# print "ajax nombre_servicio ", nombre_servicio

	result_set = []
	tipos_servicios = []
	pregunta = str(nombre_servicio[1:-1])
	# print "Pregunta: " + pregunta

	servicio_seleccionado = Servicio.objects.get(servicio = pregunta)
	# print "Nombre del servicio seleccionado: ", servicio_seleccionado
	all_tipoServicio = servicio_seleccionado.tiposervicio_set.all()
	
	for tipo in all_tipoServicio:
		# print "Tipo Servicio: ", tipo.Tipo_Servicio
		result_set.append({'TipoServicio': tipo.Tipo_Servicio})
		# print "Result_set: ", result_set
	return HttpResponse(json.dumps(result_set), content_type='application/json')

def contacto(request):
	return render(request, 'denuncias/contacto_form.html')

def nosotros(request):
	return render(request, 'denuncias/nosotros.html')

def terminos(request):
	return render(request, 'denuncias/terminos.html')