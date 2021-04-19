from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from src.banks.models import Bank
from .forms import CreateOperationForm
from .models import OperationCategory

@login_required(login_url='login')
def create_operation(request):
    if request.method == 'POST':
        data = request.POST
        form = CreateOperationForm(data)
        if form.is_valid():
            operation = form.save(commit=False)
            if operation.type == '-' and operation.bank.balance < operation.amount:
                messages.error(request, f'На вашем {operation.bank.name} не хватает денег.')
                return redirect('create-operation')
            operation.user = request.user
            operation.save()

            operation.bank.operate(operation.type, operation.amount)

            messages.success(request, f'Операция успешно добавлена.')
            return redirect('home')
        else:
            messages.error(request, form.errors)
            

    banks = Bank.objects.filter(owner=request.user)
    categories = OperationCategory.objects.all()
    return render(request, 'debts/create_operation.html', {
        'form': CreateOperationForm(),
        'banks': banks,
        'categories': categories
    })