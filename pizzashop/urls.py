from django.urls import path
from .views import *

urlpatterns = [
    path('', Toppings, name='Toppings'),
    path('toppings/delete/<int:pk>/', deletetopping, name='deleteToppings'),
    path('toppings/update/<int:pk>/', updateToppings, name='updateToppings'),
]