from django.urls import path
from shorterurl.views import ShortUrlHome

urlpatterns = [
    path('', ShortUrlHome.as_view(), name='home'),
]
