from prota import db
from flask import render_template, redirect,request,url_for,flash,abort, Blueprint
from prota.models import  User, Card, update_score

speedreview_blueprint = Blueprint('speedreview',
                            __name__,
                            template_folder='templates/speedreview')



@speedreview_blueprint.route('/game',methods=['GET','POST'])
def game():
    cards = Card.query.all()
    return render_template('game.html',cards=cards)



@speedreview_blueprint.route('scorescreen',methods=['GET','POST'])
def scorescreen():
    form = request.form
    print(form[0])

    #print(type(cardid))
    # split = cardid.split(",")
    # idl = []
    # for item in split:
    #     idl.append(int(item))
    #
    # print(idl)

    return render_template('scorescreen.html')

@speedreview_blueprint.route('updatescore',methods=['POST'])
def updatescore():
    form = request.form
    cardid = int(form['cardid'])
    userid = int(form['userid'])

    update_score(userid,cardid)
    print("success")
    return ('', 204)



#window.location = "{{ url_for("speedreview.scorescreen",cardid=cardid) }}"

