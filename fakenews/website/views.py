from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from website.models import Statement 

def index(request):
	items = Statement.objects.exclude(id=1)
	return render(request, 'website/index.html', {
		'items': items,
	})

def statement(request, id):
	try:
		item = Statement.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	decisions = ['is almost surely true','is probably true','cannot be certainly identified','is probably fake','is almost surely fake']
	return render(request, 'website/statement.html', {
		'decisions': decisions,
		'item': item,
	})

from django.shortcuts import render


def search(request):
	items = Statement.objects.exclude(id=1)
	if 'q' in request.GET:
		if request.GET['q'] == '':
		  message = 'No searching keyword entered'
		else:
		  message = 'You searched for: %s' % request.GET['q']
	else:
	  message = 'Form is not submitted properly.'
	return render(request, 'website/search.html', {
		'message' : message,
		'items': items,
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

