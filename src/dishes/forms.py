from django import forms

from .models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            'name',
            'ingredients',
            'time',
            'recipe'
        ]


class SearchForm(forms.ModelForm):
    pass
