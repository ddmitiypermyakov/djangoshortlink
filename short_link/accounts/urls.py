from django.urls import path
from accounts.views import AuthUserLogin, UserRegister, index

urlpatterns = [
    path('',index, name= 'home'),
    path('login/', AuthUserLogin.as_view(), name="login"),
    path('register/', UserRegister.as_view(), name="register"),
]