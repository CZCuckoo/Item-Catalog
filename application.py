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

engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
app = Flask(__name__)
redis = Redis()

@app.route('/')
@app.route('/categories')
def showCategories():
    categories = session.query(Category).all()
    return render_template('categories.html', categories = categories)

@app.route('/category/new', methods=['GET', 'POST'])
def newCategory():
    categories = session.query(Cateogry).all()
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html', categories = categories)

@app.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])

@app.route('/category/<int:category_id>/delete', methods=['GET', 'POST'])

@app.route('/category/<int:category_id>', methods=['GET', 'POST'])

@app.route('/category/<int:category_id>/items', methods=['GET', 'POST'])

@app.route('/category/<int:category_id>/item/new', methods=['GET', 'POST'])

@app.route('/category/<int:category_id>/item/<int:item_id/edit/', methods=['GET', 'POST'])

@app.route('/category/<int:category_id>/item/<int:item_id/delete/', methods=['GET', 'POST'])


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=8000)
