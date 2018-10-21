# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from .views import emailView

app_name = "sendmail"

urlpatterns = [
    path('email/', emailView, name='email'),
]