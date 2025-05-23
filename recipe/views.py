from django.http import HttpResponse
from recipe.models import *
from django.shortcuts import render, redirect


def main(request):
    recipes = Recipe.objects.filter(created_at__year=2023)

    return render(request, 'main.html', context={'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipes = Recipe.objects.get(id=recipe_id)

    return render(request, 'recipe_detail.html', context={'recipes': recipes})