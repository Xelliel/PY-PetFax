from flask import Blueprint, render_template, request, redirect
routes = Blueprint('api', __name__, url_prefix="/api")

from . import facts
routes.register_blueprint(facts.routes)