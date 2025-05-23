from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category
from datetime import datetime

def setUp(self):
    self.category = Category.objects.create(name='Test Category')

    self.recipe1 = Recipe.objects.create(
        title='Pasta Carbonara',
        description='Classic Italian pasta.',
        instructions='Boil pasta. Fry bacon. Mix with eggs and cheese.',
        ingredients='Pasta, eggs, cheese, bacon',
        created_at=datetime(2023, 1, 15),
        category=self.category
    )
    self.recipe2 = Recipe.objects.create(
        title='Borscht',
        description='Ukrainian soup.',
        instructions='Cook beets, cabbage, and meat.',
        ingredients='Beets, cabbage, meat',
        created_at=datetime(2023, 7, 10),
        category=self.category
    )
    self.recipe_old = Recipe.objects.create(
        title='Old Pie',
        description='Old pie description.',
        instructions='Bake it.',
        ingredients='Flour, sugar, apples',
        created_at=datetime(2022, 3, 5),
        category=self.category 
    )