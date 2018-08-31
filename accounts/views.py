from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import TemplateView

from .forms import ManagerSignUpForm
from .models import User

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class ManagerSignUpView(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('hotel-list')
