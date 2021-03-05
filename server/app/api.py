from flask import Flask, Blueprint
import game_engine
from models import user
from flask_login import login_required
#from models.db import db

api = Blueprint('api', __name__)

@api.route('/', defaults={'page': 'test'})

@api.route('/test')
def test():
    return {'content': 'Hello, World!',}


@api.route('/test_login')
@login_required
def test_login():
    return {'content': 'Hello, Specific Person!',}