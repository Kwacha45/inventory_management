from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import InventoryItem
from .serializers import InventoryItemSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#endpoint implementation code
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer

@api_view(['GET'])
def get_inventory_items(request):
    items = Inventory.objects.all()
    serializer = InventorySerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_inventory_item(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
