from django.shortcuts import render
from .models import Patient
from .form import PatientForm, UpdatePatientForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def list(request):
    Patients = Patient.objects.all()
    search_field = request.GET.get('search_field')
    in_search = request.GET.get('in_search')
    if search_field == 'Name':
        Patients = Patients.filter(patient_name__icontains=in_search)
    if search_field == 'Doctor':
        Patients = Patients.filter(doctor__username__icontains=in_search)
    pag = Paginator(Patients, 8)
    pag_num = request.GET.get('page')
    try:
        patient= pag.page(pag_num)
    except PageNotAnInteger:
        patient = pag.page(1)
    except EmptyPage:
        patient = pag.page(pag.num_pages)
    return render(request,'patient/patient.html', {'patient': patient})

def create_patient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            publish = form.save()
            publish.doctor = request.user
            publish.save()
            return HttpResponseRedirect('/patient')
    return render(request,'patient/patient_form.html', {'form': form}) 

def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return HttpResponseRedirect('/patient')

def modify_patient(request, id):
    patient = Patient.objects.get(id=id)
    form = UpdatePatientForm(instance=patient)
    if request.method == 'POST':
        form = UpdatePatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/patient')
    return render(request,'patient/patient_modify.html', {'form': form})