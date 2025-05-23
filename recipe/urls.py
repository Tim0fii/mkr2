from recipe.views import main, recipe_detail
from django.urls import path, include

app_main = 'recipe_app'

urlpatterns = [
    path('', main, name='main'),
    path('recipe_detail/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]