from django import forms
from countries.models import Country
from people.models import Person
from django.forms import ModelForm

class RegisterForm(forms.Form):
	first_name = forms.CharField(label='first_name')
	nacionality = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
	father = forms.ModelChoiceField(required=False, queryset=Person.objects.all())


class RegisterFormModel (forms.ModelForm):

	class Meta:
		model = Person
		fields = ['first_name', 'nacionality', 'father']

 

