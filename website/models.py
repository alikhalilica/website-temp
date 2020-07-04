from django.db import models

# Create your models here.
class contact(models.Model):
    message = models.TextField() 
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=100)