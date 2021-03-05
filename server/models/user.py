from models import Base
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy    
from models.db import db
import json

USERNAME_SIZE = 64
PASS_SIZE = 100
EMAIL_SIZE = 128

class User(Base):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(1), nullable=False, default='A')
    authenticated = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(EMAIL_SIZE), unique=True)
    username = db.Column(db.String(USERNAME_SIZE), unique=True, nullable=False)
    _password_hash = db.Column(db.String(PASS_SIZE))

    def __repr__(self):
        return json.dumps({'id' : self.user_id, 'username' : self.username,})
    
    def is_authenticated(self):
        return self.authenticated
    
    def is_active(self):
        return (self.status == 'A')
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id



def create_user(user_details):
    user_details_dict = user_details
    if 'password' in user_details_dict.keys():
        user_details_dict['password_hash'] = generate_password_hash(user_details_dict['password'])
    new_user = User(email = user_details_dict['email'], username = user_details_dict['username'], _password_hash = user_details_dict['password_hash'])
    db.session.add(new_user)
    db.session.flush()
    return new_user

#@login_manager.user_loader
#def user_loader(user_id):
#    return User.query.get(user_id)