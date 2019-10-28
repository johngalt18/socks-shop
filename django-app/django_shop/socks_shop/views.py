from django.shortcuts import render, get_object_or_404
from .models import Socks, Stock


def socks_list(request):
    return render(request, 'shop/product/list.html')


def socks_detail(request, id, slug):
    details = get_object_or_404(Stock, id=id, slug=slug)
    return render(request, 'shop/product/detail.html', {'details': details})