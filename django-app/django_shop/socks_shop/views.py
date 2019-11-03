from django.http import HttpResponse
from django.shortcuts import render
from .models import Socks


def return_items(request):
    items = Socks.objects.all()

    return render(request=request, template_name='socks_shop/index.html', context={'items': items})
