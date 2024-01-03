from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('split/', views.split, name="split"),
]