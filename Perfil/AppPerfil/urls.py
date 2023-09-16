from django.urls import path
from .views import *

urlpatterns = [
    path('perfil/<str:user>/', ProfileView.as_view(), name="perfil"),
    path('inventario/<str:user>/', UserInventoryView.as_view(), name="inventario"),
]