from models import Base
from flask_sqlalchemy import SQLAlchemy   
from models.db import db

class Req(Base):
    __tablename__ = 'req'
    req_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), nullable=True)

    def __repr__(self):
        return '<Req $d (id:$d)>' % self.req_id