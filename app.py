from prota import app, db
from flask import render_template
from prota.models import Card

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/test',methods=['GET','POST'])
def test():
    cards = Card.query.all()
    return render_template('test.html',cards=cards)

@app.route('/testview',methods=['GET','POST'])
def testview():
    cards = Card.query.all()
    return render_template('testview.html',cards=cards)

@app.route('/testquiz',methods=['GET','POST'])
def testquiz():
    cards = Card.query.all()
    return render_template('testquiz.html',cards=cards)



if __name__ == '__main__':
    app.run(debug=True)
