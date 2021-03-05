from flask import Flask, Blueprint, request, abort
from flask_login import current_user, login_user
from flask_sqlalchemy import SQLAlchemy
#from werkzeug.security import check_password_hash
from models.db import db
from models import user
import json

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return {} #something saying login already successful
     
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return {} #something saying login was successful
     
    return {} # something saying "what are you doing?"

@auth_api.route('/create_user', methods=['POST']) #superuser only, once superuser created
def create_user():
    #if not request.json or not 'user' in request.json:
        #abort(400)
    new_user = user.create_user(request.json['user'])
    db.session.commit()
    location = 'auth/user/' + str(new_user.user_id)
    return {'self' : location}, 201

@auth_api.route('/dump_users') #superuser only
def dump_users():
    pass #dump into csvs in data folder using pandas?
