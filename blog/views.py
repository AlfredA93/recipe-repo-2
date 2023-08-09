""" Libraries """
from django.shortcuts import render
from django.views import generic
from .models import Recipe


class RecipeList(generic.ListView):
    "Recipe List View for homepage"
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-likes')
    template_name = 'index.html'
    paginate_by = 9
