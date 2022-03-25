# from multiprocessing import context
# from tokenize import group
# from unicodedata import name
# from django.contrib.auth.models import Group, User
from email import message
from multiprocessing import context
from django.contrib import messages
import django
from django.dispatch import receiver
from django.shortcuts import render,redirect
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import  Profile
from .forms import UpdateProfileForm
from django.contrib.auth.models import User

@login_required
def dashbo(request):
    context={}
    return render(request,'dashboard.html',context)

def homePage(request):
    context={}
    return render(request,'home.html',context)


#refer this https://dev.to/earthcomfy/django-user-profile-3hik to create profile 
# below function in basic 
# @login_required
# def profile(request):
#     # profiles = Profile.objects.all()
#     # context={'profiles':profiles}
#     return render(request,'profile.html')   
#below one actual function
@login_required
def profile(request,pk):
    user = User.objects.get(id=pk)
    userDetails = Profile.objects.all()
    context={'user':user}
    return render(request,'profile.html',context)
@login_required
def update(request):
    # user=request.user
    # profile_form=UpdateProfileForm(instance=user)
    # profile = Profile.objects.filter(user=request.user)
    try:
      profile = request.user.profile
    except Profile.DoesNotExist:
      profile = Profile.objects.create(user=request.user)
    if request.method == 'POST':
        
            

            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request,'PROFILE UPDATED SUCCESSFULLY')
                user=request.user
                return redirect('users-profile',pk=user.id)
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context={'profile_form':profile_form}
    return render(request,'update_user.html',context)
    
    
        
    
  
