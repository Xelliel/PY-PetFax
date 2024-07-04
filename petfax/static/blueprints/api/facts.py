from flask import Blueprint, render_template, request, redirect
from ...models.db import db
from ...models.facts import Fact
from ...models.utils import to_dict
routes = Blueprint('facts-api', __name__, url_prefix="/facts")

@routes.route('/', methods=["GET", "POST"])
def index():
  if request.method == 'GET':
    facts = Fact.query.all()
    facts_list = [ to_dict(fact) for fact in facts ]
    return facts_list
  elif request.method == 'POST':
    new_fact = Fact(**request.json)
    db.session.add(new_fact)
    db.session.commit()
    return request.json


@routes.route('/<int:id>', methods=["GET"])
def show(id):
    fact = Fact.query.filter_by(id=id).first()
    return to_dict(fact)