from django.shortcuts import render
from .models import Registration
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'index.html')
def about(request):
	return render(request,'about.html')
def admissions(request):
	return render(request,'admissions.html')
def contact(request):
	return render(request,'contact-us.html')
def calendar(request):
	return render(request,'school-calendar.html')
def registration(request):
	if request.method=='POST':
		ward_name=request.POST['wrdname']
		sex=request.POST['sex']
		dob=request.POST['dob']
		applyfor=request.POST['applyfor']
		mother_name=request.POST['motname']
		father_name=request.POST['fatname']
		address=request.POST['address']
		mobnum=request.POST['mobnum']
		phnum=request.POST['phnum']
		email=request.POST['email']
		a=Registration(ward_name=ward_name,sex=sex,dob=dob,applyfor=applyfor,mother_name=mother_name
			,father_name=father_name,address_name=address,mobile=mobnum,phone=phnum,email=email)
		a.save()
		return render(request,'admissions.html')

		