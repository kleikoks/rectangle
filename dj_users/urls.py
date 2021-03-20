from django.urls import path 

from . views import *
urlpatterns = [
    path('home/', home,name='home'),
    path('accounts/login/', login, name='login'),
    path('accounts/register/', register, name='register'),
    path('accounts/logout/', logout, name='logout')
]
