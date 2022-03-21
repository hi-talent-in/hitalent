from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    #path('login/',views.loginPage,name='login'),
    path('dashboard/',views.dashbo,name='dashboard'),
    path('',views.homePage,name='home')
    
]