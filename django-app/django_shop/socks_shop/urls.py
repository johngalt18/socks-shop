from django.urls import path

from .views import return_items

urlpatterns = [
    path('', return_items)
]

