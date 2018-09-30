from django.urls import path

from main import views

urlpatterns = [
    path('fails/<int:id>', views.fails),
    path('highest/<int:id>', views.highest),

    path('pizza/<int:id>', views.pizza),

    path('login', views.login),

    path('add_student/', views.add_student),
]