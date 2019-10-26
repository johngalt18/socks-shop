from django.shortcuts import render, get_object_or_404
from .models import Socks, Instance


def socks_list(request, socks_slug=None):
    socks_example = None
    socks = Socks.objects.all()
    instances = Instance.objects.filter(available=True)
    if socks_slug:
        socks_example = get_object_or_404(Socks, socks_slug)
