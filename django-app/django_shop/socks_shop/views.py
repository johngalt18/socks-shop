import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
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


def show_basket(request):
    in_basket = request.session.get("in_basket", dict())
    items_in_basket = []
    total_price = 0
    for key, value in in_basket.items():
        greed = Socks.objects.get(slug__iexact=key)
        greed_sum = 0
        item = {"greed": greed, "stock": []}
        for stock, count in value.items():
            stock_sum = int(count) * greed.price
            item['stock'].append({
                "stock": stock,
                "count": count,
                "sum": stock_sum
            })
            greed_sum += stock_sum
        total_price += greed_sum
        item["sum"] = greed_sum
        items_in_basket.append(item)

    return render(request=request, template_name='socks_shop/basket.html', context={
        'items_in_basket': items_in_basket, 'total_price': total_price})


def add_in_basket(request):
    if request.is_ajax() and request.method == "POST":
        request_json = json.loads(request.body)
        slug = request_json['item_slug']
        stock = request_json['stock']
        print(request_json)
        in_basket = request.session.get("in_basket", dict())
        print(in_basket)
        if slug in in_basket:
            in_basket[slug][stock] = in_basket.get(slug, dict()).get(stock, 0) + 1
        else:
            in_basket[slug] = {stock: 1}

        request.session["in_basket"] = in_basket
        print(request.session.get("in_basket", {}))

    return JsonResponse({"status": "OK"})
