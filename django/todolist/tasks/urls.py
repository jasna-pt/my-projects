
from django.urls import path
#from.views import Tasklist,Taskview,Detail,ListCreate,ListUpdate
from . import views
'''
urlpatterns = [path("",views.task_list,name="task_list"),
               path("abc/",views.Taskview,name="Taskview"),
               path('abc/<int:id>/',views.Taskdetails,name="taskdetails"),]
'''
'''''
urlpatterns=[path("",Tasklist.as_view(),name="Tasklist"),
             path("jas/",Taskview.as_view(),name='jas'),
             path("abc/<int:id>/",Detail.as_view(),name='abc'),
             path("creat/",ListCreate.as_view(),name='creat'),
             path("<int:pk>/edit/",ListUpdate.as_view(),name='update'),]
'''
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('register/', views.register, name='register'),
]
