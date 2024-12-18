from django.shortcuts import render, redirect
from .forms import FinanceForm
from .models import Finance

def create_finance(request):
    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance_success')  
    else:
        form = FinanceForm()
    return render(request, 'finance/finance_form.html', {'form': form, 'section':'finance'})

def finance_list(request):
    finances = Finance.objects.select_related('ticket').all()
    return render(request, 'finance/finance_list.html', {'finances': finances, 'section':'finance'})