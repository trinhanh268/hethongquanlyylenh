from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    GENDER = (
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    ) 
    patient_name = models.CharField(max_length=30)
    birthday = models.DateField("Day End(mm/dd/yyyy)")
    gender = models.CharField(max_length=12, default='Nam', choices=GENDER)
    phone_number = models.CharField(max_length=50)
    doctor = models.ForeignKey(User, editable=True, on_delete = models.CASCADE, null=True)
    sympton = models.TextField()
    note = models.TextField()
    def __str__(self):
        return self.patient_name