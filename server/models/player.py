from models import Base, utils
from flask_sqlalchemy import SQLAlchemy
from models.db import db

PLAYER_NAME_SIZE = 80

class Player(Base):
    __tablename__ = 'player'
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(PLAYER_NAME_SIZE), unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), nullable=True)
    char_id = db.Column(db.Integer, db.ForeignKey('game_char.char_id'), nullable=True)
    status = db.Column(db.String(1), nullable=False, default='A')
    faction = db.Column(db.String(1), nullable=True)
    current_life = db.Column(db.Integer, nullable=False)
    maximum_life = db.Column(db.Integer, nullable=True)
    traits = db.Column(utils.TextPickleType(), nullable=False)

    

    def __repr__(self):
        return '<Player %r (id:$d)>' % self.player_name, player_id