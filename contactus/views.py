# contactus/views.py
from django.shortcuts import render

def contact(request):
    return render(request, 'contactus/contact.html')
