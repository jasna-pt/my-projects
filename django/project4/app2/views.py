from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from.models import Xyz


# Create your views here.
class Fun(View):
    def get(self, request):
        datas=Xyz.objects.all()
        context={"values":datas}
        return render(request,"jasna.html",context)

def abc(request):
    datas=Xyz.objects.all()
    context={"values":datas}

    return render(request,'jasna.html',context)
                                  