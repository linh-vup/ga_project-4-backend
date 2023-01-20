from django.urls import path
from .views import FoodListView, FoodDetailView, FoodSearchView

urlpatterns = [
  path('', FoodListView.as_view()),
  path('<int:pk>/', FoodDetailView.as_view()),
  path('search/', FoodSearchView.as_view())
]