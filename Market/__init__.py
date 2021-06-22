from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# Initialized Instance of Flask 
# Built in variable that is referring to the local python file that we're working with
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from Market import routes



