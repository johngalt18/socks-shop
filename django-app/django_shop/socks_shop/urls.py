from django.urls import path

from .views import return_items, item_detail, show_basket, add_in_basket

urlpatterns = [
    path('', return_items, name='list_of_items_url'),
    path('item/<str:slug>/', item_detail, name='item_details_url'),
    path('basket', show_basket, name='basket_url'),
    path('basket/add', add_in_basket, name='add_in_basket_url')
]
