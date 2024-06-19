from django.db import models
from demo_app.models import *
from tkinter import CASCADE
from django.contrib.auth.models import User
class Cart(models.Model):
	food=models.ForeignKey(Food,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	created_date=models.DateTimeField(auto_now_add=True)


class Order(models.Model):
	PAYMENT=(
		('Cash on Delivery','Cash on Delivery'),
		#('Esewa',"Esewa"),
		#('Khalti','Khalti')
	)
	food=models.ForeignKey(Food,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	quantity=models.IntegerField()
	total_price=models.IntegerField(null=True)
	STATUS=[
		('Pending','Pending'),
		('Out for deliver','Out of deliver'),
		('Delivered','Delivered')
	]
	status=models.CharField(default='Pending',max_length=200,choices=STATUS,null=True)
	payment_method=models.CharField(max_length=200,choices=PAYMENT)
	payment_status=models.BooleanField(default=False,null=True)
	contact_no=models.CharField(max_length=15)
	address=models.CharField(max_length=50)
	order_date=models.DateTimeField(auto_now_add=True)

