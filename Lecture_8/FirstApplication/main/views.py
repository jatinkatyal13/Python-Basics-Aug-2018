from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

	students = [
		"<li>Saurabh</li>",
		"<li>Nikhil</li>",
		"<li>Avik</li>",
		"<li>Siddharth</li>",
		"<li>Vipul</li>",
		"<li>Navneet</li>",
		"<li>Shweta</li>",
		"<li>Yash</li>",
		"<li>Zohaib</li>",
		"<li>Abhishek</li>",
		"<li>Shubhank</li>"
	]

	context = {
		"students": students,
		"developer": "Jatin Katyal"
	}

	return render(request, 'main/index.html', context)

def location(request):
	return HttpResponse("We are at Coding Blocks")

def hello(request, name, last_name):
	return HttpResponse("Hello, {} {}".format(name, last_name))

def square(request, number):
	return HttpResponse("Square of this number is: {}".format(int(number)**2))