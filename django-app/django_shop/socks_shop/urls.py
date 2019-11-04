from django.urls import path

from .views import return_items, item_detail

urlpatterns = [
    path('', return_items, name='list_of_items_url'),
    path('item/<str:slug>/', item_detail, name='item_details_url')
]

