from django.urls import path
from accounts.views import AuthUserLogin, AuthUserLogout, UserRegister, index

urlpatterns = [
    path('',index, name= 'home'),
    path('login/', AuthUserLogin.as_view(), name="login"),
    path('logout/', AuthUserLogout.as_view(), name="logout"),
    path('register/', UserRegister.as_view(), name="register"),
]