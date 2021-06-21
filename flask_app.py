from flask import Flask, render_template
# Initialized Instance of Flask 
# Built in variable that is referring to the local python file that we're working with
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
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