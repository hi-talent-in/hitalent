from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request, path=None):
    return render(request, 'frontend/index.html')