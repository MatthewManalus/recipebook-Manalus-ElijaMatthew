from django.urls import path

from . import views

app_name = "ledger"

urlpatterns = [
    path("recipes/list", views.recipes_list, name="recipes-list"),
    path("recipe/add", views.add_recipe, name="recipe-add"),
    path("recipe/<int:pk>", views.recipe_detail, name="recipe-detail"),
    path("recipe/<int:pk>/add_image", views.add_recipe_image, name="recipe-add-image"),
    path("ingredient/<int:pk>", views.ingredient_detail, name="ingredient-detail"),
]