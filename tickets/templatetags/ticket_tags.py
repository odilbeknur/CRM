from django import template
from django.db.models import Count

from ..models import Employee

register = template.Library()

@register.simple_tag
def get_all_employees():
    return Employee.objects.all()