from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.TicketListView.as_view(), name='ticket_list'),
    path('create/', views.ticket_create_view, name='ticket_create'),
    path('index/', views.index_view, name='index_view'),
    path('<int:pk>/edit/', views.TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/delete/', views.TicketDeleteView.as_view(), name='ticket_delete'),
    path('<int:ticket_id>/update_stage/', views.ticket_update_stage, name='ticket_update_stage'),
    path('<int:ticket_id>/update_status/', views.update_ticket_status, name='ticket_update_status'),
]
    