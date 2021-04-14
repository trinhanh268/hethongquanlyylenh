from django import forms
from .models import YLenh
import requests

def get_username():
    return requests.user.username() 

class YLenhForm(forms.ModelForm):
    class Meta:
        model = YLenh
        # fields = '__all__'
        fields = ['username', 'patient', 'content', 'day_end']
        forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )
    