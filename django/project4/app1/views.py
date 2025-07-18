from django.shortcuts import render
from django.http import HttpResponse
from .models import Jas

# Create your views here.
def xyz(request):
    return HttpResponse("hellooo,how are you")

def index(request):
    datas=Jas.objects.all()
    context={"datas":datas}

    return render(request, 'index.html',context)