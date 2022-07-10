from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from accounts.forms import AuthUserForm, RegisterUserForm
from django.views.generic import CreateView


class AuthUserLogin(LoginView):
    """
    Display the login form and handle the login action.
    """
    template_name = "auth/login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy("home")

    def get_success_url(self):
        return self.success_url


class AuthUserLogout(LogoutView):
    """
    Log out the user and display the 'You are logged out' message.
    """
    template_name = "auth/logout.html"


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
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))
        context = {'form': self.form_class}
        return render(request, self.template_name, context)
