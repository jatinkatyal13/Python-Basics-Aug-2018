from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from main import models

# Create your views here.

class Index(TemplateView):
    template_name = 'main/index.html'

# def index(request):
#     context = {}
#     return render(request, 'main/index.html', context)

class RestaurantList(ListView):
    model = models.Restaurant
    context_object_name = 'restaurants'
    # queryset = models.Restaurant.objects.filter(name__contains = 'd')

# def restaurants(request):
#     restaurants = models.Restaurant.objects.all()

#     context = {
#         'restaurants': restaurants
#     }
#     return render(request, 'main/restaurants.html', context)

class RestaurantDetail(DetailView):
    model = models.Restaurant
    template_name = 'main/restaurant.html'
    context_object_name = 'restaurant'

# def restaurant(request, pk):
#     # try:
#     #     restaurant = models.Restaurant.objects.get(pk = pk)
#     # except:
#     #     raise Http404
#     restaurant = get_object_or_404(models.Restaurant, pk=pk)

#     context = {
#         'restaurant': restaurant
#     }
#     return render(request, 'main/restaurant.html', context)

class FoodDetail(DetailView):
    model = models.Food

# def food(request, pk):
#     food = get_object_or_404(models.Food, pk=pk)

#     context = {
#         'food': foods
#     }
#     return render(request, 'main/food.html', context)

class CreateRestaurant(CreateView):
    model = models.Restaurant
    success_url = reverse_lazy('restaurants')
    # success_url = '/restaurants/'
    fields = '__all__'

class UpdateRestaurant(UpdateView):
    model = models.Restaurant
    success_url = reverse_lazy('restaurants')
    fields = '__all__'

class DeleteRestaurant(DeleteView):
    model = models.Restaurant
    success_url = reverse_lazy('restaurants')