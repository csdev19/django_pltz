from django.contrib import admin
from django.urls import path, include
from continentes.views import HomeContinentes

app_name = 'continent'

urlpatterns = [
    # ahora no es necesario ponerle un nombre 
    # path'continent/' como antes porque ahora se tomara el nombre del urlsprincip
    path ('', HomeContinentes.as_view(), name='home'),
]
