from django.shortcuts import render, redirect
from .models import YLenh
from .form import YLenhForm
from django.http import HttpResponseRedirect 

# Create your views here.
def list(request):
    Data = {'YLenhs': YLenh.objects.filter(username=request.user).order_by('-day_start')}
    return render(request, 'ylenh/ylenh.html', Data)    

def create_ylenh(request):
    form = YLenhForm()
    if request.method == 'POST':
        form = YLenhForm(request.POST)
        if form.is_valid():
            publish = form.save()
            publish.username = request.user
            publish.save()
            return HttpResponseRedirect('/ylenh')
    return render(request, 'ylenh/ylenh_form.html', {'form': form})

def ylenh_delete(request, id):
    ylenh = YLenh.objects.get(id=id)
    ylenh.delete()
    return HttpResponseRedirect('/ylenh')
    
def ylenh_modify(request, id):
    ylenh = YLenh.objects.get(id=id)
    form = YLenhForm(instance=ylenh)
    if request.method == 'POST':
        form = YLenhForm(request.POST, instance = ylenh)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect ('/ylenh')
    context = {'form': form}
    return render(request, 'ylenh/ylenh_form.html', context=context)



    
