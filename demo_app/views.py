from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages
import os
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from userspage.models import Order

# Create your views here.
def index(request):
	return HttpResponse("this is from the demo app ")

@login_required
@admin_only
def show_food(request):
	foods=Food.objects.all()
	context={
		'food':foods
	}
	return render(request,'demo/index.html',context)

@login_required
@admin_only
def post_category(request):
	if request.method=='POST':
		form=CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,'category added')
			return redirect('/demo/addcategory')
		else:
			messages.add_message(request,messages.ERROR,'Please verify forms fields')
			return render(request,'demo/addcategory.html',{
				'form':form
			})

	context={
		'form':CategoryForm
	}
	return render(request,'demo/addcategory.html',context)

@login_required
@admin_only
def post_food(request):
	if request.method=='POST':
		form=FoodForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,'product added')
			return redirect('/demo/addfood')
		else:
			messages.add_message(request,messages.ERROR,'product added')
			return render('demo/addcategory.html',{
				'form':form
			})

	context={
		'form':FoodForm
	}
	return render(request,'demo/addfood.html',context)

@login_required
@admin_only
def show_category(request):
	category=Category.objects.all()
	context={
		'category':category
	}
	return render(request,'demo/category.html',context)

@login_required
@admin_only
def delete_category(request,category_id):
	category=Category.objects.get(id=category_id)
	category.delete()
	messages.add_message(request,messages.SUCCESS,'category deleted')
	return redirect('/demo/category')

@login_required
@admin_only
def update_category_form(request,category_id):
	category=Category.objects.get(id=category_id)
	if request.method=='POST':
		form=CategoryForm(request.POST,instance=category)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,'category updated')
			return redirect('/demo/category')
		else:
			messages.add_message(request,messages.ERROR,' unable to update category')
			return render('demo/updatecategory.html',{
				'form':form
			})
	context={
		'form':CategoryForm(instance=category)
	}
	return render(request,'demo/updatecategory.html',context)

@login_required
@admin_only
def delete_food(request,food_id):
	food=Food.objects.get(id=food_id)
	os.remove(food.Food_image.path)
	food.delete()

	messages.add_message(request,messages.SUCCESS,'food deleted')
	return redirect("/demo/food")

@login_required
@admin_only
def food_update_form(request,food_id):
	food=Food.objects.get(id=food_id)
	if request.method == 'POST':
		if request.FILES.get('Food_image'):
			os.remove(food.Food_image.path)
		form=FoodForm(request.POST,request.FILES,instance=food)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,'Food added')
			return redirect('/demo/food')
		else:
			messages.add_message(request,messages.ERROR,'faild to update food')
			return render(request,'demo/updatefood.html',{'form':form})
	context={
		'form':FoodForm(instance=food)
	}
	return render(request,'demo/updatefood.html',context)


@login_required
@admin_only
def user_order(request):
	items=Order.objects.all()
	context={
		'items':items
	}
	return render(request,'demo/usersorder.html',context)
	