from django.urls import path
from .views import ColorListView, ColorDetailView

urlpatterns = [
  path('', ColorListView.as_view()),
  path('<int:pk>/', ColorDetailView.as_view())
]