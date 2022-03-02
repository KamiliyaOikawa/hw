from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms, models
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

class NewLoginView(LoginView):
    form_class = forms.LoginForm
    success_url = "/users/"
    template_name = "login.html"


class RegisterView(CreateView):
    form_class = forms.RegistrationForm
    template_name = "registration_login.html"
    success_url = "/users/"

class UserListView(ListView):
    queryset = models.CustomUser.objects.all()
    template_name = "user_list.html"

    def get_queryset(self):
        return self.queryset