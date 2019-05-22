from prota import db
from flask import render_template, redirect,request,url_for,flash,abort, Blueprint
from prota.models import  User, Card

card_blueprint = Blueprint('card',
                            __name__,
                            template_folder='templates/card')


@card_blueprint.route('view_all',methods=['GET','POST'])
def view_all():
    cards = Card.query.all()
    return render_template('view_all.html',cards=cards)


#    <td>{{card.eng_snd.replace(' ','')}}</td>