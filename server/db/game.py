from base import Base
from flask_sqlalchemy import SQLAlchemy    
db = SQLAlchemy()

class Game(Base):
    __tablename__ = 'game'
    game_id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Game %r (id:$d)>' % self.game_name, game_id