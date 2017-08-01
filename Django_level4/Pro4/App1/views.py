from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'App1/index.html')


def base(request):
    return render(request,'App1/base.html')



def other(request):
    return render(request,'App1/others.html')
