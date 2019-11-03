from django.http import HttpResponse
from django.shortcuts import render
from .models import Socks


def return_items(request):
    items = ['123', '3', 't645', '756']

    return render(request=request, template_name='socks_shop/index.html', context={'items': items})
