from django.db import models


class Shop(models.Model):
    name = models.CharField('Название', max_length=128)
    address = models.CharField('Адрес', max_length=128)
    status = models.CharField('Статус', max_length=128)

    def __str__(self):
        return self.address

class Manufacturer(models.Model):
    name = models.CharField('Производитель', max_length=128)
    country = models.CharField('Страна', max_length=128)
    CEO = models.CharField('Ген. директор', max_length=128)

    def __str__(self):
        return self.name

class Tech(models.Model):
    name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель")
    model = models.CharField('Модель', max_length=128)
    address = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Адрес магазина, где продается товар:")
    price = models.IntegerField('Цена', max_length=10)

    def __str__(self):
        return self.model