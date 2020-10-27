from django.urls import path

from .views import Item, Detail

urlpatterns = [
    path('', Item.as_view()),
    path('<int:pk>/', Detail.as_view()),
]