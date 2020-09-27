from .models import *
import csv

def csv_import():
    with open('recipes.csv') as csv_file:
        reader = csv.reader(csv_file)
        ingredient_list = []
        for row in reader:
            i = 3
            j = 4
            k = 5
            l = 3
            for _ in range(19):
                unit = Unit.objects.get_or_create(name=row[i])
                unit.save()
                i+=3
            for _ in range(19):
                unit = Unit.objects.get(name=row[l])
                ingredient = Ingredient.objects.get_or_create(
                    name=row[j],
                    unit=unit,
                    quantity=row[k]
                )
                ingredient.save()
                ingredient_list.append(ingredient)
                j+=3
                k+=3
                l+=3
            keyword = Keyword.objects.get_or_create(name=row[2])
            keyword.save()
            recipe = Recipe.objects.get_or_create(
                title=row[0],
                instructions=row[1],
                category=row[2],
                slug=(row[0].replace(" ", "-")),
                keyword=keyword
            )
            recipe.save()
            recipe.ingredients.add(ingredient_list)
            recipe.save()
            ingredient_list = []