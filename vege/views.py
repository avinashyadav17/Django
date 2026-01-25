from django.shortcuts import render

# Create your views here.
def receipe(request):
    return render(request,"receipes.html")


def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")