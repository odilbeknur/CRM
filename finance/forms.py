from django import forms
from .models import Finance

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['ticket', 'transaction', 'full_cost', 'remain', 'sum']
        widgets = {
            'ticket': forms.Select(attrs={'class': 'form-control'}),
            'transaction': forms.TextInput(attrs={'class': 'form-control'}),
            'full_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'remain': forms.NumberInput(attrs={'class': 'form-control'}),
            'sum': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'ticket': 'Заявка',
            'transaction': 'Счет фактура',
            'full_cost': 'Полная стоимость',
            'remain': 'Остаток',
            'sum': 'Сумма',
        }
