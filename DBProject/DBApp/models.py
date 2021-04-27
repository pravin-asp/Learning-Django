from django.db import models

# Create your models here.
class Employee(models.Model):
	empNo = models.IntegerField()
	empName = models.CharField(max_length = 20)
	empSalary = models.FloatField()
	empAddress = models.CharField(max_length = 100)

def __str__(self):
	return 'Employee details are shared ' + empName 
# An object of one class behaving as an object of another class 