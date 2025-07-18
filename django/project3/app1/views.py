from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def abs(request):
    return HttpResponse("hello guys ,good morning")
