from django.contrib import admin
from .models import Patient

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['patient_name','birthday', 'gender', 'doctor', 'sympton']
    list_filter = ['patient_name', 'doctor']
    search_fields = ['patient']

admin.site.register(Patient, PostAdmin)