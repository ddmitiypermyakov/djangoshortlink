from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    """
    Form - class for authenticating users
    """
    class Meta:
        model = User
        fields = ("username", "password",)

class RegisterUserForm(forms.ModelForm):
    """
    Form - class for register users
    """

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ("username", 'email')