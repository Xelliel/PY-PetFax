from flask import Blueprint, request, jsonify
from ..models.db import db
from ..models.reptiles import Reptile
from ..models.utils import to_dict
routes = Blueprint('reptiles', __name__, url_prefix="/reptiles")

@routes.get('/')
def index():
  all_reptiles = Reptile.query.all()
  return jsonify(to_dict(all_reptiles))

@routes.post('/')
def create():
  new_reptile = Reptile(**request.json) if request.content_type == 'application/json' else Reptile(**request.form)
  db.session.add(new_reptile)
  db.session.commit()
  return jsonify(to_dict(new_reptile))

@routes.get('/<int:idx>')
def show(idx):
  reptile = Reptile.query.get(idx)
  return jsonify(to_dict(reptile))