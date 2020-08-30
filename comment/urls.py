
from django.urls import path,include
from . import views
app_name = 'comment'

urlpatterns = [
    path('create',views.CreateComment,name='create'),
    #path('<int:comment_id>/delete',views.DeleteComment,name='delete'),
    #path('<int:comment_id>/edit',views.EditComment,name='edit'), 
   
]