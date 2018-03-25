from django.db import models

#Create your models here.

class ActiveManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(active=True)

class Country(models.Model):
	CODES_CHOICES = (
			('colombia','CO'),
			('mexico','MX'),
			('estados unidos','USA'),
			('argentina','AR')
		)
	
	name      = models.CharField(max_length=255)
	code      = models.CharField(max_length=10, choices=CODES_CHOICES)
	continent = models.ForeignKey('continentes.Continent', on_delete=models.CASCADE)
	active    = models.BooleanField(default=True)
	active_manager = ActiveManager()
	objects = models.Manager()

	def __str__ (self):
		return self.name
