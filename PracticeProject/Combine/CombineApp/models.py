from django.db import models

# Create your models here.
class Models(models.Model):
	Name = models.CharField(max_length = 20)
	Dob = models.DateField()