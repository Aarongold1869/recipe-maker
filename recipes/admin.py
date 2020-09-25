from django.contrib import admin
from .models import *

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    # list_display = ("ingredients",)
    search_fields = ['ingredients__name',]


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)