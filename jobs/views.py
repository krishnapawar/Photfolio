from django.shortcuts import render,get_object_or_404
from.models import jobs


def myjobs(request):
	j=jobs.objects
	return render(request,'jobs/home.html',{'job':j})

def bdm(request,bid):
	detiel=get_object_or_404(jobs,id=bid)
	return render(request,'jobs/fblog.html',{'b':detiel})

