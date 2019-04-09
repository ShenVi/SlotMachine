__author__ = 'Ran'

from flask import Blueprint
game = Blueprint('game', __name__)
from ..game import views