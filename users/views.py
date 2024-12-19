from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import (
    LoginForm,
    EmployeeForm
)
from .models import Client, Employee


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def list_clients(request):
    clients = Client.objects.all()  # Get all clients
    return render(request, 'users/client_list.html', {'clients': clients, 'section': 'clients'})

def list_employee(request):
    employees = Employee.objects.all()  # Get all clients
    return render(request, 'users/employees_list.html', {'employees': employees, 'section': 'employees'})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:list_employee')  # Redirect to an employee list or another page
    else:
        form = EmployeeForm()
    return render(request, 'users/employee_form.html', {'form': form , 'section': 'employees'})