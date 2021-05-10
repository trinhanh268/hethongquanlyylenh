from django import forms
from .models import YLenh
from patient.models import Patient
from datetime import date
class YLenhForm(forms.ModelForm):
    class Meta:
        model = YLenh
        exclude = ['username']
        fields = ['title', 'patient', 'content', 'day_end']
        day_end = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))
        patient = forms.ModelChoiceField(queryset=Patient.objects.all())

class UpdateYLenhForm(forms.ModelForm):
    class Meta:
        model = YLenh
        exclude = ['username', 'day_update']
        fields = ['title', 'patient', 'content', 'day_end', 'status']
        day_end = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))
        