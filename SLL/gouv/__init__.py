# SLL/gouv/__init__.py
from flask import Blueprint

gouv = Blueprint('gouv', __name__)

from . import routes
