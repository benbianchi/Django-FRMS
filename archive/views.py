from django.shortcuts import get_object_or_404, render
from .models import Club, Budget, Request, Funding
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



# class Request(models.Model):
#     requestNumber=models.ForeignKey(Funding)
#     requestAmount = models.FloatField()
#     requestDescription = models.TextField()
#     outcome = models.TextField()
#     reviewDate = models.DateField()
#     requestType = models.IntegerField(choices=requestTypeOptions,default=1)
#     clubID = models.ForeignKey('Club')
# class Funding(models.Model):
#     """
#     Description: Model Description
#     """
#     requestName = models.CharField(max_length=256, verbose_name="Event Name")
#     requestinfo = models.TextField(max_length=512,verbose_name="Event Summary")
#     requestNumber = models.AutoField(primary_key=True)

def display_request(request,num="1"):
	fdot = get_object_or_404(Funding,requestNumber=num )
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

