from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)
    steps = models.TextField(default="", blank=True)
    cooking_time = models.IntegerField(default=0)
    image = models.ImageField(upload_to="recipe_images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
