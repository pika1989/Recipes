from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework_mongoengine import generics 

#from .forms import DishForm
from .models import Dish
from .serializers import DishSerializer


class DishListCreate(generics.ListCreateAPIView):
#    lookup_field = 'id'
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
#def home_view(request, *args, **kwargs):
#    dishes = Dish.objects.all()
#    serializer = DishSerializer(dishes, many=True)
#    print(len(serializer.data))
#    return render(request, "home.html", {'dishes': dishes})
#    return JsonResponse(serializer.data, safe=False)


#def dish_create_view(request):
#    form = DishForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = DishForm()
#
#    return render(request, 'dish_create.html', {'form': form})


#def search_view(request):
#    """
#        Searchs on db recipes by ingredients
#
#        Returns:
#	    json object for finded recipes
#    """
#    ingredients = [request.form.get(key) for key in request.form.keys()
#                   if 'ingredient' in key]
#    ingredient_list = []
#    for ingredient in ingredients:
#        ingredient_list.append({'ingredients': ingredient})
#
#    dishes_cursor = None
#    if not ingredient_list:
#        dishes_cursor = Dish.objects.mongo_find({}, {'_id': 0})
#    else:
#        dishes_cursor = Dish.objects.mongo_find({'$or': ingredient_list}, {'_id': 0})
#    
#    dishes = [dict(item) for item in dishes_cursor]
#    
#    return jsonify(dishes)
