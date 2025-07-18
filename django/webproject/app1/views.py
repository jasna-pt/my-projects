
from django.shortcuts import render

# New view for the about page
def about(request):
    return render(request, 'app1/about.html')

# New view for the contact page
def contact(request):
    return render(request, 'app1/contact.html')



# Create your views here.
def index(request):
    return render(request,'app1/index.html')
