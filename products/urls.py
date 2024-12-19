from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'), 
    path('create/', views.product_create, name='create'), 
    path('<int:pk>/', views.product_detail, name='detail'),  
    path('<int:pk>/edit/', views.product_edit, name='edit'),  
    path('measurements/create/', views.measurement_create, name='measurement_create'),
    path('measurements/edit/<int:pk>/', views.measurement_edit, name='measurement_edit'),
    path('measurements/', views.measurement_list, name='measurement_list'),
]