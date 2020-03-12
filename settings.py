import os

MONGO_URI = os.getenv('MONGO_URI') 
MONGO_DB_NAME = 'recipe_site'

PORT = int(os.environ.get('PORT', '5000'))
HOST = os.environ.get('IP', '0.0.0.0')
DEBUG = True 