from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'Avinash', 'age': 22},
        {'name': 'hari', 'age': 21},
        {'name': 'Bishesh', 'age': 32}
    ]

    return render(request, "index.html",context= {'peoples': peoples})
    # return HttpResponse("<h2>Hey i am a django server.</h2>")
