from django.contrib import admin

from main import models

# Register your models here.

admin.site.register([
    models.Branch, 
    models.Exam, 
    models.Student,
    models.Pizza,
    models.Topping,
])