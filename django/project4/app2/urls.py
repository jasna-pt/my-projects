from django.contrib import admin
from django.urls import path
from . import views
from .views import Fun

urlpatterns = [
    
    path("abc/",views.abc,name="abc"),
    path("home/",Fun.as_view(),name="home"),
    
    
]