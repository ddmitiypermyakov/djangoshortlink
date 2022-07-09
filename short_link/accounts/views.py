from django.contrib.auth.views import LoginView
from django.shortcuts import render
from accounts.forms import AuthUserForm
# Create your views here.
def index(request):
    return render(request,"index.html")

class AuthUserLogin(LoginView):
    """
    Display the login form and handle the login action.
    """
    template_name = "auth/login.html"
    form_class = AuthUserForm

