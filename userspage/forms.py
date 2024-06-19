from django import forms
from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
	class Meta:
		model=Order
		fields=['quantity','contact_no','address','payment_method']

