from flask import Flask, Blueprint
import game_engine
from werkzeug.security import check_password_hash
from db import user

#todo: connexion and swagger a restful API

api = Blueprint('simple_page', __name__)

@api.route('/', defaults={'page': 'test'})

@api.route('/test')
def test():
    return {'content': 'Hello, World!',}

@api.route('/create_user')
def create_user():
    return user.create_user()
