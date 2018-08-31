from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from hotels.models import Hotel
from .models import User, Manager

class ManagerSignUpForm(UserCreationForm):
    hotel = forms.ModelChoiceField(
        queryset=Hotel.objects.all(),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        student = Manager.objects.create(user=user, hotel=self.cleaned_data.get('hotel'))
        return user