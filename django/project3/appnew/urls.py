
from django.urls import path
from .views import Index,Abc
from . import views
urlpatterns = [
    path("",views.new,name="new"),
    path("login/",views.new1,name="new1"),
    path("newlog/",views.new2,name="new2"),
    path("logout/",Index.as_view(),name="logout"),
    path("jas/",Abc.as_view(),name="jas"),
    
]