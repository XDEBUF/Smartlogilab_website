# SLL/prog/__init__.py
from flask import Blueprint

prog = Blueprint('prog', __name__)

from . import routes
