from dj_users.forms import UserLoginForm, UserRegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout


@login_required
def home(request):
    return render(request, 'dj_users/home.html', locals())

def login(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        user
        _login(request, user)
        if next:
            return redirect(next)
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'dj_users/login.html', context)

def register(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        _login(request, new_user)
        if next:
            return redirect(next)
        return redirect('')

    context = {
        'form': form
    }
    return render(request, 'dj_users/signup.html', context)

def logout(request):
    _logout(request)
    return redirect('home')