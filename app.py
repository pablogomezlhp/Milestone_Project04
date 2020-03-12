import os
from flask import Flask, render_template, redirect, session, request, \
    url_for, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import bcrypt
import settings
from utils import is_password_valid
from os import path
from pydantic import BaseModel, Field


if path.exists('env.py'):
    import env

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MONGO_DBNAME'] = settings.MONGO_DB_NAME
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    recip = list(mongo.db.recipes.find().sort('show_recipes',
                 pymongo.DESCENDING))

    return render_template('index.html',
                           recipe=mongo.db.recipes.find(),
                           recipes=recip)


@app.route('/register', methods=['POST', 'GET'])
def register():
    """Allow new users to register"""

    if request.method == 'POST':
        users = mongo.db.users
        existing_user = \
            users.find_one({'username': request.form['username']})
        use_password = request.form['password']

        if not use_password:
            flash('Password cannot be empty.')
        else:
            if not existing_user:

                # If there is no existing user with that username, encrypt the new user's password

                pw_hash = bcrypt.hashpw(request.form['password'
                        ].encode('utf-8'), bcrypt.gensalt())

                # Decode the hashed password while keeping it encrypted so it can be stored in the MongoDB database

                db_password = pw_hash.decode('utf-8')

                # Add the username and encrypted password to the database

                users.insert({'username': request.form['username'],
                             'password': db_password})

                # The newly registered user is logged in

                session['username'] = request.form['username']
                return redirect(url_for('index'))

            # The user sees this message if their chosen password is already in the database

            flash('That username is taken. Please try a different one.')

    return render_template('register.html',
                           recipes=mongo.db.recipes.find())


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Allow registered user to log in"""

    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form['username'
                                    ]})

        if login_user:

            # If the username is in the database, hash the password entered in the form and compare it with the hashed password in the database for that user

            if is_password_valid(request, login_user,
                                 request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('index'))

        # The user sees this message if the username and/or password are invalid

        flash('Invalid username/password combination.')

    return render_template('login.html')


@app.route('/logout')
def logout():
    """
    Clear session (not user logged)
    """

    session.clear()
    return redirect(url_for('index'))


@app.route('/show_recipes')
def show_recipes():
    """  
    Get all recipes by mongo database and return all the information into the showrecipes.html
    """

    return render_template('showrecipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/like/recipe_id?=<id>')
def like(id):
    '''Controls behavior of user-like increment and decrements operator.
    Feature is dependant upon user interaction in the user-interface.'''

    mongo.db.recipes.find_one_and_update({'_id': ObjectId(id)},
            {'$inc': {'likes': 1}})

    return redirect(url_for('show_recipes'))


@app.route('/dislike/recipe_id?=<id>')
def dislike(id):
    '''Controls behavior of user-dislike increment and decrements operator.
    Feature is dependant upon user interaction in the user-interface.'''

    mongo.db.recipes.find_one_and_update({'_id': ObjectId(id)},
            {'$inc': {'dislikes': 1}})
    return redirect(url_for('show_recipes'))


# Allows to print all the information by cattegorie

@app.route('/list_recipes_by_cat/<catt_name>', methods=['GET', 'POST'])
def list_recipes_by_cat(catt_name):
    """List recipes by category"""

    results = \
        mongo.db.recipes.find({'catt_name': catt_name}).sort('recipe_title'
            , 1)
    return render_template('showrecipes.html', recipes=results,
                           count=results.count())


@app.route('/add_recipe')  # Display all fields that need to be filled
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.diet.find(),
                           cosine=mongo.db.cuisine.find(),
                           cattegoria=mongo.db.cattegoria.find(),
                           allergen=mongo.db.allergen.find())






@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """ Add all the information filled as a new recipe into to the DataBase """

    recipes = mongo.db.recipes

    new_recipe = {
        'image_path': request.form.get('image_path'),
        'diet_name': request.form.get('diet_name'),
        'select_cusine': request.form.get('select_cusine'),
        'allergen_name': request.form.get('allergen_name'),
        'recipe_name': request.form.get('recipe_name'),
        'recipe_author': request.form.get('recipe_author'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_method': request.form.get('recipe_method'),
        'catt_name': request.form.get('catt_name'),
        'username': session['username'],
        }

    recipes.insert_one(new_recipe)

    # Insert validations
    # Research pydantic

    

    return redirect(url_for('index'))


@app.route('/show_recipe/<recipe_id>', methods=['GET', 'POST'])
def show_recipe(recipe_id):
    """ display the selected recipe using the field ID. """

    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=the_recipe)


@app.route('/user_recipes')
def user_recipes():

     # Display receipts listed by user

    try:
        user = session['username']
    except KeyError:
        flash("Couldn't find your session")

    query = {'username': user}
    results = mongo.db.recipes.find(query).sort('recipe_name')
    return render_template('listrecipes.html', recipes=results,
                           count=results.count())


@app.route('/edit_recipe/<recipe_id>')  # Allow user to Edit the receipts that he have uploaded before
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template(
        'editrecipe.html',
        recipe=the_recipe,
        categories=all_categories,
        categori=mongo.db.diet.find(),
        cosine=mongo.db.cuisine.find(),
        cattegoria=mongo.db.cattegoria.find(),
        allergen=mongo.db.allergen.find(),
        )


# Replace the new data into to the DataBase, if dont have any new document just keep the old field.

@app.route('/replacing_recipe<recipe_id>', methods=['POST'])
def replacing_recipe(recipe_id):
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)}, {
        'recipe_name': request.form.get('recipe_title'),
        'image_path': request.form.get('image_path'),
        'diet_name': request.form.get('diet_name'),
        'select_cusine': request.form.get('select_cusine'),
        'allergen_name': request.form.get('allergen_name'),
        'recipe_name': request.form.get('recipe_name'),
        'recipe_author': request.form.get('recipe_author'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_method': request.form.get('recipe_method'),
        'catt_name': request.form.get('catt_name'),
        'username': session['username'],
        })

    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=the_recipe)


@app.route('/deleting_recipe/<recipe_id>', methods=['GET', 'POST'])  # Allow user to Delete his receipts
def deleting_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('show_recipes'))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host=settings.HOST, port=settings.PORT,
            debug=settings.DEBUG)


			