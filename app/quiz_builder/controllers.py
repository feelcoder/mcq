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
@quiz.route('/add',methods=['GET','POST'])
def quizform():

    # If sign in form is submitted
    form = QuizAddForm(request.form)
    if form.validate_on_submit():
        if form.closed.data equal "pv":
            closed = 1
        else:
            closed = 0  
        quiz = Quiz(form.title.data, form.instructions.data, form.uid.data ,form.time.data ,form.start_date.data ,form.total_marks.data, closed)
        db.session(quiz)
        db.commit()

        if quiz.id:
            flash('Quiz %s succesfully created' % quiz.title)
            redirect(url_for(''))  

    return render_template("quiz_builder/quizadd.html", form=form)