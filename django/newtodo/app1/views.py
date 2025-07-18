from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import ToDoList,ToDoItem


class TodoListView(ListView):
    model = ToDoList
    template_name = "app1/index.html"

class ItemListView(ListView):
    model= ToDoItem
    template_name="app1/todo_item.html"

def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context