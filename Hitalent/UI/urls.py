from unicodedata import name
from django.urls import path,include

from . import views

urlpatterns = [
    #path('login/',views.loginPage,name='login'),
    path('dashboard/',views.dashbo,name='dashboard'),
    path('',views.homePage,name='home'),
    path('profile/<str:pk>', views.profile, name='users-profile'),
    path('update-user',views.update,name='update-user'),
    path('accounts/',include('allauth.urls')),
    

    
]