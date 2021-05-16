from django.shortcuts import render, redirect
from .models import YLenh
from .form import YLenhForm, UpdateYLenhForm
from django.http import HttpResponseRedirect , HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime 

# Create your views here.
def list(request):
    search_field = request.GET.get('search_field')
    in_search = request.GET.get('in_search')
    status_field = request.GET.get('status')
    YLenhs = YLenh.objects.filter(username=request.user).order_by('-day_start')
    if status_field == 'Doing':
        YLenhs = YLenhs.filter(status='Doing')
    if status_field == 'Fail':
        YLenhs = YLenhs.filter(status='Fail')
    if status_field == 'Complete':
        YLenhs = YLenhs.filter(status='Complete')
    if search_field == 'Title':
        YLenhs = YLenhs.filter(title__icontains=in_search)
    if search_field == 'Patient':
        YLenhs = YLenhs.filter(patient__patient_name__icontains=in_search)
    pag = Paginator(YLenhs, 8)
    pag_num = request.GET.get('page')
    try:
        ylenh = pag.page(pag_num)
    except PageNotAnInteger:
        ylenh = pag.page(1)
    except EmptyPage:
        ylenh = pag.page(pag.num_pages)
    for y in ylenh:
        date = datetime.datetime.today()
        if (date.year > y.day_end.year and y.status == 'Doing'):
            y.status = 'Fail'
            y.save()
        if (date.year == y.day_end.year and date.month > y.day_end.month and y.status == 'Doing'):
            y.status = 'Fail'
            y.save()
        if (date.year == y.day_end.year and date.month == y.day_end.month and date.day > y.day_end.day and y.status == 'Doing'):
            y.status = 'Fail'
            y.save()
    return render(request, 'ylenh/ylenh.html', {'Data':ylenh})    

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
    form = UpdateYLenhForm(instance=ylenh)
    date = datetime.date.today()
    if request.method == 'POST':
        form = UpdateYLenhForm(request.POST, instance = ylenh)
        if form.is_valid():
            publish = form.save()
            publish.day_update = date
            publish.save()
            return HttpResponseRedirect ('/ylenh')
    context = {'form': form}
    return render(request, 'ylenh/ylenh_modify.html', context=context)

def ylenh_view_pdf(request, id):
    ylenh = YLenh.objects.get(id=id)
    template_path = 'ylenh/ylenh_detail.html'
    context = {'ylenh': ylenh}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="ylenh.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def dashboard(request):
    date = request.GET.get('date_search')
    ylenh = YLenh.objects.filter(day_update=date)
    doing = 0
    complete = 0
    fail = 0
    create = 0
    if date:
        ylenhs = YLenh.objects.all()
        for y in ylenhs:
            if y.status == 'Doing':
                doing += 1 
    for y in ylenh:
        if y.status == 'Complete':
            complete += 1
        elif y.status == 'Fail':
            fail += 1
    return render(request,'ylenh/ylenh_broadcast.html',{'d':doing, 'c':complete, 'f':fail, 'cr':create})