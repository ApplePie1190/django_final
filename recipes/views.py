from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required


def home(request):
    context = {"recipes": Recipe.objects.order_by("?")[:5]}
    return render(request, "recipes/home.html", context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {"recipe": recipe}
    return render(request, "recipes/detail.html", context)


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            recipe = form.save(commit=False)
            recipe.author = current_user
            recipe.save()
            return redirect("profile")  # Перенаправление на страницу списка рецептов
    else:
        form = RecipeForm()
    return render(request, "recipes/add_recipe.html", {"form": form})


@login_required
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect(
                "detail", recipe_id=recipe_id
            )  # Перенаправление на страницу деталей рецепта
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipes/edit_recipe.html", {"form": form, "recipe": recipe})


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect("profile")
