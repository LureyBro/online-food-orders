from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .auth import admin_only
from django.core.cache import cache
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from userspage.models import *
from demo_app.models import *

# Create your views here.
def user_register(request):
	if request.method == 'POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,'Account created successfully')
			return redirect('/login')
		else:
			messages.add_message(request,messages.ERROR,'Please verify form fields')
			return render(request,'accounts/register.html',{'form':form})
	context={
		'form':UserCreationForm,
	}
	return render(request,'accounts/register.html',context)

def user_login(request):
	if request.method == 'POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			user=authenticate(request,username=data['username'],password=data['password'])
			if user is not None:
				login(request,user)
				return redirect('/dashboard')
			else:
				messages.add_message(request,messages.ERROR,'Please provide correct credential')
				return render(request,'accounts/login.html',{'form':form})
	context={
		'form':LoginForm
	}
	return render(request,'accounts/login.html',context)

def user_logout(request):
	logout(request)
	return redirect('/login')

@login_required
@admin_only
def dashboard(request):
    order=Order.objects.all()
    total_order=order.count()
    foods=Food.objects.all()
    total_food=foods.count()
    category=Category.objects.all()
    total_category=category.count()
    deliver=order.filter(status='Delivered').count()
    pending=order.filter(status='Pending')
    pending_count=pending.count()
    use=User.objects.all()
    total_user=use.count()
    

    context={
        'total_order':total_order,
        'deliver':deliver,
		'pending':pending,
        'pending_count':pending_count,
        'total_food':total_food,
        'total_category':total_category,
        'total_user':total_user,
        'order':order,

	}
    return render(request, "accounts/dashboard.html",context)
