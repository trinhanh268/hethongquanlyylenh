from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines('<h1>This is home page</h1>')
    response.write('<p>Hello!!!</p>')
    return response
    
