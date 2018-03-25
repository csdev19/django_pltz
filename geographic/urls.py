from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView
from countries.views import (HomeView,
                             TagsView, 
                            )
                             # CountryDetailView,
                             # CountryDetailIdView

# ahora enves de importar solo la funcion home 
# from countries.views import home
# from continentes.views import HomeContinentes

# ahora vamos a empezar a usar includes 
urlpatterns = [
    path ('admin/', admin.site.urls),
    # path('',TemplateView.as_view(template_name = 'countries/home.html'))
    path ('', HomeView.as_view(), name='home' ),
    # ahora podemos ver un poco mas como funcionana las urls /<nombre>/
    path ('tags/', TagsView.as_view(), name='tags'),
    # path ('continent/', HomeContinentes.as_view(), name='continent_home'),
    path ('continent/', include('continentes.urls' , namespace = 'continent') ),
    # tambien podemos validar de la sgte manera 
    # entonces si el elemento es un entero sera procesado aqui y si no pasara 
    # a <code> no olvide el orden importa si <code> estuviera arriba se ejecutara ese
    # path ('countries/<int:id>/',CountryDetailIdView.as_view(), name='country_detail_id'),
    # esto es una ruta cuando se define asi <nombre>
    # path ('countries/<code>/',CountryDetailView.as_view(), name='country_detail'),
    path ('countries/', include('countries.urls' , namespace = 'countries') ),
    path ('people/', include('people.urls' , namespace = 'people') ),
]
    