from django.urls import path
from . import views
from .views import register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('blocked_page/', views.blocked_page, name='blocked_page'),
    path('register/', register, name='register'),
    path('login', views.custom_login, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/<username>', views.profile, name='profile'),
]