from django.urls import path
from .views import *

urlpatterns = [
    path('list_waste_util/', list_waste_util, name='list_waste_util'),
    path('detail_waste_util/<pk>/', detail_waste_util, name='detail_waste_util'),
    path('create_waste_util_review/', create_waste_util_review, name='create_waste_util_review'),
]
