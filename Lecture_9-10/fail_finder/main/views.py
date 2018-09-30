from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from main.models import Student, Pizza
from main.forms import LoginForm, StudentForm

from functools import reduce

# Create your views here.

def fails(request, id):
    s = Student.objects.get(id = id)

    fails = s.exam_set.filter(marks__lt = 40).count()

    context = {
        'student': s,
        'fails': fails
    }

    return render(request, 'main/index.html', context)

def highest(request, id):
    s = Student.objects.get(id = id)

    exams = s.exam_set.all()
    exam_maximum_marks = reduce(lambda a, b: a if a.marks > b.marks else b, exams)

    context = {
        'student': s,
        'maximum_marks': exam_maximum_marks
    }

    return render(request, 'main/highest.html', context)

def pizza(request, id):
    pizza = get_object_or_404(Pizza, id = id)
    # try:
    #     pizza = Pizza.objects.get(id = id)
    # except:
    #     raise Http404()

    context = {
        'pizza': pizza
    }

    return render(request, 'main/pizza.html', context)

def login(request):

    if request.method == "GET":
        form = LoginForm()

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            return HttpResponse("Hello, {}".format(username))

    context = {
        'form': form
    }

    return render(request, 'main/login.html', context)

def add_student(request):

    if request.method == "GET":
        form = StudentForm()

    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            s = form.save()
            return HttpResponse("Student created with name {}".format(s.name))

    context = {
        'form': form
    }
    return render(request, 'main/add_student.html', context)