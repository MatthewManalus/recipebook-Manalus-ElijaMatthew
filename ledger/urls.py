from django.urls import path
from . import views

app_name = "ledger"

urlpatterns = [
    path("recipes/list", views.recipes_list, name="recipes-list"),
    path("recipe/<int:pk>", views.recipe_detail, name="recipe-detail"),
    path("ingredient/<int:pk>", views.ingredient_detail, name="ingredient-detail"),
]
