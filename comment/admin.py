from django.contrib import admin
from .models import Comment



class CommentAdmin (admin.ModelAdmin):
    list_display=("user","name","url","email","created_date")
    list_filter=("created_date","url",'approved_comment')
    
    
    


admin.site.register(Comment,CommentAdmin)


# Register your models here.
