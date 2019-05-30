import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_restful import Api, Resource, url_for


login_manager = LoginManager()

app = Flask(__name__)

Bootstrap(app)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)


login_manager.init_app(app)


login_manager.login_view = "users.login"

from prota.core.views import core_blueprints
from prota.users.views import users_blueprint
from prota.card.views import card_blueprint
from prota.speedreview.views import speedreview_blueprint
from prota.card.cards_api import cards_api_bp
from prota.score.score_api import score_api_bp

app.register_blueprint(core_blueprints,url_prefix="/core")
app.register_blueprint(users_blueprint, url_prefix="/user")
app.register_blueprint(card_blueprint, url_prefix="/card")
app.register_blueprint(speedreview_blueprint, url_prefix="/speedreview")
app.register_blueprint(cards_api_bp,url_prefix='/cards/api')
app.register_blueprint(score_api_bp,url_prefix='/score/api')

