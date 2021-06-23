from Market.forms import LoginForm, RegisterForm
from Market import app
from flask import render_template,redirect,url_for, flash, get_flashed_messages
from Market.models import Item, User
from Market.forms import RegisterForm
from Market.models import db
from flask_login import login_user,logout_user, login_required


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
@login_required
def market_page():
    items = Item.query.all()
    return render_template('market.html',items = items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        db.session.add(User(username=form.username.data, email_address=form.email.data, password=form.password1.data))
        db.session.commit()
        flash(f'Success! Your account with username "{form.username.data}" is successfully created',category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}: # If there are no errors for validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating an user:{err_msg}',category='danger')
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash("Username and Password don't match! Please try Again",category='danger')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been successfully logged out',category='info')
    return redirect(url_for("home_page"))

# @app.route('/profile/<username>')
# def user_profile(username):
#     return f'<h1>This is {username}'