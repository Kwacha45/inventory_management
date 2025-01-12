from django.urls import path
from . import views

urlpatterns = [
    path('api/inventory/', views.get_inventory_items, name='get_inventory_items'),
    path('api/inventory/add/', views.add_inventory_item, name='add_inventory_item'),
]
