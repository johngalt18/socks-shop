from django.db import models
from django.contrib.postgres.fields import ArrayField


class Socks(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=30, db_index=True)
    image = models.ImageField(upload_to='Item/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")
    available = models.BooleanField(default=True, verbose_name="Доступен")

    class Meta:
        ordering = ['name']
        verbose_name = 'Носки'
        verbose_name_plural = 'Носки'

        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name


class Instance(Socks):
    def __init__(self):
        super(Socks, self).__init__()

    size = ArrayField(models.CharField(max_length=10, blank=True), size=8)
    stock = models.PositiveIntegerField(verbose_name="На складе")

    class Meta:
        ordering = ['name']
        verbose_name = 'Экземпляр'
        verbose_name_plural = 'Экземпляры'

    def __str__(self):
        return self.name
