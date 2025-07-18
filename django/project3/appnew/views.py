from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def new(request):
    return HttpResponse("A NEW APP IS DEVELOPED,THANKYOU")
def new1(request):
    name="ezrin"
    return render(request,"index.html",{"name":name})
def new2(request):
    name="jasna"

    return render(request,"abc.html",{"name":name})

class Index(View):
    def get(self,request):
        return render(request,"index.html",{})

class Abc(View):
    def get(self,request):
        return render(request,"abc.html",{})