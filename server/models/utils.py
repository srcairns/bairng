import json
import sqlalchemy
from sqlalchemy.types import TypeDecorator

SIZE = 256

def init_db(app):
    import models
    from models.game_char import GameChar
    from models.game import Game
    from models.player import Player
    from models.req import Req
    from models.user import User
    from models.db import db
    
    db.init_app(app)
    models.Base.metadata.create_all(bind=db.engine)
    db.session.commit()


class TextPickleType(TypeDecorator):

    impl = sqlalchemy.Text(SIZE)

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value
