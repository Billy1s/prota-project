from prota import Resource
from prota.models import Card, Score

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


