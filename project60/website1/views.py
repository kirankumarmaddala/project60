from django.shortcuts import render
import datetime

# Create your views here.
def fun1(request):
	dt=datetime.datetime.now()
	return render(request,'website1/home.html',{'date':dt})