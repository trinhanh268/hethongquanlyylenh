from django.shortcuts import render
from .models import YLenh
from .form import YLenhForm
from django.http import HttpResponseRedirect 

# Create your views here.
def list(request):
    Data = {'YLenhs': YLenh.objects.all().order_by('-day_start')}
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


