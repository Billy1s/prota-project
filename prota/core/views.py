from prota import app, db
from flask import render_template, redirect,request,url_for,flash,abort, Blueprint
from flask_login import login_user,login_required,logout_user
from prota.models import User
from prota.users.forms import LoginForm, RegistrationForm

core_blueprints = Blueprint('core',
                              __name__,
                              template_folder='templates/core')

