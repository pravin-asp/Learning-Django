from django.db import models

# Create your models here.
class Details(models.Model):
	Name = models.CharField(max_length = 20)
	PhoneNo = models.IntegerField()
	Address = models.CharField(max_length = 50)
	Pincode = models.IntegerField()