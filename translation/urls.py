from os import name
from django.urls import path
from .views import set_lang


urlpatterns = [
    path('set_lang/<lang>', set_lang, name='set_lang')
]
