from django import forms
from django.core.exceptions import ValidationError
from .models import Ticket, Person, Client, Stage

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

    class Meta:
        model = Ticket
        fields = [
            "client_first_name",
            "client_last_name",
            "client_phone_number_1",
            "description",
            "ads_info",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def save(self, commit=True):
        """
        Override save to automatically create the client if it doesn't exist.
        """
        first_name = self.cleaned_data.get("client_first_name")
        phone_number_1 = self.cleaned_data.get("client_phone_number_1")
        gender = self.cleaned_data.get("gender")

        # Ensure required fields are filled
        if not first_name or not phone_number_1:
            raise ValidationError("Необходимо заполнить обязательные поля.")

        client = self.get_or_create_client(
            first_name,
            self.cleaned_data.get("client_last_name", ""),
            gender,
            phone_number_1
        )
        self.instance.client = client

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
