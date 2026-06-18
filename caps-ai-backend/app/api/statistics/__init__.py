from flask import Blueprint

stats_bp = Blueprint('statistics', __name__)

from . import routes
