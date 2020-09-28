from collections import Counter

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect

from .models import Recipe, Ingredient
from .forms import *

# Create your views here.
def ingredient_select_view(request):
    form = RecipeQueryForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data["ingredients"]
        request.session['ingredients'] = form_data
        return HttpResponseRedirect('/recipes/query/') 
    template = 'recipes/ingredient_select.html'
    context = {"form" : form}
    return render(request, template, context)

def recipe_query_view(request):
    food_list = request.session.get('ingredients')
    ingredient_list = []
    match_list = []
    for food in food_list:
        x = Ingredient.objects.filter(food=food)
        ingredient_list.append(x)
    for ingredient in ingredient_list:
        for recipe in Recipe.objects.all().filter(ingredients=ingredient[0]):
            match_list.append(recipe)
    result = [item for items, c in Counter(match_list).most_common() 
                                      for item in [items] * c]
    recipe_list = list(dict.fromkeys(result))
    template = 'recipes/recipe_list_page.html'
    user_ingredients = []
    for x in food_list:
        obj = Food.objects.get(id=x)
        name = str(obj.name)
        user_ingredients.append(name)
    context = {
        'recipe_list': recipe_list,
        'ingredients': user_ingredients
    }
    return render(request, template, context)

def recipe_detail_page(request, slug):  
    obj = get_object_or_404(Recipe, slug=slug)
    ingredients = obj.ingredients.all()
    template = 'recipes/recipe_detail_page.html'
    context = {"recipe": obj,
        "ingredients" : ingredients,
    }
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
        ingredients = form.cleaned_data['ingredients']
        for x in ingredients:
            obj.ingredients.add(x)
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