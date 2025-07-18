from django.urls import path
from . import views


urlpatterns=[path("",views.equip,name='form'),
             path("message/",views.index,name='message')]