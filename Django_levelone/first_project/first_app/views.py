from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Accessrecord,Webpage,Topic

# Create your views here.

def index(request):
    # my_dict = {'insert_me':'Hello im coming from the views.py'}
    # return render(request,'first_app/index.html',context=my_dict)
    weblist = Webpage.objects.order_by('name')
    my_dict2 = {'webdata':weblist,'insert_me':'Hello im coming from the views.py'}
    return render(request,'first_app/index.html',context=my_dict2)

def data(request):
    weblist = Webpage.objects.order_by('Name')
    my_dict2 = {'webdata':weblist}
    return render(request,'first_app/index.html',context=my_dict2)
