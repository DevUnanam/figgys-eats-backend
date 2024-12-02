from django.shortcuts import render

from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderListCreateView(generics.ListCreateAPIView):
    """
    List all orders (for admin) or create a new order (for authenticated users).
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        If the user is not a staff/admin, only return their own orders.
        """
        if self.request.user.is_staff:
            return super().get_queryset()
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assign the logged-in user to the order.
        """
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update, or partially update an order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Restrict users to only view their own orders unless they are staff/admin.
        """
        if self.request.user.is_staff:
            return super().get_queryset()
        return Order.objects.filter(user=self.request.user)

# Create your views here.
