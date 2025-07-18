from django.shortcuts import render
from .forms import InputForm,TeamMemberForm,AdmissionForm
from .models import TeamMember,Admission
from .forms import ContactForm
# Create your views here.
def index(request):
    form=AdmissionForm(request.POST or None)
    if form.is_valid():
         form.save()
    return render(request, 'app1/index.html',context={'form':form})

def about(request):
    form=TeamMemberForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'app1/about.html',context={'form':form})

def contact(request):
    form=InputForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'app1/contact.html',context={'form':form})

def services(request):
    return render(request, 'app1/services.html')


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
            form.save()
    return render(request, 'app1/services.html', {'forms': form})











    