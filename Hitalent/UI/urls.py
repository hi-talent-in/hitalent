
from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),

    path('',views.homePage,name='home'),
    path('accounts/',include('allauth.urls')),
    path('dashboard/',views.dashbo,name='dashboard'),
    # path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('update-user',views.update,name='update-user'),
    path('profile/<str:pk>/',views.profile,name='user-profile')




]

