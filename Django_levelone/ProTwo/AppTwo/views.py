from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import userrecord
from AppTwo import forms
# Create your views here.


def index(request):
    text_input={'filler':'Please use /users in the URL to get the list of the Users'}
    return render(request,'AppTwo/index.html',context=text_input)

def user(request):
    UserRecord=userrecord.objects.order_by('First_Name')
    my_list ={'userData':UserRecord}
    return render(request,'AppTwo/users.html',context=my_list)

def signUp(request):
    info = forms.Sign_Up_Form()

    if request.method =='POST':

        info = forms.Sign_Up_Form(request.POST)
        if info.is_valid():
            info.save()
            return index(request)
        else:
            print("Can not save the data")

    return render(request,'AppTwo/signup.html',{'form':info})
