from django.urls import path
from . import views

urlpatterns = [
	path("",views.homepage),
	path("foods/",views.foods),
	path('fooddetails/<int:food_id>',views.food_details),
	path('add_to_cart/<int:food_id>',views.add_to_cart),
	path('mycart/',views.show_cart_items),
	path('orderform/<int:food_id>/<int:cart_id>',views.order_form),
	path('myorder/',views.show_order_items),
	path('faqs/',views.faqs),
	path('remove_cart/<int:cart_id>',views.remove_cart_items),
	path('showuser/<int:order_id>/',views.showuser,name="showuser" ),
	path('profiles/',views.profile_info,name="profile" ),
	path('user/',views.customer),
	path('about/',views.aboutus),
	path('blog/',views.blog),

	
]
