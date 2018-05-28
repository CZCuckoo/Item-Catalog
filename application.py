from flask import Flask, render_template, request, redirect, url_for, flash
from flask import make_response, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User_info, Category, Item
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import random
import string
import json
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db', connect_args={'check_same_thread':False})

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
app = Flask(__name__)

@app.route('/')
@app.route('/categories')
def showCategories():
    categories = session.query(Category).all()
    return render_template('categories.html', categories = categories)

@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items/')
def showItems(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category_id).all()
    return render_template('showitems.html', category = category, items = items)


@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    return "page to create a new category."

@app.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
    return "page to edit a category."


@app.route('/category/<int:category_id>/delete', methods=['GET', 'POST'])
def deleteCategory(category_id):
    return "page to delete a category."


@app.route('/category/<int:category_id>/item/new', methods=['GET', 'POST'])
def newItem(category_id):
    return "page add a new item."

@app.route('/category/<int:category_id>/item/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    return "page edit an item."

@app.route('/category/<int:category_id>/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    return "page delete an item."


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=8000)
