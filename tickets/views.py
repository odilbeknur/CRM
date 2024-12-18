from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model, login
from django.core.exceptions import ValidationError
from .models import Ticket, Stage, StageHistory
from .forms import TicketForm
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

# Список заявок

def index_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user.employee  # Assign the authenticated user's employee
            
            # Set default status as "Новая"
            ticket.status = "Новая"
            
            ticket.save()

            # Create StageHistory with default Stage 'Звонок'
            stage, created = Stage.objects.get_or_create(name='Звонок')  # Получаем только Stage
            StageHistory.objects.create(
                ticket=ticket,
                stage=stage,  # Используем только экземпляр Stage
            )

            return redirect(reverse_lazy('tickets:index_view'))  # Перенаправление после сохранения
    else:
        form = TicketForm()

    return render(
        request,
        'tickets/index.html',
        {
            'form': form,  # Передача формы в шаблон
            'stages': Stage.objects.all(),
            'tickets': Ticket.objects.all(),
            'section': 'index',
        }
    )

def ticket_list_view(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    stages = Stage.objects.all()  # Получаем все стадии

    context = {
        'tickets': tickets,
        'stages': stages,
        'section': 'tickets',

    }

    return render(request, 'tickets/ticket_list.html', context)

# Создание заявки
@login_required
def ticket_create_view(request):
    if not request.user.employee:  # Check if user has an associated Employee
        return redirect('some_error_page')  # Redirect to an appropriate error page

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user.employee  
            
            ticket.status = "Новая"
            
            ticket.save()

            stage, created = Stage.objects.get_or_create(name='Звонок')
            StageHistory.objects.create(
                ticket=ticket,
                stage=stage,
            )

            return redirect(reverse_lazy('tickets:ticket_list'))
    else:
        form = TicketForm()

    return render(request, 'tickets/ticket_form.html', {'form': form, 'section': 'tickets'})


@login_required
def update_ticket_status(request, ticket_id):
    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, id=ticket_id)

        new_status = request.POST.get('status')

        if new_status in dict(ticket.STATUS_CHOICES):
            ticket.status = new_status
            ticket.save()  
            return redirect('tickets:ticket_list')  
        else:
            return HttpResponseBadRequest("Неверный статус")  
    else:
        return HttpResponseBadRequest("Метод не поддерживается")


@login_required
def ticket_update_stage(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        new_stage_id = request.POST.get('stage')
        new_stage = get_object_or_404(Stage, id=new_stage_id)
        
        # Create a new StageHistory entry
        StageHistory.objects.create(
            ticket=ticket,
            stage=new_stage,
        )
        
        return redirect(reverse('tickets:ticket_list'))
    
    return redirect(reverse('tickets:ticket_list'))

@login_required
def ticket_update_stage_perform(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        new_stage_id = request.POST.get('stage')
        new_stage = get_object_or_404(Stage, id=new_stage_id)
        
        # Create a new StageHistory entry
        StageHistory.objects.create(
            ticket=ticket,
            stage=new_stage,
        )
        
        return redirect(reverse('tickets:ticket_list'))
    
    return redirect(reverse('tickets:ticket_list'))
    
# Редактирование заявки
def ticket_update_view(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)  # Получаем объект заявки по pk
    form = TicketForm(instance=ticket)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('tickets:ticket_list'))

    context = {
        'form': form,
        'ticket': ticket,
        'section': 'tickets',
    }
    return render(request, 'tickets/ticket_form.html', context)

# Удаление заявки
def ticket_delete_view(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)  # Получаем объект заявки по pk

    if request.method == 'POST':
        ticket.delete()
        return redirect(reverse_lazy('tickets:ticket_list'))

    context = {
        'ticket': ticket,
        'section': 'tickets',
    }
    return render(request, 'tickets/ticket_confirm_delete.html', context)

