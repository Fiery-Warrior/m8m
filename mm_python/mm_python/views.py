#created this views.py in root directory for connecting with react, aka frontend 
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')