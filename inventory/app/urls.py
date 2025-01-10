from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, UserViewSet

router = DefaultRouter()
router.register(r'inventory', InventoryItemViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
