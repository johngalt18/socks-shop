from django.shortcuts import render
from .models import Socks


def return_items(request):
    items = Socks.objects.filter(available=True)

    return render(request=request, template_name='socks_shop/index.html', context={'items': items})


def item_detail(request, slug):
    item_details = Socks.objects.get(slug__iexact=slug)
    return render(request=request, template_name='socks_shop/item_detail.html', context={'item_details': item_details})
