from django.urls import path
from .views import register_view, login_view, logout_view, home_view, verify_email,home_view1

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('verify/<int:uid>/<str:token>/', verify_email, name='verify_email'),
    path('', home_view, name='home'),
    path('demo/', home_view1, name='home1'),
]
from django.contrib.auth import views as auth_views

urlpatterns += [
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
