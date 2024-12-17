from django.db import models
from django.utils import timezone
from users.models import Employee, Client, Person



# Основная модель Заявки
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
    ]

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="tickets", verbose_name="Клиент"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус заявки"
    )
    created_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, related_name="created_tickets",
        verbose_name="Создатель заявки"
    )
    assigned_employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, related_name="assigned_tickets",
        verbose_name="Назначенный сотрудник"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["assigned_employee"]),
        ]

    def __str__(self):
        return f"Заявка {self.id} для {self.client}"


# Этапы (справочник)
class Stage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название этапа")
    priority = models.PositiveIntegerField(verbose_name="Приоритет этапа", null=True, blank=True,)

    class Meta:
        verbose_name = "Этап"
        verbose_name_plural = "Этапы"
        ordering = ["priority"]

    def __str__(self):
        return f"{self.name} (Приоритет: {self.priority})"


# История этапов выполнения заявки
class StageHistory(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="stage_history", verbose_name="Заявка"
    )
    stage = models.ForeignKey(
        Stage, on_delete=models.CASCADE, related_name="stage_histories", verbose_name="Этап"
    )
    started_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата начала этапа")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата завершения")
    performed_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, related_name="stage_histories",
        verbose_name="Ответственный сотрудник"
    )

    class Meta:
        verbose_name = "История этапов"
        verbose_name_plural = "История этапов"
        indexes = [
            models.Index(fields=["ticket", "stage"]),
        ]

    def __str__(self):
        return f"Этап '{self.stage}' для заявки {self.ticket.id} (Начат: {self.started_at}, Завершен: {self.completed_at})"
    # def save(self, *args, **kwargs):
    #     # Проверка начала этапа
    #     if not self.started_at:
    #         self.started_at = timezone.now()

    #     # Проверка завершения этапа
    #     if self.completed_at and self.completed_at <= self.started_at:
    #         raise ValueError("Дата завершения должна быть позже даты начала этапа")

    #     # Проверка перехода на следующий этап (порядок этапов)
    #     if self.pk:  # Если это не новый объект
    #         last_stage_history = StageHistory.objects.filter(
    #             ticket=self.ticket
    #         ).exclude(pk=self.pk).order_by('-completed_at').first()
            
    #         if last_stage_history and last_stage_history.stage.priority >= self.stage.priority:
    #             raise ValueError("Этап не может быть завершен до перехода на следующий этап.")

    #     super().save(*args, **kwargs)
