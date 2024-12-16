from django import forms
from .models import Product, Measurement

# Форма для Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'type', 'color', 'material']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название продукции'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Название продукции',
            'type': 'Тип продукции',
            'color': 'Цвет продукции',
            'material': 'Материал продукции',
        }


# Форма для Measurement
class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['ticket', 'product', 'height', 'width', 'description', 'photo']
        widgets = {
            'ticket': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'width': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'ticket': 'Заявка',
            'product': 'Продукция',
            'height': 'Высота',
            'width': 'Ширина',
            'description': 'Описание',
            'photo': 'Фото',
        }
