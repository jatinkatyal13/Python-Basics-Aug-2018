from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length = 100)
    hod = models.CharField(max_length = 100)

    def __str__ (self):
        return self.name

    class Meta:
        ordering = ('name',)
        
class Newsletter(models.Model):
    name = models.CharField(max_length = 100)

class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length = 100, default = 'unnamed')
    age = models.IntegerField()
    branch = models.ForeignKey('Branch', on_delete = models.CASCADE)
    newsletter = models.ForeignKey('Newsletter', on_delete = models.CASCADE)

    def __str__ (self):
        return self.name

class Exam(models.Model):
    SUBJECT = (
        (1, 'English'),
        (2, 'Maths'),
        (3, 'C++'),
        (4, 'Python'),
    )
    subject = models.IntegerField(choices = SUBJECT)
    marks = models.IntegerField()
    student = models.ForeignKey('Student', on_delete = models.CASCADE)

    def __str__ (self):
        return "{} - {}".format(self.subject, self.marks)


# Many to Many Relations

class Topping(models.Model):
    name = models.CharField(max_length = 100)

    def __str__ (self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length = 100)
    cost = models.IntegerField()

    # many to many field
    toppings = models.ManyToManyField('Topping')

    def __str__ (self):
        return self.name