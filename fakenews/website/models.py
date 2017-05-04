from __future__ import unicode_literals

from django.db import models

class Statement(models.Model):
	title = models.CharField(max_length=200)
	fakeness = models.IntegerField(default=0)
	usersvoteFake = models.IntegerField(default=0)
	usersvoteTrue = models.IntegerField(default=0)
	tags = models.TextField(default="")
	pass

class Article(models.Model):
	title  = models.CharField(max_length=200)
	source = models.CharField(max_length=200)
	link   = models.URLField(max_length=200)
	image  = models.URLField(max_length=200)
	statement = models.ForeignKey(Statement, on_delete=models.CASCADE)

