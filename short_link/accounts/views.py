from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse
from accounts.forms import AuthUserForm, RegisterUserForm
# Create your views here.
from django.views.generic import CreateView, TemplateView


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
    template_name = "register.html"
    form_class = RegisterUserForm
    success_msg = "Пользователь создан"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password == password2:
                User.objects.create_user(username,email, password)
                return redirect(reverse("login"))
        context = {'form': self.form_class}
        return render(request, self.template_name,context)