from django.shortcuts import get_object_or_404, render
from .models import Club, Budget, Request, Funding
from django.views.generic import TemplateView
from django.db.models import Sum

def allClubs(request):
    posts = Club.objects.all()
    return render(request, 'archive/club_list.html', {'posts': posts})

def display_club(request,num="1"):

	num =int(num)-1;
	c = get_object_or_404(Club, clubID=num)
	b = get_object_or_404(Budget,clubID=num)
	r = Request.objects.filter(clubID=num).aggregate(Sum('requestAmount'))
	l = Request.objects.filter(clubID=num)
	
	labelstring = []
	datastring = []

	for record in l:
		labelstring.append('\"'+str(record.reviewDate)+'\"')
		datastring.append('\"'+str(record.requestAmount)+'\"')


	chartdata =	{'labels':(','.join(labelstring) ),'data':(','.join(datastring) )	}
	package = {'club': c,'budget': b,'request': r, 'list':l,"chart":chartdata}
	return render(request, 'archive/assemble_club.html',{'package':package})


def returnStat(request):
		pass

