from prota import Resource
from prota.models import Card, Score
from flask import Blueprint
from flask_restful import Api

cards_api_bp = Blueprint('/cards/api',__name__)


# API for accessing cards (not used for anything yet) #


class Card_api(Resource):

    def get(self,id):
        card = Card.query.filter_by(id=id).first()

        if card:
            return card.json()

        return {'card':None},404


class All_Cards(Resource):

    def get(self):
        cards = Card.query.all()
        return [card.json() for card in cards]





api = Api(cards_api_bp)


api.add_resource(Card_api,'/<int:id>')
api.add_resource(All_Cards,'/all')

