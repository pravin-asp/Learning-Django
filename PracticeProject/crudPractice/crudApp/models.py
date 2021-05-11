from django.db import models

# Create your models here.
class Employee(models.Model):
	Name = models.CharField(max_length = 20)
	EmpId = models.CharField(max_length = 7)