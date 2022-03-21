# from multiprocessing import context
# from tokenize import group
# from unicodedata import name
# from django.contrib.auth.models import Group, User
from multiprocessing import context
from django.shortcuts import render,redirect

def dashbo(request):
    context={}
    return render(request,'dashboard.html',context)
def homePage(request):
    context={}
    return render(request,'home.html',context)