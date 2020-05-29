from django.shortcuts import render
from . models import Contact

def index(request):
	
	cats = ['SWE','BA','OS','DS','CIO','Marketing']

	params={'allProds':cats}
	
	return render(request,'dash/index.html',params)

def projectview(request,myid):
	
	product = Contact.objects.filter(team=myid)

	return render(request,'dash/projectview.html',{'product':product})

def info(request,myid):

	product = Contact.objects.filter(project=myid)

	return render(request,'dash/info.html',{'product':product})

def contact(request):

	thank = False

	if(request.method=="POST"):

		name=request.POST.get('name','')
		email=request.POST.get('email','')
		zoho=request.POST.get('zoho','')
		phone=request.POST.get('phone','')
		linkedin=request.POST.get('linkedin','')
		team=request.POST.get('team','')
		project=request.POST.get('project','')
		
		contact=Contact(name=name,email=email,zoho=zoho,phone=phone,linkedin=linkedin,team=team,project=project)
		contact.save()

		thank = True

	return render(request,'dash/contact.html',{'thank':thank})
