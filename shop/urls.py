from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('checkout/', views.checkout),
    path('store/', views.store),
]