from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
	empName = models.CharField(max_length = 20)
	empID = models.IntegerField()
	empDept = models.CharField(max_length = 10)
	empDOB = models.DateField()