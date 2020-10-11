from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.utils.html import strip_spaces_between_tags, strip_tags
from django.utils.text import Truncator
# Create your models here.
from meta.models import ModelMeta


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(ModelMeta,models.Model):

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
    published_date = models.DateTimeField(default=timezone.now)

    _metadata = {
    'title': 'title',
    'description': 'get_meta_content',
    'image': 'get_meta_image',
    'published_time': 'published_date',
    'modified_time': 'updated_date',
    'url': 'get_absolute_url',
    'locale': 'fa_IR',
    #'keywords':'get_meta_keywords'

    }

    class Meta: 
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:single_post', kwargs={"post_slug": str(self.slug)})

    def snippet(self):
        return self.content[0:100]

    def get_meta_content(self):
        value = strip_spaces_between_tags(self.content)
        value = value.replace("</p>"," </p>")
        value = value.replace("&quot","  ")
        value = strip_tags(value)
        return Truncator(value).words(40)

    def get_meta_image(self):
        if self.image:
            return self.image.url