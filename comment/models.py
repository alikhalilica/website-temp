from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    Rating_modes = ((1,1)
                    ,(2,2)
                    ,(3,3)
                    ,(4,4)
                    ,(5,5)
    )
    user = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    body = models.TextField(max_length=500)
    url = models.SlugField(max_length=200)
    rating = models.PositiveIntegerField(choices=Rating_modes,null=True,default=None,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField()
    parent = models.ForeignKey('self',null=True,on_delete=models.CASCADE,blank=True)
    likes = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.name 

    @property
    def replies(self):
        replies = Comment.objects.filter(parent=self.pk,approved_comment=True).order_by("created_date")
        return replies