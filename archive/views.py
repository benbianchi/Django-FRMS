from django.shortcuts import get_object_or_404, render
from .models import Club, Budget, Portion, Request
from django.views.generic import TemplateView
from django.db.models import Sum
from FRMS_Utils import toList
from django.core import serializers
import json


		

def indexPage(request):
    return render(request, 'archive/index.html', {})

def clubList(request):
	clubs = Club.objects.all()
	return render(request,'archive/club_list.html', {"clubs":clubs})


def display_club(request,num="1"):
	num = int(num)
	club = get_object_or_404(Club,clubID=num)
	portlist =list(Portion.objects.filter(clubID_id=num).values('requestAmount','reviewDate')  )
	reqlist = Request.objects.filter(clubID_id=num);
	print len(portlist)
	for x in xrange(0,len(portlist)):
		portlist[x]['reviewDate']=str(portlist[x]['reviewDate'])
	budgets = Budget.objects.filter(clubID=num);
	print "Hello"
	return render(request, 'archive/club_template.html',{"club":club, "requests":reqlist, "portions":json.dumps(portlist),"budgets":budgets})


def display_request(request,num="1"):
	club = get_object_or_404(Club,clubID=int(num))
	event = get_object_or_404(Request,EventNumber=int(num) )
	portions = Portion.objects.filter(requestNumber=int(num)).order_by('requestNumber')
	chartdata = []

	
	return render(request, 'archive/request_template.html',{'Event':event, "club":club, "portions":portions})

def display_search(request):

	sf = request.META
	print sf
	clubs = Club.objects.filter(shortName__icontains=sf)
	events = Request.objects.filter(EventName__icontains=sf) | Request.objects.filter(Eventinfo__icontains=sf)
	requests = Request.objects.filter(requestDescription__icontains=sf)
	return render(request, 'archive/search_results.html',{'events':events})





def statistics(request):
	return render(request, 'archive/statistics.html',{'clubs':Club.objects.all()})
#Input: ChartType, filterkeys, filtervalues
#Output: chartdata, chartoptions


from django.http import JsonResponse,HttpResponse

def populateChart(request):

	# take all filters and keys use a for loop to iterate through.
	# unsure how exactly to pass information.
	# data = json.loads(request.body)
	modelData = request.GET.get('model')

	
	if modelData == "Budget":
		return JsonResponse(Budget.objects ,safe=False)
	if modelData == "Club":
		return JsonResponse(Club.objects,safe=False)
	if modelData == "Request":
		return JsonResponse(Request.objects,safe=False)
	if modelData == "Portion":
		return JsonResponse(Portion.objects,safe=False)



    # type = request.GET.get('type', 'default')
	#okay, now we need to get through all of the filtering.
	# for filt,key in data['filters']:
	# 	# apply new filters
	# 	print Request.objects( **([filt]:key))
	return HttpResponse(modelData)
	
	# l = Request.objects.filter(requestNumber=1).order_by('requestNumber')
	


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['title', 'body',])
        
        found_entries = Entry.objects.filter(entry_query).order_by('-pub_date')

    return render('search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))
