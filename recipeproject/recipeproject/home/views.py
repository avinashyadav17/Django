from django.shortcuts import render, redirect
from .forms import RecipeForm   
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'home/recipe_list.html', {'recipes': recipes})


# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')   # temporary redirect
    else:
        form = RecipeForm()

    return render(request, 'home/create.html', {'form': form})