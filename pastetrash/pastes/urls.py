from django.contrib import admin
from django.urls import path, include

from .views import index, paste

urlpatterns = [
    path('', index, name="index"),
    path('<str:slug>/', paste, name="paste"),
]
