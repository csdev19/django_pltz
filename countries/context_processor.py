from django.urls import reverse
from countries.models import Country

def countries_data (request):
	countries = Country.objects.all()
	return {'countries': countries}
	# peru = {
	# 	'nombre': 'peru',
	# 	'code': 'PE',
	# 	'id' : 1,
	# 	'detail_url' : reverse ('country_detail_id', kwargs = {'id' : 1 })
	# 	}
	# argentina = {
	# 	'nombre': 'argentina',
	# 	'code': 'AR',
	# 	'id' : 2,
	# 	'detail_url' : reverse ('country_detail_id', kwargs = {'id' : 2 })
	# 	}
	# colombia = {
	# 	'nombre': 'colombia',
	# 	'code': 'CO',
	# 	'id' : 3,
	# 	'detail_url' : reverse ('country_detail_id', kwargs = {'id' : 3 })
	# 	}
	# brazil = {
	# 	'nombre': 'brazil',
	# 	'code': 'BR',
	# 	'id' : 4,
	# 	'detail_url' : reverse ('country_detail_id', kwargs = {'id' : 4 })
	# 	}
	# countries = [peru,colombia,argentina,brazil]
	# # retornamos un diccionario que es la data que queremos enviar
	# return {'countries': countries}
