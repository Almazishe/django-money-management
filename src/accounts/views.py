from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages


from .forms import RegisterForm



def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account was created\nPlease log in...")
            return redirect('login')
        else:
            messages.error(request, f"{form.errors}")

    return render(request, 'auth/registration.html')



def login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login success!')
            return redirect('home')
        else:
            messages.info(request, 'Usename or password incorrect!')
            return render(request, 'auth/login.html', context)

    return render(request, 'auth/login.html', context)


def logout(request):
    auth_logout(request)
    return  redirect('login')