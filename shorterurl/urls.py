from django.urls import path
from shorterurl.views import ShortUrlHome, redirect_url_view, my_history_url

urlpatterns = [
    path('', ShortUrlHome.as_view(), name='home'),
    path('history/', my_history_url, name='history'),
    path('<str:short_part>', redirect_url_view, name='redirect'),
]
