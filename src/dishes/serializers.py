from rest_framework_mongoengine import serializers

from .models import Dish


class DishSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
