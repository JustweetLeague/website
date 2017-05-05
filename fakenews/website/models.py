from __future__ import unicode_literals
import json

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

class User(models.Model):
	name = models.CharField(max_length=200)
	screen_name = models.CharField(max_length=200)
	profile_image_url_https = models.URLField(max_length=400)
	pass

class Tweet(models.Model):
	"""docstring for Tweet"""
	id_str = models.IntegerField(default=0)
	text = models.TextField(default="")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	retweet_count = models.IntegerField(default=0)
	favorite_count = models.IntegerField(default=0)
	created_at = models.CharField(max_length=200,default="")
	score = models.IntegerField(default=-1)
	statements = models.ManyToManyField(Statement)
	
	problemsSaved = models.CharField(max_length=1000)
    	def setProblems(self, x):
        	self.problemsSaved = json.dumps(x)
    	def problems(self):
        	return json.loads(self.problemsSaved)



