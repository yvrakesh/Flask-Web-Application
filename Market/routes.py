from Market import app
from flask import render_template
from Market.models import Item

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items = items)

# @app.route('/')
# def hello_world():
#     return '<h1>Hello World</h1>'

# @app.route('/about')
# def about_page():
#     return '<h1>You are in routes page</h1>'

# @app.route('/profile/<username>')
# def user_profile(username):
#     return f'<h1>This is {username}'