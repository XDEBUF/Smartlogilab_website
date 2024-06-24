# SLL/actu/__init__.py
from flask import Blueprint

actu = Blueprint('actu', __name__)

from . import routes
