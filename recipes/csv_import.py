from .models import *
import csv
import json

def csv_to_json():
    recipes = {}
    with open('recipes.csv') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            recipes[row[1]] = {}
            recipes[row[1]]['title'] = row[1]
            recipes[row[1]]['slug'] = row[1].replace(" ", "-")
            recipes[row[1]]['category'] = row[0]
            recipes[row[1]]['keywords'] = row[0]
            recipes[row[1]]['instructions'] = row[2]
            recipes[row[1]]['ingredients'] = {}

            i=3
            j=4
            k=5
            for _ in range(19):
                quantity = row[i] 
                unit = row[j]
                ingredient = row[k]
                i+=3
                j+=3
                k+=3
                if ingredient != '':
                    recipes[row[1]]['ingredients'][ingredient] = {}
                    recipes[row[1]]['ingredients'][ingredient]['unit'] = unit
                    recipes[row[1]]['ingredients'][ingredient]['quantity'] = quantity

    return recipes
                
def data_import():
    data = csv_to_json()
    dumps = json.dumps(data)
    json_data = json.loads(dumps)

    for x in data:
        category_name = json_data[x]['category']
        if Category.objects.filter(name=category_name).exists():
            category = Category.objects.filter(name=category_name).first()
        else:
            category = Category()
            category.name = category_name
            category.save()

        keyword_name = json_data[x]['keywords']
        if Keyword.objects.filter(name=keyword_name).exists():
            keyword = Keyword.objects.filter(name=keyword_name).first()
        else:
            keyword = Keyword()
            keyword.name = keyword_name
            keyword.save()

        ingredient_list = []
        for item in json_data[x]['ingredients']:
            
            food_name = item
            if Food.objects.filter(name=food_name).exists():
                food = Food.objects.filter(name=food_name).first()
            else:
                food = Food()
                food.name = food_name
                food.save()

            unit = Unit()
            unit.name = json_data[x]['ingredients'][item]['unit']
            unit.save()
            
            quantity = json_data[x]['ingredients'][item]['quantity']
            
            ingredient = Ingredient.objects.create(food=food, unit=unit, quantity=quantity)
            ingredient_list.append(ingredient)

        recipe = Recipe.objects.create(
            title=json_data[x]['title'],
            slug=json_data[x]['slug'],
            instructions=json_data[x]['instructions'],
            category=category
        )
        recipe.keywords.add(keyword)
        for x in ingredient_list:
            recipe.ingredients.add(x)
        recipe.save()


        


    

    
