from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path("abc/",views.xyz,name="xyz"),
path("appdata/",views.index,name="index"),
    
    
    
]