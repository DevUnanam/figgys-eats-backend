from django.shortcuts import render

from rest_framework import generics
from .models import Meal
from .serializers import MealSerializer

class MealListCreateView(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

