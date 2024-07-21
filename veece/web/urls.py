from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('privacyPolicy', views.privacyPolicy, name='privacy-policy'),
]