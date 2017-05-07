#!/usr/bin/python3

import json
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

app = Flask('recipes')
mongo = PyMongo(app)
Bootstrap(app)

@app.route('/')
def home_page():
    """
        Displays list of all recipes on the main page of the app

        Returns:
            a template of main page
    """
    dishes_cursor = mongo.db.dishes.find({}, {'_id': 0})
    dishes = [item for item in dishes_cursor]
    return render_template('index.html', dishes=dishes)

@app.route('/search', methods=['POST'])
def search():
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
    dishes_cursor = mongo.db.dishes.find({'$or': ingredient_list}, {'_id': 0})
    dishes = [item for item in dishes_cursor]
    return jsonify(dishes)

if __name__ == "__main__":
    app.run()
