from django.shortcuts import get_object_or_404, render
from .models import Club, Budget, Request, Event
from django.views.generic import TemplateView
from django.db.models import Sum
import random
import json

class PieChartSlice(object):
	"""docstring for PieChartSlice"""
	def __init__(self, value,label):
		super(PieChartSlice, self).__init__()
		self.value = value
		r = lambda: random.randint(0,255)
		self.color =('#%02X%02X%02X' % (r(),r(),r()))
		self.highlight = self.color
		self.label = label
		

def allClubs(request):
    posts = Club.objects.all()
    return render(request, 'archive/club_list.html', {'posts': posts})

def display_club(request,num="1"):

	num =int(num);
	c = get_object_or_404(Club, clubID=num)
	b = get_object_or_404(Budget,clubID=num)
	r = Request.objects.filter(clubID=num).aggregate(Sum('requestAmount'))
	l = Request.objects.filter(clubID=num).order_by('reviewDate')
	
	labelstring = []
	datastring = []

	for record in l:
		labelstring.append('\"'+str(record.reviewDate)+'\"')
		datastring.append('\"'+str(record.requestAmount)+'\"')


	chartdata =	{'labels':(','.join(labelstring) ),'data':(','.join(datastring) )	}
	package = {'club': c,'budget': b,'request': r, 'list':l,"chart":chartdata}
	return render(request, 'archive/assemble_club.html',{'package':package})


def display_request(request,num="1"):
	fdot = get_object_or_404(Event,requestNumber=num )
	l = Request.objects.filter(requestNumber=num).order_by('requestNumber')
	chartdata = []
	for x in l:
		k = {}
		k['value'] = x.requestAmount
		r = lambda: random.randint(0,255)
		k['color'] = ('#%02X%02X%02X' % (r(),r(),r()))
		k['highlight'] = k['color']
		k['label'] = x.requestDescription
		chartdata.append(k)

	
	package = {'fdot': fdot,'requests': l,'PieChartData':json.dumps(chartdata) }
	return render(request, 'archive/assemble_fr.html',{'package':package})

def display_search(request):

	sf = request.META
	print sf
	clubs = Club.objects.filter(shortName__icontains=sf)
	events = Event.objects.filter(EventName__icontains=sf) | Event.objects.filter(Eventinfo__icontains=sf)
	requests = Request.objects.filter(requestDescription__icontains=sf)
	return render(request, 'archive/search_results.html',{'clubs':clubs, 'events':events, 'requests':requests})



#Input: ChartType, filterkeys, filtervalues
#Output: chartdata, chartoptions


from django.http import JsonResponse

def populateChart(request):

	# take all filters and keys use a for loop to iterate through.
	# unsure how exactly to pass information.
	data = json.loads(request.body)
	#okay, now we need to get through all of the filtering.
	# for filt,key in data['filters']:
	# 	# apply new filters
	# 	print Request.objects( **([filt]:key))
	
	
	# l = Request.objects.filter(requestNumber=1).order_by('requestNumber')
	
	to_json = {
	"key1":"value1"
	}
	return JsonResponse((to_json))