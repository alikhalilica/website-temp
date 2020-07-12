from django.db import models

# Create your models here.
class contact(models.Model):
    message = models.TextField() 
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.subject