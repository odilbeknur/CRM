from django.db import models
from tickets.models import Ticket  # Импорт модели Ticket

class Finance(models.Model):

    ticket = models.ForeignKey(
        Ticket, 
        on_delete=models.CASCADE, 
        related_name="payments",
        verbose_name="Заявка"
    )
    transaction = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Счет фактура"
    )
    full_cost = models.FloatField(
        verbose_name="Полная стоимость"
    )
    remain = models.FloatField(
        verbose_name="Остаток"
    )
    sum = models.FloatField(
        verbose_name="Сумма"
    )
    created_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Транзакция {self.transaction} для Заявки {self.ticket.id}"
