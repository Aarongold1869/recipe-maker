from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ['name',]

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ['ingredients__name', 'title', 'author', 'slug', 'date']

class IngredientAdmin(admin.ModelAdmin):
    list_display = ("food", "quantity", "unit")
    search_fields = ['food',]

class UnitAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ['name',]

class FoodAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ['name',]


admin.site.register(Unit, UnitAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)