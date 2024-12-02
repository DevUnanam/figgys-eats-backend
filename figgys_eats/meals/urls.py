from django.urls import path
from .views import MealListCreateView, MealDetailView

urlpatterns = [
    path('', MealListCreateView.as_view(), name='meal-list'),
    path('<int:id>/', MealDetailView.as_view(), name='meal-detail'),
]
