from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from website.models import Statement 

def index(request):
	items = Statement.objects.exclude(id=1)
	return render(request, 'website/index.html', {
		'items': items,
	})


def statements(request):
	items = Statement.objects
	return render(request, 'website/relatedStat.html', {
		'items': items,
	})

def statement(request, id):
	try:
		item = Statement.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'website/statement.html', {
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

'''
def search(request):
    if request.method == 'POST':
        # do some processing
        form = ContactForm(request.POST)
        if form.is_valid():
            s_query = form.cleaned_data['search_query']
            s_results = SomeTable.objects.filter(name=s_query)
            return render(request, 'search.html', {'form': form, 's_results': s_results})
    else:
        form = SearchForm()
    return render(request, 'website/search.html', {'form': form,})
'''