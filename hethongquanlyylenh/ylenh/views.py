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
    return render(request, 'ylenh/create_ylenh.html', {'form': form})

def ylenh_detail(request, id):
    ylenh = YLenh.objects.get(id=id)
    return render(request, "ylenh/ylenh_detail.html", {'ylenh': ylenh})

def ylenh_delete(request, id):
    ylenh = YLenh.objects.get(id=id)
    ylenh.delete()
    return HttpResponseRedirect('/ylenh')

# def ylenh_modify(request, id):
#     ylenh = YLenh.objects.get(id=id)
#     yform = YLenhForm(instance=ylenh)
#     if request.method == 'POST':
#         yform = YLenhForm(request.POST, instance=ylenh)
#         if yform.is_valid():
#             yform.save()
#             return redirect("ylenh_list")
#     return render(request, 'ylenh/create_ylenh.html', {'form': yform}) 
    
