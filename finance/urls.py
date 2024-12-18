from django.urls import path
from .views import *

app_name='finance'

urlpatterns = [
    path('create/', create_finance, name='create_finance'),
    path('', finance_list, name='finance_list'),
]