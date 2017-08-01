from django.shortcuts import render
from App3 import forms

# Create your views here.

def index(request):
    return render(request,'App3/index.html')

def Info_Form(request):
    info = forms.NameForm()

    if request.method == 'POST':

        info = forms.NameForm(request.POST)

        if info.is_valid():
            #you can write the code here if the data provided in form is valid
            print('Validation Successfull')
            print('Fist Name: '+info.cleaned_data['FirstName'])
            print('Last Name: '+info.cleaned_data['LastName'])
            print('Email: '+info.cleaned_data['Email'])
            print('Bio: '+info.cleaned_data['Bio'])

        else:
            print("something is wrong")

    return render(request,'App3/forms.html',{'form':info})
