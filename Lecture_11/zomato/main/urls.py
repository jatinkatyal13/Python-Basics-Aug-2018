from django.urls import path

from main import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('restaurants/', views.RestaurantList.as_view(), name = 'restaurants'),
    path('restaurant/<int:pk>', views.RestaurantDetail.as_view(), name = 'restaurant'),
    path('add_restaurant/', views.CreateRestaurant.as_view(), name = 'add_restaurant'),
    path('edit_restaurant/<int:pk>', views.UpdateRestaurant.as_view(), name = 'edit_restaurant'),
    path('delete_restaurant/<int:pk>', views.DeleteRestaurant.as_view(), name = 'delete_restaurant'),

    path('food/<int:pk>', views.FoodDetail.as_view(), name = 'food'),
]