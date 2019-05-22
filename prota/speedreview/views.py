from prota import db
from flask import render_template, redirect,request,url_for,flash,abort, Blueprint
from prota.models import  User, Card

speedreview_blueprint = Blueprint('speedreview',
                            __name__,
                            template_folder='templates/speedreview')



@speedreview_blueprint.route('/game',methods=['GET','POST'])
def game():
    cards = Card.query.all()
    return render_template('game.html',cards=cards)