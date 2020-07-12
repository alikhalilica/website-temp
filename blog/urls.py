from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'blog'

urlpatterns = [
    path('',views.list_post,name='list_post'),
    path('post/<str:post_slug>',views.single_post,name='single_post'), # <int:id>
]