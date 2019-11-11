from django.shortcuts import render, get_object_or_404, redirect
from .models import Socks, Stock
from .forms import StockForm
from django.views.generic.edit import CreateView

from django.views.decorators.http import require_http_methods


def return_items(request):
    items = Socks.objects.filter(available=True)

    return render(request=request, template_name='socks_shop/index.html', context={'items': items})


class CreateMyModelView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'socks_shop/template.html'
    success_url = 'socks_shop/success.html'


def item_detail(request, slug):
    item_details = Socks.objects.get(slug__iexact=slug)

    stock = Stock.objects.filter(name=item_details)

    return render(request=request, template_name='socks_shop/item_detail.html', context={'item_details': item_details,
                                                                                         'stocks': stock})
