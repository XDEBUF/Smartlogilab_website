# SLL/actu/__init__.py
from flask import Blueprint

index = Blueprint('index', __name__)

from . import routes