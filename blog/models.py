from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS = ((0, "draft"), (1, "published"))
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ManyToManyField(Category)  # category__name
    content = RichTextUploadingField()
    likes = models.ManyToManyField(User)
    tags = TaggableManager()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_author')  # SET_NULL (null=True)
    image = models.ImageField(upload_to="blog/")

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:single', kwarg={"slug": str(self.slug)})

    def snippet(self):
        return self.content[0:100]
