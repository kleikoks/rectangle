from os import name
from django.urls import path
from .views import *


urlpatterns = [
    path('get_available_text', get_available_text, name='get_available_text')
]
