from prota import db
from prota.models import User,Card,Score, load_user, load_card, get_score


# def get_or_create(session, model, **kwargs):
#     instance = session.query(model).filter_by(**kwargs).first()
#     if instance:
#         return instance
#     else:
#         instance = model(**kwargs)
#         session.add(instance)
#         session.commit()
#         return instance




#print(load_user(1))
# print(load_card(1))
#
# score = Score(1,1,1)
#
# print(score.score)
#
# db.session.add(score)
# db.session.commit()

#b = Score.query.filter_by(userid=1,cardid=2).first()
#
# test = get_score(1,[2,1,3,4])
# print(type(test))
# for item in test:
#     print(item.userid,item.cardid,item.score)
#
#
scores = Score.query.all()
cards = Card.query.all()
u = 1
testc = db.session.query(Card)
#gets only ones with socre
#test = db.session.query(Card,Score).join(Score).filter(u == Score.userid and Card.id == Score.cardid)


all = db.session.query(Card,Score).join(Card).filter(1 == Score.userid)

# for item in all:
#     print(item[0])
#     if item[0] in cards:
#         #print("pop" + cards[item[0]])
#         cards.pop(cards.index(item[0]))
#
#
#
# print(cards)
# print(all[0][0] == cards[0])

#print(all)

for item in all:
    print(item)
    print(item[1].score)