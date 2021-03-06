from prota import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_required

# class models for database #


#############
### users ###
#############

# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)



def load_card(card_id):
    return Card.query.get(card_id)
#############
### card ###
#############

class Card(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer,primary_key=True)
    fr = db.Column(db.Text)
    eng = db.Column(db.Text)
    fr_snd = db.Column(db.Text)
    eng_snd = db.Column(db.Text)

    def __init__(self,fr,eng,fr_snd,eng_snd):
        self.fr = fr
        self.eng = eng
        self.fr_snd = fr_snd
        self.eng_snd = eng_snd

    def json(self):
        return {'id':self.id,'fr':self.fr,'eng':self.eng,'fr_snd':self.fr_snd,'eng_snd':self.eng_snd}





#############
### score ###
#############

class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer,db.ForeignKey('users.id'))
    cardid = db.Column(db.Integer, db.ForeignKey('cards.id'))
    score = db.Column(db.Integer,default=0)

    def __init__(self,userid,cardid,score):
        self.userid = userid
        self.cardid = cardid
        self.score = score

    def json(self):
        card = Card.query.filter_by(id=self.cardid).first()
        return {'score':self.score,'userid':self.userid,'cardid':self.cardid,'fr':card.fr,'eng':card.eng,'fr_snd':card.fr_snd,'eng_snd':card.eng_snd}



def update_score(userid,cardid):
    c = Score.query.filter_by(userid=userid, cardid=cardid).first()
    if c == None:
        newc = Score(userid,cardid,1)
        db.session.add(newc)
    else:
        c.score += 1
        db.session.add(c)
    db.session.commit()


