from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Project,Team

def project_view(request):
	#import ipdb; ipdb.set_trace()
	projects = Project.objects.all()
	
	return render(request,'index.html',{'projects':projects})

def project_view_detail(request,title):
	#import ipdb; ipdb.set_trace()
	project = get_object_or_404(Project, titulo=title)

	return render(request,'proyecto.html',{'project':project})




