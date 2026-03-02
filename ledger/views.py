from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Ingredient, Recipe


def recipes_list(request):
    recipes = Recipe.objects.all().order_by("name")
    return render(request, "ledger/recipes_list.html", {"recipes": recipes})


@login_required
def recipe_detail(request, pk: int):
    recipe = get_object_or_404(
        Recipe.objects.select_related("author").prefetch_related("ingredients__ingredient"),
        pk=pk,
    )
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})


def ingredient_detail(request, pk: int):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    return render(request, "ledger/ingredient_detail.html", {"ingredient": ingredient})