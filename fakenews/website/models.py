from __future__ import unicode_literals

from django.db import models

class Statement(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	fakeness = models.IntegerField()
	usersvoteFake = models.IntegerField()
	usersvoteTrue = models.IntegerField()
	usersvote = models.IntegerField()
	
