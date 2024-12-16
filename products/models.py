from django.db import models
from tickets.models import Ticket
from django.urls import reverse


# Product Model
class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('type1', 'Тип 1'),
        ('type2', 'Тип 2'),
    ]

    COLOR_CHOICES = [
        ('red', 'Красный'),
        ('blue', 'Синий'),
        ('green', 'Зеленый'),
    ]

    MATERIAL_CHOICES = [
        ('metal', 'Металл'),
        ('plastic', 'Пластик'),
        ('wood', 'Дерево'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название продукции")
    type = models.CharField(
        max_length=20, choices=PRODUCT_TYPE_CHOICES, verbose_name="Тип продукции"
    )
    color = models.CharField(
        max_length=20, choices=COLOR_CHOICES, verbose_name="Цвет продукции"
    )
    material = models.CharField(
        max_length=20, choices=MATERIAL_CHOICES, verbose_name="Материал продукции"
    )

    class Meta:
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"
        indexes = [
            models.Index(fields=["name", "type"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.type})"
    
    def get_absolute_url(self):
        return reverse('products:detail', args=[self.id])
    def edit_absolute_url(self):
        return reverse('products:edit', args=[self.id])


# Measurement Model
class Measurement(models.Model):
    ticket = models.OneToOneField(
        Ticket, on_delete=models.CASCADE, related_name="measurement", verbose_name="Заявка"
    )
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="measurements",
        verbose_name="Продукция"
    )
    height = models.FloatField(verbose_name="Высота")
    width = models.FloatField(verbose_name="Ширина")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="measurements/photos/", null=True, blank=True, verbose_name="Фото")

    class Meta:
        verbose_name = "Замер"
        verbose_name_plural = "Замеры"
        indexes = [
            models.Index(fields=["ticket", "product"]),
        ]

    def __str__(self):
        return f"Замер для заявки {self.ticket.id}"
    
    def get_absolute_url(self):
        return reverse('products:measurement_edit', args=[self.id]) 
