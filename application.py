from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify
)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User_info, Category, Item

# Imports to create a random string for the login session
from flask import session as login_session
import random
import string

# Creates a flow object from the client secrets JSON file
from oauth2client.client import flow_from_clientsecrets
# Handles errors trying to exchange authorization codes for tokens
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

# Client ID: 929908741189-mb1fncqv8dt044dmacume9t5plin9167.apps.googleusercontent.com
# Client Secret: fMp2Fd1PPUnXGfplG5tZoV1p

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db', connect_args={'check_same_thread':False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#______________________________________________________________________________
# Oauth routes
#______________________________________________________________________________

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)






#______________________________________________________________________________
# Category routes
#______________________________________________________________________________


# Show all categories
@app.route('/')
@app.route('/categories')
def showCategories():
    categories = session.query(Category).all()
    return render_template('categories.html', categories = categories)

# Create a new cateogry
@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'], description=request.form['description'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')

# Edit an existing category
@app.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
        if request.form['description']:
            editedCategory.description = request.form['description']

        session.add(editedCategory)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory)

# Delete a cateogry
@app.route('/category/<int:category_id>/delete', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(Category).filter_by(id= category_id).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        return redirect(url_for('showCategories', category_id=category_id))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)
    return render_template('deleteCategory.html')

#______________________________________________________________________________
# Item routes
#______________________________________________________________________________

# Show all items in a specific category
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items/')
def showItems(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category_id).all()
    return render_template('showItems.html', category = category, items = items)

# Create a new item within a category
@app.route('/category/<int:category_id>/item/new', methods=['GET', 'POST'])
def newItem(category_id):
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form['description'],category_id=category_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('newItem.html', category_id=category_id)

# Edit an item within a category
@app.route('/category/<int:category_id>/item/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    itemToEdit = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            itemToEdit.name = request.form['name']
        if request.form['description']:
            itemToEdit.description = request.form['description']
        session.add(itemToEdit)
        session.commit()
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('editItem.html', category_id=category_id, item_id=item_id, item=itemToEdit)

# Delete an item in a category
@app.route('/category/<int:category_id>/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('deleteItem.html', item=itemToDelete)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port=8000)
