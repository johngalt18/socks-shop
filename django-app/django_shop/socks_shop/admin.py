from django.contrib import admin
from .models import Socks, Stock
from django.utils.safestring import mark_safe


class AdminSocks(admin.ModelAdmin):
    list_display = ['available', 'price', 'color', 'slug', 'name', 'image', 'image_tag']
    list_filter = ['available', 'price', 'color']
    list_editable = ['price', 'color', 'image']

    prepopulated_fields = {'slug': ('name', )}


class AdminStock(admin.ModelAdmin):
    list_display = ['name', 'size', 'amount']
    list_filter = ['name', 'size', 'amount']
    list_editable = ['size', 'amount']


admin.site.register(Socks, AdminSocks)
admin.site.register(Stock, AdminStock)
