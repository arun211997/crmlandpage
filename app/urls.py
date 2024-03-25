from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',views.land,name='land'),
     path('dashboard',views.dashboard,name='dashboard'),
]
