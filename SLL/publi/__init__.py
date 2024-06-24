# SLL/publi/__init__.py
from flask import Blueprint

publi = Blueprint('publi', __name__)

from . import routes
