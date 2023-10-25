from django.shortcuts import render, redirect  # Added 'redirect' import
from .models import *
from django.core.cache import cache
from django.conf import settings  # Added 'settings' import
from django.core.cache.backends.base import DEFAULT_TIMEOUT  # Added 'DEFAULT_TIMEOUT' import

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def home(request):
    recipes = Recipe.objects.all()
    
    context = {'recipes': recipes}
    
    return render(request, "home.html", context)

def view_recipe(request, id):
    if cache.get(id):
        print("Data From Cache")
        recipe = cache.get(id)
    else:
        try:
            recipe = Recipe.objects.get(id=id)
            cache.set(id, recipe)  # Added CACHE_TTL for cache expiration
            print("Data From DB")
        except Recipe.DoesNotExist:
            return redirect('/')
    
    context = {'recipe': recipe}
    
    return render(request, "view.html", context)
