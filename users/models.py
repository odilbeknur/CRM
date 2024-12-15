from django.contrib.auth.models import User
from django.db import models

# Role Model
class Role(models.Model):
    SYSTEM_USER_CHOICES = [
        ('admin', 'Администратор'),
        ('employee', 'Сотрудник'),
    ]

    position = models.CharField(max_length=100, verbose_name="Должность")
    system_user = models.CharField(
        max_length=50, choices=SYSTEM_USER_CHOICES, verbose_name="Тип системного пользователя"
    )

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
        indexes = [
            models.Index(fields=["system_user"]),
        ]

    def __str__(self):
        return self.position


# Person Model
class Person(models.Model):
    SEX_CHOICES = [
        ('male', 'Мужчина'),
        ('female', 'Женщина'),
    ]

    first_name = models.CharField(max_length=50, verbose_name="Имя", db_index=True)
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", db_index=True)
    nickname = models.CharField(max_length=50, null=True, blank=True, verbose_name="Прозвище")
    sex = models.CharField(
        max_length=10, choices=SEX_CHOICES, null=True, blank=True, verbose_name="Пол"
    )
    phone_number_1 = models.CharField(max_length=20, unique=True, verbose_name="Телефон 1")
    phone_number_2 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон 2")

    class Meta:
        verbose_name = "Личность"
        verbose_name_plural = "Личности"
        indexes = [
            models.Index(fields=["first_name"]),
            models.Index(fields=["last_name"]),
        ]
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name', 'phone_number_1'], name="unique_person")
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Employee Model
class Employee(models.Model):
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="employees", verbose_name="Личность"
    )
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, related_name="employees", verbose_name="Роль"
    )
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="employee", verbose_name="Пользователь"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        indexes = [
            models.Index(fields=["role"]),
        ]

    def __str__(self):
        return f"{self.person} - {self.role} - {'No User' if not self.user else self.user.username}"

class Client(models.Model):
    CLIENT_TYPE_CHOICES = [
        ('g', 'Государственный'),
        ('b', 'Бизнес'),
        ('f', 'Физическое лицо'),
    ]

    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="clients", verbose_name="Личность"
    )
    type = models.CharField(
        max_length=1, choices=CLIENT_TYPE_CHOICES, verbose_name="Тип клиента"
    )
    fin_account = models.IntegerField(
        null=True, blank=True, verbose_name="Финансовый аккаунт"
    )  # Теперь это поле необязательно

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        indexes = [
            models.Index(fields=["type"]),
        ]

    def __str__(self):
        return f"{self.person} ({self.get_type_display()})"


                          