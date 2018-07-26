from django.http import HttpResponse
from django.shortcuts import render

from .models import Dish
from .forms import DishForm

# Create your views here.
def home_view(request, *args, **kwargs):
    dishes_cursor = Dish.objects.mongo_find({}, {'_id': 0})
    dishes = [dict(item) for item in dishes_cursor]
    return render(request, "home.html", {'dishes': dishes})


def dish_create_view(request):
    form = DishForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DishForm()

    return render(request, 'dish_create.html', {'form': form})


def search_view(request):
    """
        Searchs on db recipes by ingredients

        Returns:
	    json object for finded recipes
    """
    ingredients = [request.form.get(key) for key in request.form.keys()
                   if 'ingredient' in key]
    ingredient_list = []
    for ingredient in ingredients:
        ingredient_list.append({'ingredients': ingredient})

    dishes_cursor = None
    if not ingredient_list:
        dishes_cursor = Dish.objects.mongo_find({}, {'_id': 0})
    else:
        dishes_cursor = Dish.objects.mongo_find({'$or': ingredient_list}, {'_id': 0})
    
    dishes = [dict(item) for item in dishes_cursor]
    
    return jsonify(dishes)
