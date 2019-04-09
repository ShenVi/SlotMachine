__author__ = 'Ran'

from flask import Blueprint
account = Blueprint('account', __name__)
from ..account import views