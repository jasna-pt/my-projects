from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from .models import Book, IssueRecord, Member
from .forms import BookForm, IssueForm, RegisterForm
from django.contrib.auth.models import User
from django.utils import timezone

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

@login_required
def issue_book(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            member, _ = Member.objects.get_or_create(user=request.user)
            issue.member = member
            issue.save()
            return redirect('book_list')
    else:
        form = IssueForm()
    return render(request, 'library/issue_book.html', {'form': form})

@login_required
def return_book(request, pk):
    record = get_object_or_404(IssueRecord, pk=pk, member__user=request.user)
    record.return_date = record.return_date or timezone.now().date()
    record.save()
    return redirect('book_list')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Member.objects.create(user=user)
            login(request, user)
            return redirect('book_list')
    else:
        form = RegisterForm()
    return render(request, 'library/register.html', {'form': form})

def issue_book(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            if book.available_quantity < 1:
                return HttpResponse("Book is not available", status=400)

            issue = form.save(commit=False)
            member, _ = Member.objects.get_or_create(user=request.user)
            issue.member = member
            issue.save()

            book.available_quantity -= 1
            book.save()

            return redirect('book_list')
    else:
        form = IssueForm()
    return render(request, 'library/issue_book.html',{'form': form})

from django.utils import timezone

def return_book(request, pk):
    record = get_object_or_404(IssueRecord, pk=pk, member__user=request.user)
    if not record.return_date:
        record.return_date = timezone.now().date()
        record.book.available_quantity += 1
        record.book.save()
        record.save()
    return redirect('book_list')

def logout_view(request):
    logout(request)
    return redirect('login')
