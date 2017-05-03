from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse

from booker.models import *
# Create your views here.
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.

class LibrosCreateView(CreateView):
	model = Libros
	# indiquem la plantilla personalitzada i els camps que han d'apareixer al formulari
	# veureu que la plantilla es molt senzilla ja que fa tot el formulari amb {{form.as_p}}
	template_name = "libros.html"
	fields = ['nombre','genero','portada','sinopsis']

class LibrosListView(ListView):
	model = Libros
	template_name = "libroshecho.html"
	# si no posem template_name agafara per defecte karaoke/item_list.html
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)