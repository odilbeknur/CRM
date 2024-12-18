from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.ticket_list_view, name='ticket_list'),
    path('create/', views.ticket_create_view, name='ticket_create'),
    path('index/', views.index_view, name='index_view'),
    path('tickets/<int:pk>/edit/', views.ticket_update_view, name='ticket_edit'),
    path('tickets/<int:pk>/delete/', views.ticket_delete_view, name='ticket_delete'),
    path('<int:ticket_id>/update_stage/', views.ticket_update_stage, name='ticket_update_stage'),
    path('<int:ticket_id>/update_status/', views.update_ticket_status, name='ticket_update_status'),
]
    