from django.contrib import admin
from .models import Post,Category

# Register your models here.
class PostAdmin (admin.ModelAdmin):
    list_display=("title","get_categories","author","created_date")
    list_filter=("created_date",)
    search_fields=["title","author"]
    prepopulated_fields = {"slug":('title',)}
    
    def get_categories(self,obj):
        return " , ".join([c.name for c in obj.category.all()])


admin.site.register(Post,PostAdmin)
admin.site.register(Category)