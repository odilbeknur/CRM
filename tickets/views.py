from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model, login
from django.core.exceptions import ValidationError
from .models import Ticket, Stage, StageHistory
from .forms import TicketForm

User = get_user_model()

# Список заявок

class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'  # Имя контекста для шаблона
    ordering = ['-created_at']  # Сортировка по дате создания
    paginate_by = 10  # Количество элементов на страницу

# Создание заявки
@login_required
def ticket_create_view(request):
    if not request.user.employee:  # Check if user has an associated Employee
        return redirect('some_error_page')  # Redirect to an appropriate error page

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.assigned_employee = request.user.employee  # Assign the authenticated user's employee
            
            # Set default status as "Новая"
            ticket.status = "Новая"
            
            ticket.save()

            # Create StageHistory with default Stage 'Звонок'
            stage, created = Stage.objects.get_or_create(name='Звонок')
            StageHistory.objects.create(
                ticket=ticket,
                stage=stage,
            )

            return redirect(reverse_lazy('tickets:ticket_list'))
    else:
        form = TicketForm()

    return render(request, 'tickets/ticket_form.html', {'form': form})


# Редактирование заявки
class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('tickets:ticket_list')  # после успешного редактирования перенаправление на список заявок

# Удаление заявки
class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'tickets/ticket_confirm_delete.html'
    success_url = reverse_lazy('tickets:ticket_list')
