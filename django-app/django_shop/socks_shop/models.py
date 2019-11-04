from django.db import models
from django.utils.safestring import mark_safe

from django.shortcuts import reverse


class Socks(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Наименование", unique=True)
    slug = models.SlugField(max_length=30, db_index=True, unique=True)
    image = models.ImageField(upload_to='images/%Y/%m/%D/', blank=True, null=True, verbose_name="Изображение товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание", null=False, default="")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    color = models.CharField(max_length=30, db_index=False, verbose_name="Цвет", null=True)

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return 'No Image Found'

    def get_absolute_url(self):
        return reverse('item_details_url', kwargs={'slug': self.slug})

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        ordering = ['name']
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'

        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.ForeignKey(Socks, on_delete=models.CASCADE, verbose_name="Наименование")
    amount = models.PositiveIntegerField(verbose_name="Количество")
    size = models.PositiveSmallIntegerField(verbose_name="Размер")

    class Meta:
        ordering = ['name']
        verbose_name = 'Экземпляр'
        verbose_name_plural = 'Экземпляры'

    def __len__(self):
        return self.amount
