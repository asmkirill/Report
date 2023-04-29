from django.urls import path
from . import views
from .views import register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register, name='register'),
    path('login', views.custom_login, name='login'),
    #path('logout', views.custom_logout, name='logout'), --- for messaging type logOut with No logOut page
    #path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]