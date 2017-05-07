#!/usr/bin/python3

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
import json

app = Flask('recipes')
mongo = PyMongo(app)
Bootstrap(app)

@app.route('/')
def home_page():
    dishes_cursor = mongo.db.dishes.find({}, {'_id': 0})
    dishes = [item for item in dishes_cursor]
    return render_template('index.html', dishes=dishes)

@app.route('/search', methods=['POST'])
def search():
    ingredients = [request.form.get(key) for key in request.form.keys()
                   if 'ingredient' in key]
    ingredient_list = []
    for ingredient in ingredients:
        ingredient_list.append({'ingredients': ingredient})
    dishes_cursor = mongo.db.dishes.find({'$or': ingredient_list}, {'_id': 0})
    dishes = [item for item in dishes_cursor]
    return json.dumps(dishes)
    #return render_template('index.html', dishes=dishes)

if __name__ == "__main__":
    app.run()
