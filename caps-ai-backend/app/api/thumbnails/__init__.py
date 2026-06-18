from flask import Blueprint

thumbnails_bp = Blueprint('thumbnails', __name__)

from . import routes
