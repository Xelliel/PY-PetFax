from flask import Blueprint, render_template, request, redirect
from ..models.db import db
from ..models.facts import Fact
routes = Blueprint('fact', __name__, url_prefix="/facts")


@routes.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    all_facts = Fact.query.all()
    return render_template('facts/index.html', data=all_facts)
  elif request.method == 'POST':
    new_fact = Fact(**request.form)
    db.session.add(new_fact)
    db.session.commit()
    return redirect('/facts')

@routes.route('/new', methods=['GET'])
def form():
  if request.method == 'GET':
    return render_template('facts/form.html')