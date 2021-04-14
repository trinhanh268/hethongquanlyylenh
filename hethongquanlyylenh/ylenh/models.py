from django.db import models

# Create your models here.
class YLenh(models.Model):
    username = models.CharField(max_length=25)
    patient = models.CharField(max_length=30)
    content = models.TextField()
    day_start = models.DateTimeField(auto_now_add=True)
    day_end = models.DateField()
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+&', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")