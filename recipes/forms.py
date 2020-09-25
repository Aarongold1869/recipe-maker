from django import forms
from .models import *


class IngredientAddForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']

    def clean_name(self, *args, **kwargs):
        instance = self.instance
        name = self.cleaned_data.get('name')
        qs = Ingredient.objects.filter(name__iexact=name)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This ingredient has already been added.")
        return name

def get_ingredients():
    qs = Ingredient.objects.all()
    OPTIONS = []
    for x in qs:
        OPTIONS.append((x.id, x.name))
    tuple(OPTIONS)
    return OPTIONS

class RecipeCreateForm(forms.ModelForm):
    OPTIONS = get_ingredients()
    ingredients = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        choices=OPTIONS)

    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'ingredients', 'instructions']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = Recipe.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title


class RecipeQueryForm(forms.ModelForm):
    OPTIONS = get_ingredients()
    ingredients = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        choices=OPTIONS)

    class Meta:
        model = Ingredient
        fields = ['ingredients']