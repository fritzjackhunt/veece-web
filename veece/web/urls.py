from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('coming-soon', views.home, name='homepage'),
    path('privacyPolicy', views.privacyPolicy, name='privacy-policy'),
    path('help', views.help, name='help'),
]