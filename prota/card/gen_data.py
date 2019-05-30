from prota.models import Card
from prota import db

# Script to populate db with #

card1 = {
    "fr": "salut",
    "eng": "hi",
    "fr_snd": "static/sounds/fr-1/level-1/f-1-f.mp3,"
              "static/sounds/fr-1/level-1/f-1-m.mp3",
    "eng_snd": "static/sounds/fr-1/level-1/e-1.mp3"
}

card2 = {
  "fr":"quoi de neuf ?",
  "eng":"what's up?",
  "fr_snd":"static/sounds/fr-1/level-1/f-2-f.mp3,"
           "static/sounds/fr-1/level-1/f-2-m.mp3",
    "eng_snd":"static/sounds/fr-1/level-1/e-2.mp3"
}
card3 = {
  "fr":"allons-y !",
  "eng":"let's go!",
  "fr_snd":"static/sounds/fr-1/level-1/f-3.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-3.mp3"
}
card4 = {
  "fr":"santé !",
  "eng":"cheers!",
  "fr_snd":"static/sounds/fr-1/level-1/f-4-f.mp3,"
           "static/sounds/fr-1/level-1/f-4-m.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-4.mp3"
}
card5 = {
  "fr":"oui",
  "eng":"yes",
  "fr_snd":"static/sounds/fr-1/level-1/f-5-f.mp3,static/sounds/fr-1/level-1/f-5-m.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-5.mp3"
}
card6 = {
  "fr":"non",
  "eng":"no",
  "fr_snd":"static/sounds/fr-1/level-1/f-6-f.mp3,"
           "static/sounds/fr-1/level-1/f-6-m.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-6.mp3"
}
card7 = {
  "fr":"s'il vous plaît",
  "eng":"please",
  "fr_snd":"static/sounds/fr-1/level-1/f-7-f.mp3,"
           "static/sounds/fr-1/level-1/f-7-m.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-7.mp3"
}
card8 = {
  "fr":"merci",
  "eng":"thank you",
  "fr_snd":"static/sounds/fr-1/level-1/f-8-f.mp3,"
           "static/sounds/fr-1/level-1/f-8-m.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-8.mp3"
}
card9 = {
  "fr":"bonjour",
  "eng":"good morning; good day",
  "fr_snd":"static/sounds/fr-1/level-1/f-9-f.mp3,"
           "static/sounds/fr-1/level-1/f-9-m.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-9.mp3"
}
card10 = {
  "fr":"bonne nuit",
  "eng":"good night",
  "fr_snd":"static/sounds/fr-1/level-1/f-10-f.mp3,"
           "static/sounds/fr-1/level-1/f-10-m.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-10.mp3"
}
card11 = {
  "fr":"à bientôt",
  "eng":"see you later",
  "fr_snd":"static/sounds/fr-1/level-1/f-11-f.mp3,"
           "static/sounds/fr-1/level-1/f-11-m.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-11.mp3"
}
card12 = {
  "fr":"au revoir",
  "eng":"goodbye",
  "fr_snd":"static/sounds/fr-1/level-1/f-12-f.mp3,"
           "static/sounds/fr-1/level-1/f-12-m.mp3",
  "eng_snd":"static/sounds/fr-1/level-1/e-12.mp3"
}


dictofcards = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12]

for card in dictofcards:
    a = Card(fr=card["fr"],eng=card["eng"],fr_snd=card["fr_snd"],eng_snd=card["eng_snd"])
    db.session.add(a)
    db.session.commit()

print(Card.query.all())

for i in Card.query.all():
    print(i.eng_snd)