from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

import json
from pprint import pprint
from jsonmerge import merge

from website.models import Statement 
from website.models import Article
from website.models import User
from website.models import Tweet

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
		statement = Statement.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This statement does not exist')

	try:
		articles = Article.objects.filter(statement=statement)
	except ObjectDoesNotExist:
		raise Http404('This articles does not exist')
	decisions = ['is almost surely true','is probably true','cannot be certainly identified','is probably fake','is almost surely fake']
	
	try:
		tweets = getTweets(statement.title)
		tweetWithScore = [0] * len(tweets)
		for i in range(len(tweets)):
			analysis = analyse(tweets[i])
			tweetWithScore[i] = merge(tweets[i], analysis)
			update_tweets(tweetWithScore[i],statement)
	except:
		tweetWithScore = Tweet.objects.filter(statements=statement)
	return render(request, 'website/statement.html', {
		'decisions': decisions,
		'item': statement,
		'tweets':tweetWithScore,
		#'tweets':tweets,
		'articles':articles,
	})


def update_tweets(tweet,statement):
	#add user to a database
	user, createdUser = User.objects.get_or_create(name=tweet['user']['name'])
	if createdUser:
		user.name = tweet['user']['name']
		user.screen_name = tweet['user']['screen_name']
		user.profile_image_url_https = tweet['user']['profile_image_url_https']
		user.save()	
	#add tweet to a database
	tweetDB, created = Tweet.objects.get_or_create(user=user,id_str=tweet['id_str'])
	tweetDB.id_str = tweet['id_str']
	tweetDB.text = tweet['text']
	tweetDB.retweet_count = tweet['retweet_count']
	tweetDB.favorite_count = tweet['favorite_count']
	tweetDB.created_at = tweet['created_at']
	tweetDB.score = tweet['score']
	tweetDB.setProblems(tweet['problems'])
	tweetDB.statements.add(statement)
	tweetDB.save()

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

