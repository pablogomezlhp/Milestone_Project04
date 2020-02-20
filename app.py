import os
from flask import Flask, render_template,redirect, session, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_site'
app.config["MONGO_URI"] = 'mongodb+srv://pablolhp:Gavioes13@myfirstcluster-fwrws.mongodb.net/recipe_site?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html',recipes=mongo.db.recipes.find())

@app.route('/register', methods=['POST', 'GET'])
def register():
    
    """Allow new users to register"""
    
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})
        use_password = request.form['password']
        
        if use_password is None:
            flash('Password cannot be empty.')
        else:
            if existing_user is None:
                # If there is no existing user with that username, encrypt the new user's password
                pw_hash = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
                # Decode the hashed password while keeping it encrypted so it can be stored in the MongoDB database
                db_password = pw_hash.decode("utf-8")
                # Add the username and encrypted password to the database
                users.insert({'username' : request.form['username'], 'password' : db_password})
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
        login_user = users.find_one({'username' : request.form['username']})
    
        if login_user:
            # If the username is in the database, hash the password entered in the form and compare it with the hashed password in the database for that user
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                return redirect(url_for('index'))
    
        # The user sees this message if the username and/or password are invalid
        flash('Invalid username/password combination.')
        
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))  

@app.route("/show_recipes")
def show_recipes():
    return render_template('showrecipes.html',recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",
                            categories=mongo.db.diet.find(), cosine=mongo.db.cuisine.find(), allergen=mongo.db.allergen.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)