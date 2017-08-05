# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.quiz_builder.forms import QuizAddForm

# Import module models (i.e. User)
from app.quiz_builder.models import Quiz

# Define the blueprint: 'auth', set its url prefix: app.url/auth
quiz = Blueprint('quiz', __name__, url_prefix='/quiz')
# Set the route and accepted methods
@quiz.route('/add/')
def quizform():

    # If sign in form is submitted
    form = QuizAddForm(request.form)
    return render_template("quiz_builder/quizadd.html", form=form)