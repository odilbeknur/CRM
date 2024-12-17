# from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

app_name = "users"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', views.user_login, name='login'),
    path('clients/', views.list_clients, name='client_list'),
    path('employees/', views.list_employee, name='list_employee'),

]