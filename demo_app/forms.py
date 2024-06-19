from django.forms import ModelForm,fields
from . models import *

class CategoryForm(ModelForm):
	class Meta:
		model=Category
		fields='__all__'

class FoodForm(ModelForm):
	class Meta:
		model=Food
		fields='__all__'