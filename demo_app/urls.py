from django.urls import path
from . import views

urlpatterns = [
	path('',views.index),
	path('food/',views.show_food),
	path('addcategory/',views.post_category),
	path("addfood/",views.post_food),
    path('category/',views.show_category),
	path('delete_category/<int:category_id>',views.delete_category),
	path('update_category/<int:category_id>',views.update_category_form),
	path('delete_food/<int:food_id>',views.delete_food),
	path('update_food/<int:food_id>',views.food_update_form),
	path('usersorder/',views.user_order),

]
