# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import Bootstrap
from flask_bootstrap import Bootstrap

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Bootstrap
bootstrap = Bootstrap(app) 

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# index page
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')

#Quiz page
@app.route('/takequiz/<name>/')
def quiz(name):
    return render_template('quiz/takeQuiz.html', name=name)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.authentication.controllers import authentication as auth
from app.quiz_builder.controllers import quiz as quiz
from  app.statistic.controllers import statistic as stat
#from  app.quiz.controllers import takeQuiz as takeQuiz
# Register blueprint(s)
app.register_blueprint(auth)
app.register_blueprint(quiz)
app.register_blueprint(stat)
#app.register_blueprint(takeQuiz)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()