from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from slugify import slugify

from src.debts.models import Operation
from .models import Bank
from .forms import CreateBankForm




@login_required(login_url='login')
def home(request):
    user = request.user
    user_banks = Bank.objects.filter(owner=user).order_by('-created_at')
    user_operations = Operation.objects.filter(user=user).order_by('-date')

    context = {
        'banks': user_banks,
        'operations': user_operations
    }

    return render(request, 'home.html', context)


@login_required(login_url='login')
def create_bank(request):
    if request.method == 'POST':
        data = request.POST
        form = CreateBankForm(data)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.owner = request.user
            bank.slug = slugify(bank.name)
            try:
                bank.save()
                messages.success(request, f'Счет с названием {bank.name} успешно создан.')
                return redirect('home')
            except IntegrityError:
                messages.error(request, f'Извините у вас уже есть счет с таким названием.')
        else:
            messages.error(request, form.errors)
    return render(request, 'banks/create_bank.html')

@login_required(login_url='login')
def create_operation(request):
    if request.method == 'POST':
        data = request.POST
        form = CreateBankForm(data)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.owner = request.user
            bank.slug = slugify(bank.name)
            try:
                bank.save()
                messages.success(request, f'Счет с названием {bank.name} успешно создан.')
                return redirect('home')
            except IntegrityError:
                messages.error(request, f'Извините у вас уже есть счет с таким названием.')
        else:
            messages.error(request, form.errors)
    return render(request, 'banks/create_bank.html')