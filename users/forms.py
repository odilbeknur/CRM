from django import forms
from .models import Employee


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['person', 'role', 'user']
        widgets = {
            'person': forms.Select(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }