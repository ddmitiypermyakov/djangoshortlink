from django.urls import path
from shorterurl.views import ShortUrlHome, redirect_url_view

urlpatterns = [
    path('', ShortUrlHome.as_view(), name='home'),
    path('<str:short_part>', redirect_url_view, name='redirect'),
]
