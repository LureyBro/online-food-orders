import django_filters
from demo_app.models import *
from django_filters import CharFilter


class FoodFilter(django_filters.FilterSet):
	foodname=CharFilter(field_name='food_name',lookup_expr='icontains' ,label='Food ')
	class Meta:
		model=Food
		fields=''
		exclude=['food_price','food_description','Food_image','category','created_by']
		

class HotelFilter(django_filters.FilterSet):
	h=CharFilter(field_name='created_by',lookup_expr='icontains',label='Restaurant Name ',)
	class Meta:
		model=Food
		fields=''
		exclude=['food_price','food_description','Food_image','category','food_name']


