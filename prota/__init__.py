import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_restful import Api, Resource, url_for

# Create a login manager object
login_manager = LoginManager()

app = Flask(__name__)
Bootstrap(app)
# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Bootstrap(app)
Migrate(app,db)

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "login"

from prota.core.views import core_blueprints
from prota.users.views import users_blueprint
from prota.card.views import card_blueprint
from prota.speedreview.views import speedreview_blueprint

app.register_blueprint(core_blueprints,url_prefix="/core")
app.register_blueprint(users_blueprint, url_prefix="/user")
app.register_blueprint(card_blueprint, url_prefix="/card")
app.register_blueprint(speedreview_blueprint, url_prefix="/speedreview")

api = Api(app)

from prota.card.cards_api import Card_api, All_Cards

api.add_resource(Card_api,'/card/<int:id>')
api.add_resource(All_Cards,'/card/all')