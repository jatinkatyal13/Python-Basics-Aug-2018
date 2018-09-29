from django.urls import path

from my_portfolio import views

urlpatterns = [
    path('', views.index),
]