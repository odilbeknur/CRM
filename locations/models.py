from django.db import models

class Location(models.Model):
    CITY_CHOICES = [
        ('Tashkent', 'Ташкент'),
    ]

    DISTRICT_CHOICES = [
        ('almazar', 'Алмазарский район'),
        ('bektemir', 'Бектемирский район'),
        ('mirobod', 'Мирабадский район'),
        ('mirzo_ulugbek', 'Мирзо Улугбекский район'),
        ('sergeli', 'Сергелийский район'),
        ('chilhonzor', 'Чиланзарский район'),
        ('shaikhontohur', 'Шайхонтаурский район'),
        ('yunusabad', 'Юнусабадский район'),
        ('yakkasaroy', 'Яккасарайский район'),
        ('yashnobod', 'Яшнабадский район'),
        ('uchtepa', 'Учтепинский район'),
    ]
    city = models.CharField(max_length=100, choices=CITY_CHOICES, verbose_name="Город")
    district = models.CharField(max_length=100, choices=DISTRICT_CHOICES, verbose_name="Район", blank=True, null=True)
    street = models.CharField(max_length=100, verbose_name="Улица", blank=True, null=True)
    apartment = models.CharField(max_length=50, verbose_name="Квартира", blank=True, null=True)
    entrance = models.CharField(max_length=50, verbose_name="Подъезд", blank=True, null=True)
    floor = models.CharField(max_length=50, verbose_name="Этаж", blank=True, null=True)
    landmark = models.CharField(max_length=100, verbose_name="Ориентир", default="Нет", blank=True, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return f"г. {self.city}, {self.district} р-н, улица {self.street}, дом {self.apartment}, {self.entrance}, {self.floor}, Ориентир - {self.landmark}"
