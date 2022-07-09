from django.urls import path
from accounts.views import AuthUserLogin, index

urlpatterns = [
    path('',index, name= 'home'),
    path('login/', AuthUserLogin.as_view(), name="login"),
]