#ram vai => Neepal@12

from multiprocessing import context
from django.shortcuts import render,redirect
from demo_app.models import *
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only
from .models import *
from django.contrib import messages
from .forms import OrderForm
from .filters import FoodFilter
from . filters import HotelFilter

# Create your views here.
def homepage(request):
	foods=Food.objects.all().order_by('-id')
	hotel_filter=HotelFilter(request.GET,queryset=foods)  #filter
	hotel_final=hotel_filter.qs 
	context={
		'foods':hotel_final,
		'hotel_filter':hotel_filter

	}
	return render(request,'client/homepage.html',context)


def foods(request):
	foods=Food.objects.all().order_by('-id')
	food_filter=FoodFilter(request.GET,queryset=foods)  #filter
	food_final=food_filter.qs                           # all 

	context={
		'foods':food_final,
		'food_filter':food_filter
	}
	return render(request,'client/foods.html',context)

def food_details(request,food_id):
	food=Food.objects.get(id=food_id)
	context={
		'food':food
	}
	return render(request,'client/fooddetails.html',context)

@login_required
@user_only
def add_to_cart(request,food_id):
	user=request.user
	food=Food.objects.get(id=food_id)

	check_item_presence=Cart.objects.filter(user=user,food=food)
	if check_item_presence:
		messages.add_message(request,messages.ERROR,'Recipy already present in the cart')
		return redirect('/mycart')
	else:
		cart=Cart.objects.create(food=food,user=user)
		if cart:
			messages.add_message(request,messages.SUCCESS,'Items added to cart')
			return redirect('/mycart')
		else:
			messages.add_message(request,messages.ERROR,'Unable to add to cart')
			return redirect('/foods')


@login_required
@user_only
def show_cart_items(request):
	user=request.user
	items=Cart.objects.filter(user=user)
	context={
		'items':items
	}
	return render(request,'client/cart.html',context)
	
@login_required
@user_only
def order_form(request,food_id,cart_id):
	user=request.user
	food=Food.objects.get(id=food_id)
	cart_item=Cart.objects.get(id=cart_id)

	if request.method == 'POST':
		form=OrderForm(request.POST)
		if form.is_valid():
			quantity=request.POST.get('quantity')
			if int(quantity)<0:
				messages.add_message(request,messages.ERROR,'Quantity can not be negative')
				return render(request,'client/orderform.html',{'form':form})
			price=food.food_price
			total_price=int(quantity)*int(price)
			contact_no=request.POST.get('contact_no')
			if not (contact_no.isdigit() and len(contact_no) == 10 and contact_no[0] == '9'):
				messages.add_message(request, messages.ERROR, 'Invalid phone number format')
				return render(request, 'client/orderform.html', {'form': form})
			address=request.POST.get('address')
			payment_method=request.POST.get('payment_method')
			payment_status=request.POST.get('payment_status')
			status=request.POST.get('status','Pending')

			order=Order.objects.create(
				food=food,
				user=user,
				quantity=quantity,
				total_price=total_price,
				contact_no=contact_no,
				address=address,
				payment_method=payment_method,
				payment_status=payment_status,
				status=status
			)
			if order.payment_method == 'Cash on Delivery':
				cart=Cart.objects.get(id=cart_id)
				cart.delete()
				messages.add_message(request,messages.SUCCESS,'order successfully')
				return redirect('/myorder')
			elif order.payment_method == 'Esewa':
				context={
					'order':order,
					'cart':cart_item
				}
				return render(request,'client/esewa_payment.html',context)
			else:
				messages.add_message(request,messages.ERROR,'Something went wrong')
				return render(request,'client/orderform.html',{'form':form})

	context={
			'form':OrderForm
	}
	return render(request,'client/orderform.html',context)

@login_required
@user_only
def show_order_items(request):
	user=request.user
	items=Order.objects.filter(user=user)
	context={
		'items':items
	}
	return render(request,'client/order.html',context)


def faqs(request):
	return render(request,'client/faqs.html')

def remove_cart_items(request,cart_id):
	item=Cart.objects.get(id=cart_id)
	item.delete()
	messages.add_message(request,messages.SUCCESS,'item removed from the cart')
	return redirect('/mycart')


    
def showuser(request,order_id):
	form=Order.objects.get(id=order_id)
	
	context={
		'i':form,
	}
	return render(request,'client/showuser.html',context)


def profile_info(request):
	return render(request,'client/profile_info.html')
	
def customer(request):
	if request.user.is_authenticated:
		return render(request,'client/customer.html')
	else:
		return redirect('/')
	
def aboutus(request):
	return render(request,'client/aboutus.html')

def blog(request):
	
	return render(request,'client/blog.html')