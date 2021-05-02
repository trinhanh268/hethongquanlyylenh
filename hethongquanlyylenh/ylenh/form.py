from django import forms
from .models import YLenh

class YLenhForm(forms.ModelForm):
    class Meta:
        model = YLenh
        exclude = ['username']
        fields = ['title', 'patient', 'content', 'day_end']
        day_end = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))

class UpdateYLenhForm(forms.ModelForm):
    class Meta:
        model = YLenh
        exclude = ['username']
        fields = ['title', 'patient', 'content', 'day_end', 'status']
        day_end = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))