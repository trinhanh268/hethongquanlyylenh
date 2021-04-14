from django.contrib import admin
from .models import YLenh

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['username', 'patient', 'content', 'day_start', 'day_end']
    list_filter = ['username', 'patient', 'day_start']
    search_fields = ['username', 'patient']

admin.site.register(YLenh, PostAdmin)