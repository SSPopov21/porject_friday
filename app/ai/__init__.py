from flask import Blueprint

ai = Blueprint('ai', __name__)

from . import routes, ai_api
