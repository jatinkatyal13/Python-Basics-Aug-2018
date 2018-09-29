from django.shortcuts import render

# Create your views here.

def index(request):

    name = "Jatin Katyal"
    interests = [
        "Driving",
        "Party",
        "Gaming",
        "TV Series expecially TBBT"
    ]
    degree = "B.Tech CSE"
    skills = [
        "Python",
        "GO",
        "Node",
        "C/C++",
        "Android",
        "PHP",
        "Java",
    ]

    context = {
        "name": name,
        "interests": interests,
        "degree": degree,
        "skills": skills
    }

    return render(request, 'my_portfolio/index.html', context)