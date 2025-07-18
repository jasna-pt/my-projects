from django.urls import path
from . import views
urlpatterns =[path("",views.index,name='home'),
              path("about/",views.about,name='about'),
              path("contact/",views.contact,name='contact'),
              path("services/",views.services,name='services'),
              path("view/",views.contact_view,name='contact_view'),

              
              ]
