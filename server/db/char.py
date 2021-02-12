import utils
from base import Base
from flask_sqlalchemy import SQLAlchemy    
db = SQLAlchemy()

TRAITS_BLURB_LENGTH = 1024

class Char(Base):
    __tablename__ = 'char'
    char_id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(80), unique=True, nullable=False)
    life = db.Column(db.Integer, nullable=True)
    traits = db.Column(utils.TextPickleType(), nullable=False)
    traits_blurb = db.Column(db.String(TRAITS_BLURB_LENGTH), nullable=False)

    def __repr__(self):
        return '<Character %r (id:$d)>' % self.char_name, char_id