from django.contrib import admin
from main import models

# register your models here.
admin.site.register([models.Restaurant, models.Food])