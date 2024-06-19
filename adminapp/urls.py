from django.urls import path
from . import views

urlpatterns = [
	
	path("customer/",views.customer),
	path("food/",views.food),
	path("create_order/<int:food_id>/",views.createOrder,name='createorder'),
	path("deleteorder/<int:food_id>/",views.delete_order,name='deleteorder'),
	path("page/",views.page)
]