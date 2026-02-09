
from django.urls import path
from . import views

urlpatterns = [
    path("recipes/list", views.recipes_list, name="recipes-list"),
    path("recipe/1", views.recipe_1, name="recipe-1"),
    path("recipe/2", views.recipe_2, name="recipe-2"),
]
