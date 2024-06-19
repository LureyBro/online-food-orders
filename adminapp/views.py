from django.shortcuts import render, redirect
from userspage.models import *
from .forms import *
from django.contrib import messages


# Create your views here.
# customer order details
def customer(request):
    order = Order.objects.all()
    order_count = order.count()
    context = {"order": order, "or": order_count}
    return render(request, "inv/customer.html", context)

#show food items in order
def food(request):
    food = Order.objects.all()
    context = {"food": food}
    return render(request, "inv/food.html", context)

# admin deliver ,pending
def createOrder(request,food_id):
    form = Order.objects.get(id=food_id)
    if request.method == "POST":
        form = OrderForm(request.POST,instance=form)
        if form.is_valid():
            form.save(commit = True)
            messages.add_message(request, messages.SUCCESS, "Added form")
            return redirect("/dashboard")
    context = {
        "form": OrderForm(instance=form)
        }
    return render(request, "inv/order_create.html", context)

#delete order admin
def delete_order(request,food_id):
    order=Order.objects.get(id=food_id)
    order.delete()
    messages.add_message(request,messages.SUCCESS,'Delete Order')
    return redirect('/dashboard')
    
def page(request):
    return render(request,'inv/home.html')