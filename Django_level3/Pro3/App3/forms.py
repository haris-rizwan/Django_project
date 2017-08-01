from django import forms
from django.core import validators



class NameForm(forms.Form):

    FirstName =forms.CharField()
    LastName =forms.CharField()
    Email =forms.EmailField()
    Verify_Email=forms.EmailField()
    Bio =forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data= super().clean()

        email = all_clean_data['Email']
        vemail = all_clean_data['Verify_Email']

        if email != vemail :
            raise forms.ValidationError('Email does not match')
