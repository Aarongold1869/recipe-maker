from django.contrib import admin
from django.urls import path
from .views import (
    recipe_detail_page,
    recipe_list_view,
    recipe_delete_view,
    recipe_edit_view,
)

urlpatterns = [
    path("", recipe_list_view),
    path("<str:slug>/", recipe_detail_page),
    path("<str:slug>/edit/", recipe_edit_view),
    path("<str:slug>/delete/", recipe_delete_view),
    
]
