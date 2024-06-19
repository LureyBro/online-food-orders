from django.db import models

# Create your models here.
class Category(models.Model):
	category_name=models.CharField(max_length=200,unique=True)
	 
	def __str__(self):
		return self.category_name

class Food(models.Model):
	food_name=models.CharField(max_length=100)
	food_price=models.PositiveIntegerField()
	Food_image=models.FileField(upload_to='static/uploads',null=True)
	food_description=models.TextField()
	created_by=models.CharField(max_length=50)
	category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.food_name
