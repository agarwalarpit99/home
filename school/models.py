from django.db import models

# Create your models here.
class Registration(models.Model):
	ward_name=models.CharField(max_length=200)
	sex=models.CharField(max_length=200)
	dob=models.CharField(max_length=200)
	applyfor=models.CharField(max_length=200)
	mother_name=models.CharField(max_length=200)
	father_name=models.CharField(max_length=200)
	address_name=models.TextField(max_length=200)
	mobile=models.IntegerField()
	phone=models.IntegerField()
	email=models.CharField(max_length=200)

	def __str__(self):
		return self.ward_name