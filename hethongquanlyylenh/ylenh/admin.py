from django.contrib import admin
from .models import YLenh

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['username_id', 'patient', 'content', 'day_start', 'day_end']
    list_filter = ['username_id', 'patient', 'day_start']
    search_fields = ['username_id', 'patient']

admin.site.register(YLenh, PostAdmin)