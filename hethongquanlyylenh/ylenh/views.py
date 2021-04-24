from django.shortcuts import render, redirect
from .models import YLenh
from .form import YLenhForm
from django.http import HttpResponseRedirect , HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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

    
