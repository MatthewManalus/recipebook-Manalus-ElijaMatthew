from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm, RecipeImageForm
from .models import Ingredient, Recipe


def recipes_list(request):
    recipes = Recipe.objects.all().order_by("name")
    return render(request, "ledger/recipes_list.html", {"recipes": recipes})


@login_required
def recipe_detail(request, pk: int):
    recipe = get_object_or_404(
        Recipe.objects.select_related("author").prefetch_related(
            "ingredients__ingredient",
            "images",
        ),
        pk=pk,
    )
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})


def ingredient_detail(request, pk: int):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    return render(request, "ledger/ingredient_detail.html", {"ingredient": ingredient})


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            if hasattr(request.user, "profile"):
                recipe.author = request.user.profile
            recipe.save()
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm()

    return render(request, "ledger/recipe_form.html", {"form": form})


@login_required
def add_recipe_image(request, pk: int):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeImageForm()

    return render(
        request,
        "ledger/recipeimage_form.html",
        {
            "form": form,
            "recipe": recipe,
        },
    )