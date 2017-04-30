#!/usr/bin/python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo

app = Flask('recipes')
mongo = PyMongo(app)
Bootstrap(app)

@app.route('/')
def home_page():
    dishes_cursor = mongo.db.dishes.find({}, {'_id': 0})
    dishes = [item for item in dishes_cursor]
    return render_template('index.html', dishes=dishes)


if __name__ == "__main__":
    app.run()
