from prota import db
from flask import render_template, redirect,request,url_for,flash,abort, Blueprint
from prota.models import  User, Card, Score, get_score

card_blueprint = Blueprint('card',
                            __name__,
                            template_folder='templates/card')


@card_blueprint.route('view_all',methods=['GET','POST'])
def view_all():
    userid = request.args.get('userid', None)

    cardscore = db.session.query(Card, Score).join(Card).filter(userid == Score.userid)
    cards = Card.query.all()

    for item in cardscore:
        if item[0] in cards:
            cards.pop(cards.index(item[0]))

    return render_template('view_all.html',cards=cards,cardscore=cardscore)


