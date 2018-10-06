from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    closing_time = models.TimeField(null = True, blank = True)
    owner = models.CharField(max_length = 100, null = True, blank = True)
    contact = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Food(models.Model):
    CUISINE = (
        (1, 'Chinese'),
        (2, 'North Indian'),
        (3, 'South Indian'),
        (4, 'Italian'),
    )

    name = models.CharField(max_length = 100)
    price = models.FloatField()
    cuisine = models.IntegerField(choices = CUISINE)
    restaurant = models.ForeignKey('Restaurant', on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    