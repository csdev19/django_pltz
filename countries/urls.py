
from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView
from countries.views import (
						CountryDetailView,
                        CountryDetailIdView,
                        CountrySearchView
                    )

app_name = 'countries'

urlpatterns = [
    path ('search/<query>/',CountrySearchView.as_view(), name='country_search'),
    path ('<int:pk>/',CountryDetailIdView.as_view(), name='id_detail'),
    path ('<code>/',CountryDetailView.as_view(), name='detail'),
]
