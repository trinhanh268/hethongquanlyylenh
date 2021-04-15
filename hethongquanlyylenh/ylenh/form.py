from django import forms
from .models import YLenh
import re

def get_username():
    return requests.user.username() 

class YLenhForm(forms.ModelForm):
    class Meta:
        model = YLenh
        fields = ['username', 'patient', 'content', 'day_end']
        day_end = forms.DateField(
        widget=forms.widgets.DateInput(format="%d/%m/%Y"))