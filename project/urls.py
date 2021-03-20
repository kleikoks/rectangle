from os import name
from django.urls import path
from .views import *

serializer_routes = [
    path('book_list', book_list, name='book_list')
]

urlpatterns = [
    path('set_lang/<lang>', set_lang, name='set_lang')
] + serializer_routes
