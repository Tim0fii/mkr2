from django.http import HttpResponse
from recipe.models import *
from django.shortcuts import render, redirect


def main(request):
    recipes = Recipe.objects.filter(created_at__year=2023)

    return render(request, 'main.html', context={'recipes': recipes})
