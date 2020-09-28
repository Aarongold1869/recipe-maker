from django.db import models
from django.contrib.auth import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(unique=True, max_length=128)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.PROTECT, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, blank=True)
    quantity = models.CharField(max_length=100, blank=False, null=False)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.food) + ' ' + str(self.quantity) + ' ' + str(self.unit)

class Recipe(models.Model):
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=30, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True, related_name="ingredients")
    instructions = models.TextField(blank=False, null=False)
    date = models.DateField(auto_now_add=True, null=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.PROTECT)
    # image = models.FileFeild(blank=True, null=True)
