from prota import Resource
from prota.models import Card, Score
from flask import Blueprint, request
from flask_restful import Api
from prota import db

score_api_bp = Blueprint('score/api',__name__)


# API for accessing and updating users score relating to a card (Currently in use for updating score from speed review game #

class Score_api(Resource):
    def get(self):
        if 'userid' in request.json and 'cardid' in request.json:
            userid = request.json['userid']
            cardid = request.json['cardid']
            scorecard = Score.query.filter_by(userid=userid,cardid=cardid).first()
            if scorecard:
                return scorecard.json()

        return {'score':None}


    def post(self):
        userid = request.json['userid']
        cardid = request.json['cardid']
        scorecard = Score.query.filter_by(userid=userid,cardid=cardid).first()
        if scorecard:
            scorecard.score += 1
            db.session.add(scorecard)
            db.session.commit()
            return scorecard.json()

        return {'score':None},404


class All_Cards(Resource):

    def get(self):
        scores = Score.query.all()
        return [score.json() for score in scores]


api = Api(score_api_bp)


api.add_resource(Score_api,'/score')
api.add_resource(All_Cards,'/all_score')