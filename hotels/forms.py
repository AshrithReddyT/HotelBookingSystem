from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Hotel,Room

class BookingForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['room_type', 'occupancy','room_type','available']