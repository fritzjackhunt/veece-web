from django.urls import path
from . import views

urlpatterns = [
    path('coming-soon', views.home, name='homepage'),
    path('privacyPolicy', views.privacyPolicy, name='privacy-policy'),
    path('help', views.help, name='help'),
    path('', views.coming_soon, name='coming-soon'),
]