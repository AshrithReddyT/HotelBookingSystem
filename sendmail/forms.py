# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    hotel_name = forms.CharField(required=True)
    hotel_email = forms.EmailField(required=True)
    email = forms.EmailField(required=True)
    contact = forms.CharField(required=True)