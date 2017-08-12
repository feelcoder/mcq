# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash


# Import the database object from the main app module
from sqlalchemy.orm import Session



from app import db, statistic
from app.authentication.models import User
from app.quiz_builder.models import Quiz

# Define the blueprint: 'auth', set its url prefix: app.url/auth
takeQuiz = Blueprint('takeQuiz', __name__, url_prefix='/takeQuiz')
