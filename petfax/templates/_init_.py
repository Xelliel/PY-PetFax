from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate

def create_app():
  load_dotenv()

  app = Flask(__name__)
  app.config['TEMPLATES_AUTO_RELOAD'] = True

  # Database
  app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  from .models.db import db
  db.init_app(app)
  migrate = Migrate(app, db)

  from .blueprints import pets
  app.register_blueprint(pets.routes)

  from .blueprints import facts
  app.register_blueprint(facts.routes)

  from .blueprints import reptiles
  app.register_blueprint(reptiles.routes)

  # from .blueprints.api import api
  # app.register_blueprint(api.routes)

  return app