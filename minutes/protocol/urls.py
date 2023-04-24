from django.urls import path
from . import views


urlpatterns = [
    path('create_protocol/', views.create_protocol, name='create_protocol'),
]