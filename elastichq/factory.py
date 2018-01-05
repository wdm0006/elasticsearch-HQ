from flask import Flask, render_template
from elastichq.settings import ProdConfig
from elastichq.extensions import bcrypt, db, migrate
from elastichq.models.user import User
from elastichq.api import endpoints
from elastichq.views import public


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(endpoints.blueprint)
    app.register_blueprint(public.blueprint)


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
        
    return None
