from django.urls import path

from main import views

urlpatterns = [
    path('', views.index),
    path('location/', views.location),
    path('hello/<name>/<last_name>', views.hello),
    path('square/<number>', views.square),
]