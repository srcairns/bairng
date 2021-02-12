#imports
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import argparse
import api
import connexion

APP_DIR = '/home/scairns/code/bairng/server/app/openapi'
OPENAPI_DIR = APP_DIR
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/bairng_server.db'

connex_app = connexion.FlaskApp(__name__, specification_dir=OPENAPI_DIR)
app = connex_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

#login_manager = LoginManager()
#login_manager.init_app(app)
connex_app.add_api('bairng_api.yaml')
app.register_blueprint(api.api, url_prefix='/api')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", dest='debug', help="run in debug mode", action="store_true")
    args=parser.parse_args()

    db.create_all()
    db.session.commit()

    app.run(host='0.0.0.0', port=5000, debug=args.debug)