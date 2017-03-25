from django.shortcuts import render,redirect
# Create your views here.
from django.db.models import Count
from . models import  Comment
from ..login_reg.models import User
from datetime import date, datetime
#_____________________________________________________________________________________________
def index(request):	
	counter=Comment.objects.annotate(var=Count("users_comment")).order_by("-created_at")
	context={
		"info":User.objects.filter(id=request.session['user_info']),
		'all_comments':Comment.objects.order_by("-created_at").all()[:10],
		'counter':counter
	}
	return render(request,"secret/index.html",context)
#_____________________________________________________________________________________________
def process(request):
	if request.method=="POST":
		info=User.objects.get(id=request.session['user_info'])
		comm=Comment.objects.get_info(request.POST, info)
		return redirect('secret_app:index')
	elif request.method=="GET":
		info=User.objects.get(id=request.session['user_info'])
		comm=Comment.objects.get_info(request.POST, info)
		return redirect('secret_app:popular')

#_____________________________________________________________________________________________
def delete(request,id):
	if request.method=="POST":
		Comment.objects.get(id=id).delete()
		return redirect('secret_app:index')
	if request.method=="GET":
		Comment.objects.get(id=id).delete()
		return redirect('secret_app:popular')

#_____________________________________________________________________________________________
def like(request,id):		
		if request.method=="POST":
			var=request.session['user_info']
			table=Comment.objects.like(var,id)
			return redirect('secret_app:index')
		if request.method=="GET":
			var=request.session['user_info']
			table=Comment.objects.like(var,id)
			return redirect('secret_app:popular')

#_____________________________________________________________________________________________
def popular(request):
	counter=Comment.objects.annotate(var=Count("users_comment")).order_by("-var")
	context2={
		"info":User.objects.filter(id=request.session['user_info']),
		'counter':counter
	}
	return render(request,"secret/index2.html",context2)


			