from django.db import models
from django.contrib.auth import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Recipe(models.Model):
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=30, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="ingredients")
    instructions = models.TextField(blank=False, null=False)
    date = models.DateField(auto_now_add=True, null=True)
    # image = models.FileFeild(blank=True, null=True)
