from recipe.views import main
from django.urls import path, include

app_main = 'recipe_app'

urlpatterns = [
    path('', main, name='main'),
]