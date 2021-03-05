#imports
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import connexion
from flask_login import LoginManager

import api
import auth

import argparse
import os
import csv
import pandas as pd
from models.db import db
import models.utils as db_utils

APP_DIR = '/home/scairns/code/bairng/server/app/openapi'
OPENAPI_DIR = APP_DIR
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/bairng_server.db'

connex_app = connexion.FlaskApp(__name__, specification_dir=OPENAPI_DIR)
app = connex_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.secret_key = os.environ.get('BAIRNG_SECRET_KEY') #'dev' in dev

login_manager = LoginManager()
login_manager.init_app(app)

connex_app.add_api('bairng_api.yaml', resolver=connexion.RestyResolver('api'))
app.register_blueprint(api.api, url_prefix='/api')
app.register_blueprint(auth.auth_api, url_prefix='/auth')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", dest='debug', help="run in debug mode", action="store_true", default=0)
    args=parser.parse_args()
    app.app_context().push()

    db_utils.init_db(app)

    ##for file name in os sweep data folder #todo: generate these through an initial setup
    #file_name = 'data/user.csv'
    #datafile = pandas.read_csv(file_name)
    #datafile.to_sql(con=engine, index_label='id', name="%s.__tablename__" % file_name, if_exists='replace')

    app.run(host='0.0.0.0', port=5000, debug=args.debug)