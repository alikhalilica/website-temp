from django.contrib import admin
from .models import contact

# Register your models here.

class ContactAdmin (admin.ModelAdmin):
    list_display=("subject","Email","name","created_date")
    list_filter=("created_date","Email")
    search_fields=["subject","message"]





admin.site.register(contact,ContactAdmin)
