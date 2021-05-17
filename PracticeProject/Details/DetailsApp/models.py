from django.db import models

# Create your models here.
class SignUpForm(models.Model):
	Email = models.CharField(max_length = 30)
	Phone_No = models.IntegerField()
	Password = models.CharField(max_length = 20)