from django.db import models

# Create your models here.
class NameEmail(models.Model):
	Name = models.CharField(max_length = 10)
	Email = models.CharField(max_length = 30)