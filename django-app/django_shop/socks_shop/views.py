from django.shortcuts import render, get_object_or_404
from .models import Socks, Stock


def return_items(request):
    items = Socks.objects.filter(available=True)

    return render(request=request, template_name='socks_shop/index.html', context={'items': items})


def item_detail(request, slug):
    item_details = Socks.objects.get(slug__iexact=slug)

    stock = Stock.objects.filter(name=item_details)

    return render(request=request, template_name='socks_shop/item_detail.html', context={'item_details': item_details,
                                                                                         'stocks': stock})