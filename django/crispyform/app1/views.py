from django.shortcuts import render,redirect
from .forms import EquipForm,MessageForm

# Create your views here.
def equip(request):
    form = EquipForm(request.POST)
    if form.is_valid():
            form.save()
            #return redirect('equip.html')
    return render(request, 'app1/equip.html', {'form': form})


def index(request):
      form=MessageForm(request.POST)

      return render(request, 'app1/index.html',{'form':form})