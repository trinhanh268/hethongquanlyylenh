from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class YLenh(models.Model):
    STATUS = (
        ('Complete', 'Complete'),
        ('Fail', 'Fail'),
        ('Doing', 'Doing'),
    )
    username = models.ForeignKey(User, editable=False, on_delete = models.CASCADE, null=True)
    patient = models.CharField(max_length=30)
    title = models.CharField(default='Y Lenh', max_length=40)
    content = models.TextField()
    day_start = models.DateTimeField(auto_now_add=True)
    day_end = models.DateField("Day End(mm/dd/yyyy)")
    status = models.CharField(max_length=12, default='Doing', choices=STATUS)
    
    