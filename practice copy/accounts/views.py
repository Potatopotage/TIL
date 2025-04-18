from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user
from .forms import CustomerChangeForm, CustomerCreationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomerCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = CustomerChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomerChangeForm(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/user_update.html', context)


def delete(request):
    request.user.delete()
    return redirect('articles:index')