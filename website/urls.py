from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'website'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]

