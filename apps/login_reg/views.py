from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
# Create your views here.

def index(request):
		return render(request, "login_reg/index.html")

# ___________________________________________________________________________________________
def process(request):
    if request.method == 'POST':
        user=User.objects.reg(request.POST['first'], request.POST['last'], request.POST['email'], request.POST['password'], request.POST['password2'])
        if not user[0]:
        	for i in range(0,len(user[1])):
	        	messages.error(request,user[1][i])
        	return redirect('login_reg_app:index')
        else:	
			request.session['user_info']=user[1].id
			return redirect('login_reg_app:secrets')

# ___________________________________________________________________________________________
def login(request):
	user=User.objects.login(request.POST)
	if  user[0]==False:
		messages.error(request,user[1])
		return redirect('login_reg_app:index')		
	else:
		request.session['user_info']=user[1].id
		return redirect('login_reg_app:secrets')

# ___________________________________________________________________________________________	
def secrets(request):
	if 'user_info' in request.session:		
		return redirect( "secret_app:index")
	else:
		messages.warning(request,"Don try to steal my cookies! RUDE!!")
		return redirect('login_reg_app:index')

# ___________________________________________________________________________________________
def logout(request):
	del request.session['user_info']	
	return redirect('login_reg_app:index')