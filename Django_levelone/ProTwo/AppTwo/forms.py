from django import forms
from django.forms import ModelForm
from django.core import validators
from AppTwo.models import userrecord

class Sign_Up_Form(forms.ModelForm):
    class Meta:
        model = userrecord
        fields = '__all__'
    
