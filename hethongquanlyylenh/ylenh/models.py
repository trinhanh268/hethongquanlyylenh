from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=25)
    patient = models.CharField(max_length=30)
    content = models.TextField()