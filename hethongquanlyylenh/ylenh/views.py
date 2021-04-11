from django.shortcuts import render
from .models import YLenh

# Create your views here.
def list(request):
    Data = {'YLenhs': YLenh.objects.all().order_by('-day_start')}
    return render(request, 'ylenh/ylenh.html', Data)    
