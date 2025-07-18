from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(form.cleaned_data['password'])
            user.save()

            token = get_random_string(32)
            request.session['email_verification_token'] = token
            request.session['user_id'] = user.id

            current_site = get_current_site(request)
            subject = 'Verify your email'
            message = render_to_string('verify_email.html', {
                'domain': current_site.domain,
                'uid': user.id,
                'token': token
            })

            send_mail(subject, message, 'admin@example.com', [user.email])
            return render(request, 'check_email.html')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def verify_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if request.session.get('email_verification_token') == token:
        user.is_active = True
        user.save()
        del request.session['email_verification_token']
        return redirect('login')
    return HttpResponse('Invalid or expired token.')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                request.session['username'] = user.username
                return redirect('home')
        messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html', {'username': request.session.get('username')})