from django.db import models
import datetime

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length = 100)
    hod = models.CharField(max_length = 100)

    def __str__ (self):
        return self.name

class Student(models.Model):

    def upload_to(instance, file_name):
        y = datetime.datetime.now().year
        m = datetime.datetime.now().month
        return "display_picture/{}/{}/{}/{}.{}".format(instance.name, y, m, instance.name, file_name.split('.')[-1])

    GENDER = (
        ('N', 'Not Specified'),
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    gender = models.CharField(max_length = 1, choices = GENDER, default = 'N')
    language = models.CharField(max_length = 100)
    mark = models.IntegerField(null = True, blank = True)

    display_picture = models.ImageField(
            null = True, 
            blank = True, 
            upload_to = upload_to
    )

    branch = models.ForeignKey('Branch', on_delete = models.CASCADE, null = True)

    def __str__ (self):
        return self.name

class Marks(models.Model):

    SUBJECTS = (
        (1, 'English'),
        (2, 'Maths'),
        (3, 'C++'),
        (4, 'Physics'),
    )

    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    subject = models.IntegerField(choices = SUBJECTS)
    marks = models.IntegerField(default=0)