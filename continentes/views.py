from django.shortcuts import render
from django.views.generic import  TemplateView


# Create your views here.

class HomeContinentes (TemplateView):
	template_name = "continentes/home.html"


	def get_context_data (self, *args, **kwargs):
		america = { 
			'nombre' : 'america',
			'traduccion':'america',	
			'color' : '#f26419',
		}
		europa = { 
			'nombre' : 'europa',
			'traduccion':'europa',
			'color' : '#e71d36',
		}
		antartida = { 
			'nombre' : 'antartida',
			'traduccion':'antartida',	
			'color' : '#52ffb8',
		}	
		antartica = { 
			'nombre' : 'antartica',
			'traduccion':'antartica',	
			'color' : '#218380',
		}

		continentes = [america,europa,antartica,antartida]

		return {'continentes' : continentes}

