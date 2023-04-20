from django.urls import path
from .views import create_protocol


urlpatterns = [
    path('create_protocol/', create_protocol, name='create_protocol'),
]