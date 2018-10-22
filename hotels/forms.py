from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Booking

from .models import Hotel,Room

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['room', 'begin_time', 'end_time', 'num_rooms']
        