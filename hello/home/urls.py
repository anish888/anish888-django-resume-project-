from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   #adding path of the index function
    path('about',views.about,name='home'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('home',views.home,name='home'),
    path('',views.home,name='home')
]
