from django.shortcuts import render
from.models import blog

# Create your views here.
def blogging(request):
	blogs=blog.objects
	return render(request,'blog/index.html',{'mypost':blogs})
