from flask import Flask, Response, render_template, request, redirect, url_for
from Config import Config
from SLL.extension import db
from .auth.routes import load_user
from datetime import datetime
from SLL.extension import engine, login_manager, Session
import logging




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login_manager.init_app(app)
    #login_manager.login_view = 'login'
    #login_manager.user_loader(load_user)
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


 # Importer et enregistrer les blueprints
    from .actu import actu as actu_blueprint
    from .auth import auth as auth_blueprint
    from .gouv import gouv as gouv_blueprint
    from .prog import prog as prog_blueprint
    from .publi import publi as publi_blueprint
    from .index import index as index_blueprint
    app.register_blueprint(actu_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(gouv_blueprint)
    app.register_blueprint(prog_blueprint)
    app.register_blueprint(publi_blueprint)
    app.register_blueprint(index_blueprint)

    return app