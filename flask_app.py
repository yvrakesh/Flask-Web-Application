from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# Initialized Instance of Flask 
# Built in variable that is referring to the local python file that we're working with
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=38),nullable=False,unique=True)
    price = db.Column(db.Integer(),nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False,unique=True)
    description = db.Column(db.String(length=1924),nullable=False,unique=True)

    def __repr__(self):
        return f'Item {self.name}'

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