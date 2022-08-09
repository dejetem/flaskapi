from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes
from dotenv import load_dotenv
load_dotenv()
import os
#from pymongo import MongoClient


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
app.config['JWT_TOKEN_LOCATION'] = os.getenv("JWT_TOKEN_LOCATION")

api = Api(app)
bcrypt = Bcrypt(app)
api = Api(app)
jwt = JWTManager(app)
api = Api(app)
cors = CORS(app, resources={r'/*': { 'origins': '*' }})
#client = MongoClient()

app.config['MONGODB_SETTINGS'] = os.getenv("MONGODB_SETTINGS")



initialize_db(app)
initialize_routes(api)