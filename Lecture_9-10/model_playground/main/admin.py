from django.contrib import admin

from main import models

# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Marks)
admin.site.register(models.Branch)