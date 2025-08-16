# contactus/urls.py
from django.urls import path
from . import views

app_name = 'contactus'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
