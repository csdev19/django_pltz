from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from countries.models import Country
# para trabajar con Classes Based View
# from django.views.generic import View
# o con template view

# Create your views here.

# # AHORA ENVES DE FUNCION SERA UN CLASE
# def home (request):
# 	return render (request, 'countries/home.html')

# class HomeView (View):
	# NO FUNCIONA SI LE DOY GETVIEW 
	# def get (self, request, *args, **kwargs):
	# 	return render (request, 'countries/home.html')

# o podriamos usar templateview

class HomeView (TemplateView):
	template_name = 'countries/home.html'
# los template views tienen una forma de mandar datos al template
	# def get_context_data (self, *args, **kwargs):
	# 	cristian = {'nombre' : 'cristian','edad' : 19}
	# 	diego = {'nombre' : 'diego','edad' : 14}
	# 	lucho ={'nombre' : 'lucho','edad' : 45}
	# 	mari ={'nombre' : 'mari','edad'  : 49}
	# 	saludo = [cristian, diego, lucho, mari]
	# 	return {'saludo': saludo}


class TagsView (TemplateView):
	template_name = 'countries/tags.html'
	

class CountryDetailView (TemplateView):
	template_name = 'countries/countries_detail.html'

	def get_context_data (self, *args, **kwargs):
	# como kwargs es un diccionario
		code = kwargs['code']  	
		return {'code': code}


# class CountryDetailIdView (TemplateView):
# 	template_name = 'countries/countries_detail_id.html'
 
# 	def get_context_data (self, *args, **kwargs):
# 		country = get_object_or_404(Country, id=kwargs['id'])
# 		return {'country': country}
class CountryDetailIdView (DetailView):
	template_name = "countries/countries_detail_id.html"
	model         = Country


class CountrySearchView (ListView):
	template_name = 'countries/search.html'
	
	model         = Country

	def get_queryset(self):
		query = self.kwargs['query']
		return Country.objects.filter(name__contains=query)
