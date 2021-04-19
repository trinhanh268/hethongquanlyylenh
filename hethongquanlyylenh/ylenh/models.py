from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class YLenh(models.Model):
    username = models.ForeignKey(User, editable=False, on_delete = models.CASCADE, null=True)
    patient = models.CharField(max_length=30)
    content = models.TextField()
    day_start = models.DateTimeField(auto_now_add=True)
    day_end = models.DateField("Day End(mm/dd/yyyy)")
    