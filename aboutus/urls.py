# aboutus/urls.py
from django.urls import path
from . import views

app_name = 'aboutus'

urlpatterns = [
    path('about/', views.about, name='about'),
]
