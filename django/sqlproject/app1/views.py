from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog_list(request):
    blogs=Blog.objects.all()

    return render(request, 'app1/blog_list.html', {'blogs': blogs})
