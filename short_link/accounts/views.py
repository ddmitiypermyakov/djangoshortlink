from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from accounts.forms import AuthUserForm, RegisterUserForm
# Create your views here.
from django.views.generic import CreateView


def index(request):
    return render(request,"index.html")

class AuthUserLogin(LoginView):
    """
    Display the login form and handle the login action.
    """
    template_name = "auth/login.html"
    form_class = AuthUserForm

class UserRegister(CreateView):
    """
   View for creating User.
    """
    model = User
    template_name = "register.html"
    form_class = RegisterUserForm
    success_msg = "Пользователь создан"