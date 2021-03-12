from flask import Flask
from flask_cors import CORS

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)

from divvy_api import routes, models