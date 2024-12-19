from django import forms
from django.core.exceptions import ValidationError
from .models import Ticket, Person, Client
from locations.models import Location


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TicketForm(forms.ModelForm):
    client_first_name = forms.CharField(
        max_length=50,
        required=True,
        label="Имя клиента",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    client_last_name = forms.CharField(
        max_length=50,
        required=False,
        label="Фамилия клиента",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    client_gender = forms.ChoiceField(
        choices=Person.GENDER_CHOICES,  
        label="Пол клиента",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    client_phone_number_1 = forms.CharField(
        max_length=20,
        required=True,
        label="Телефон клиента",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    ads_info = forms.ChoiceField(
        choices=Ticket.ADS_CHOICES,  
        label="Источник рекламы",
        widget=forms.Select(attrs={"class": "form-control"}),  
    )
    # Поля для локации
    city = forms.CharField(
        max_length=100, required=True, label="Город",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    district = forms.CharField(
        max_length=100, required=False, label="Район",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    street = forms.CharField(
        max_length=100, required=True, label="Улица",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    apartment = forms.IntegerField(
        required=False, label="Квартира",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    entrance = forms.IntegerField(
        required=False, label="Подъезд",
        widget=forms.NumberInput(attrs={"class": "form-control"})   
    )
    floor = forms.IntegerField(
        required=False, label="Этаж",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    landmark = forms.CharField(
        max_length=20, required=False, label="Ориентир",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Ticket
        fields = [
            "client_first_name",
            "client_last_name",
            "client_gender",
            "client_phone_number_1",
            "description",
            "ads_info",
            "city",
            "district",
            "street",
            "apartment",
            "entrance",
            "floor",
            "landmark",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def save(self, commit=True):
        """
        Override save to automatically create the client if it doesn't exist.
        """
        first_name = self.cleaned_data.get("client_first_name")
        last_name = self.cleaned_data.get("client_last_name", "")
        phone_number = self.cleaned_data.get("client_phone_number_1")
        gender = self.cleaned_data.get("client_gender")

        # Создаём клиента
        client = self.get_or_create_client(first_name, last_name, gender, phone_number)
        self.instance.client = client

        # Создаём локацию
        location = Location.objects.create(
            city=self.cleaned_data.get("city"),
            district=self.cleaned_data.get("district"),
            street=self.cleaned_data.get("street"),
            apartment=self.cleaned_data.get("apartment"),
            entrance=self.cleaned_data.get("entrance"),
            floor=self.cleaned_data.get("floor"),
            landmark=self.cleaned_data.get("landmark"),
        )
        self.instance.location = location

        return super().save(commit=commit)

    @staticmethod
    def get_or_create_client(first_name, last_name, gender, phone_number):
        
        """
        Get or create a client by first name, last name, and phone number.
        """
        person, _ = Person.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            phone_number_1=phone_number,
        )
        client, _ = Client.objects.get_or_create(
            person=person,
            defaults={"type": "f"},  
        )
        return client

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['client', 'description', 'ads_info', 'status']
        labels = {
            'client': 'Клиент',
            'description': 'Описание',
            'ads_info': 'Источник рекламы',
            'status': 'Статус',
        }
        widgets = {
            'client': forms.Select(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control", "rows": 3}),  
            'ads_info': forms.Select(attrs={"class": "form-control"}),  
            'status': forms.Select(attrs={"class": "form-control"}),  
        }