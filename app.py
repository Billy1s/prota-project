from prota import app, db
from flask import render_template
from prota.models import Card

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
