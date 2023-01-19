from django.urls import path  # import path from django
from .views import UserDayListView, UserDayDetailView  # import class from .views

urlpatterns = [
    path('', UserDayListView.as_view()),
    path('<int:pk>/', UserDayDetailView.as_view())
]