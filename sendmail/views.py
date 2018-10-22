# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .SECRET import EMAIL
def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            hotel_name = form.cleaned_data['hotel_name']
            hotel_email = form.cleaned_data['hotel_email']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            subject = name + 'wants to add ' + hotel_name + '(' + location + ')'
            message ="""
Greetings Admin!
A request has been recieved to add a new hotel to the database:-

Hotel Name: %s
Location: %s
Hotels Email ID: %s
Requested By: %s
Users Email ID: %s
Contact Number: %s



Regards,
Team HBS.
""" % (hotel_name,location,hotel_email,name,email,contact)
            try:
                send_mail(subject, message, EMAIL, [EMAIL])
                success = "Mail sent Successfully."
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return  render(request, "email.html", {'success': success})
    return render(request, "email.html", {'form': form})