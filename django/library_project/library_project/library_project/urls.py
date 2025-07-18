from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from library_project import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='library/login.html'), name='login'),
    #path('accounts/logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('', include('library.urls')),
]
