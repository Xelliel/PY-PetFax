from flask import Blueprint, render_template, request
import json

routes = Blueprint('pet', __name__, url_prefix="/pets")


@routes.route('/')
def index():
  if request.method == 'GET':
    pets = json.load(open('pets.json'))
    return render_template('pets/index.html', data=pets)
  elif request.method == 'POST':
    print(request.form)
    return 'Thanks for submitting a fun fact!'

@routes.route('/<int:idx>')
def show(idx):
  # print(idx)
  pet = [ pet for pet in json.load(open('pets.json')) if pet["pet_id"] == idx ][0]
  # print (pet)
  return render_template('pets/show.html', pet=pet)