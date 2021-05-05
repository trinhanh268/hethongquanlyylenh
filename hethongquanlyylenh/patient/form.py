from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['doctor']
        fields = ['patient_name', 'birthday', 'gender', 'phone_number', 'sympton', 'note']
        birthday = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))

class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['doctor']
        fields = ['patient_name', 'birthday', 'gender', 'phone_number', 'sympton', 'note']
        birthday = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))