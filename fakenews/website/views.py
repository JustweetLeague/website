from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

import json
from pprint import pprint
from jsonmerge import merge

from website.models import Statement 
from website.models import Article
from website.getTweets import getTweets
from website.analyseTweets import analyse

def index(request):
	items = Statement.objects.exclude(id=1)
	return render(request, 'website/index.html', {
		'items': items,
	})

def search(request):
	if 'q' in request.GET:
		if request.GET['q'] == '':
		  message = ''
		else:
		  message = request.GET['q']
	else:
	  message = 'Form is not submitted properly.'

	items = Statement.objects.filter(tags__icontains=message)
	return render(request, 'website/search.html', {
		'message' : message,
		'items': items,
	})

def statement(request, id):
	try:
		item = Statement.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')

	try:
		articles = Article.objects.filter(statement=item)
	except ObjectDoesNotExist:
		raise Http404('This articles does not exist')
	decisions = ['is almost surely true','is probably true','cannot be certainly identified','is probably fake','is almost surely fake']
	tweets = getTweets(item.title)
	tweetWithScore = [0] * len(tweets)
	for i in range(len(tweets)):
		analysis = analyse(tweets[i])
		tweetWithScore[i] = merge(tweets[i], analysis)
	return render(request, 'website/statement.html', {
		'decisions': decisions,
		'item': item,
		'tweets':tweetWithScore,
		#'tweets':tweets,
		'articles':articles,
	})

def update_fVotes(request):
	try:
		fVote = request.GET.get('fakeVote')
    		sID = request.GET.get('statementID')
    		statement = Statement.objects.get(id=sID)
    		statement.usersvoteFake = fVote;
    		statement.save()
		return HttpResponse("Update successful!")
	except:
   		return HttpResponse("Oh... Update failed...")

def update_tVotes(request):
	try:
		tVote = request.GET.get('trueVote')
    		sID = request.GET.get('statementID')
    		statement = Statement.objects.get(id=sID)
    		statement.usersvoteTrue = tVote;
    		statement.save()
		return HttpResponse("Update successful!")
	except:
   		return HttpResponse("Oh... Update failed...")

