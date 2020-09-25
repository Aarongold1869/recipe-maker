from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .models import Recipe
from .forms import *

# Create your views here.
def recipe_query_view(request):
    form = RecipeQueryForm(rquest.GET or None)
    if form.is_valid()
        ingredients = form.ingredients
    

def recipe_detail_page(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    template = 'recipes/recipe_detail_page.html'
    context = {"recipe": obj}
    return render(request, template, context)

def recipe_list_view(request):
    qs = Recipe.objects.all()
    template = 'recipes/recipe_list_page.html'
    context = {'recipe_list': qs}
    return render(request, template, context)

@staff_member_required
def recipe_create_view(request):
    form = RecipeCreateForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = RecipeCreateForm()
    template = 'recipes/recipe_create_page.html'
    context = {'form': form}
    return render(request, template, context)

@staff_member_required
def recipe_edit_view(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    template = 'recipes/recipe_edit_page.html'
    context = {"recipe": obj}
    return render(request, template, context)

@staff_member_required
def recipe_delete_view(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    template = 'recipes/recipe_delete_page.html'
    context = {"recipe": obj}
    return render(request, template, context)

def ingredient_add_view(request):
    form = IngredientAddForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = IngredientAddForm()
    template = 'ingredients/ingredient_add.html'
    context = {'form': form}
    return render(request, template, context)