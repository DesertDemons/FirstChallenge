from django.db import models

# Create your models here.

class Game(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.CharField(max_length=250)	
	

	def __str__(self):
		return self.name