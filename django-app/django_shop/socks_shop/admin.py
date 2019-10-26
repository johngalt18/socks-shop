from django.contrib import admin
from .models import Socks, Instance


class AdminSocks(admin.ModelAdmin):
    list_display = ['name', 'available', 'slug', 'price']
    list_filter = ['available', 'price']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name', )}


class AdminInstances(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'size', 'stock', 'available']
    list_filter = ['available', 'price', 'size']
    list_editable = ['stock', 'available', 'size']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Socks, AdminSocks)
admin.site.register(Instance, AdminInstances)