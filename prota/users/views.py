from prota import app, db
from flask import render_template, redirect,request,url_for,flash,abort, Blueprint
from flask_login import login_user,login_required,logout_user
from prota.models import User
from prota.users.forms import LoginForm, RegistrationForm

# Views for User Class #

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates/users')



@users_blueprint.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('index'))

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash("Email not registered")
        print("pas1")
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in Successfully!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('users.welcome_user')

            return redirect(next)

    if form.email.data:
        flash("Please enter a valid email format")
    return render_template('login.html',form=form)

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)
