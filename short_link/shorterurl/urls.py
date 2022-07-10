from django.urls import path
from shorterurl.views import index

urlpatterns = [
    path('', index, name='home'),
]
