from django import forms
from django.forms import ModelForm

from userspage.models import *
class OrderForm(ModelForm):
	class Meta:
		model=Order
		fields=['status']