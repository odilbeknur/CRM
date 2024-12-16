from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.TicketListView.as_view(), name='ticket_list'),
    path('create/', views.ticket_create_view, name='ticket_create'),
    path('<int:pk>/edit/', views.TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/delete/', views.TicketDeleteView.as_view(), name='ticket_delete'),
]
    