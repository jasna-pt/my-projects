from django.shortcuts import render,redirect
from.models import Task
from.forms import TaskForm
from django.views import View
from rest_framework import viewsets
from django.views.generic import ListView
# Create your views here.
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
'''
def task_list(request):
    
    form=TaskForm(request.POST)
    if  form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'tasks/tasks.html', {'form': form})

def Taskview(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_view.html', {'tasks': tasks})

def Taskdetails(request,id):
    taskdetails=Task.objects.get(id=id)
    return render(request,'tasks/taskdetails.html',{'tasksdetails': taskdetails})

'''
'''
class Tasklist(View):
    def get(self,request):
        form=TaskForm(request.POST)
        return render(request,"tasks/tasks.html",{'form': form})
    '''

'''
class Tasklist(ListView):
    model=Task
    template_name="tasks/task_view.html"

class ListCreate(CreateView):
    model = Task
    fields = ["title","description"]

class ListUpdate(UpdateView):
    model = Task
    form_class=TaskForm
    template_name="tasks/task_edit.html"
    success_url='/'

class Taskview(View):
    def get(self,request):
        tasks = Task.objects.all()
        return render(request,"tasks/task_view.html",{'tasks': tasks})  

class Detail(View):
    def get(self,request,id):
        taskdetails=Task.objects.get(id=id)
        return render(request,"tasks/taskdetails.html",{'tasksdetails': taskdetails})      


from .serializers import TaskSerializer
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer        
    '''


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_view.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/tasks.html',{'form':form})