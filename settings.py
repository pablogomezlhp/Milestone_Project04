import os

MONGO_URI = os.getenv('MONGO_URI')  #'mongodb+srv://pablolhp:Gavioes13@myfirstcluster-fwrws.mongodb.net/recipe_site?retryWrites=true&w=majority'  # Need be hidded
MONGO_DB_NAME = 'recipe_site'

PORT = int(os.environ.get('PORT', '5000'))
HOST = os.environ.get('IP', '0.0.0.0')
DEBUG = True # Remove when published on Heroku