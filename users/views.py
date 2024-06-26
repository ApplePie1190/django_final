from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Ваш аккаунт создан: можно войти на сайт.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    user = request.user
    recipes = Recipe.objects.filter(author=user)
    context = {"user": user, "recipes": recipes}
    return render(request, "users/profile.html", context)
